% -------------------------------------------------------------------------
% Valida��o do modelo identificados para o Motor-Taco-Gerador
% Rodrigo Ivan Goytia Mejia
% -------------------------------------------------------------------------
close all
clc

%% Configurando o Arduino
% -------------------------------------------------------------------------
if exist ('ar','var')&& isa (ar,'arduino')&& isvalid(ar)
    %N�o Fazer Nada
else
    ar = arduino ('COM9');
end
configurePin(ar,'D9','PWM');

%% Par�metros iniciais
% -------------------------------------------------------------------------
N           = 2047;             % N�mero de amostras
Fs          = 10;               % Frequencua de amostragem, Hz
Ts          = 1/Fs;             % Periodo de amostragem, seg
t           = 0:Ts:N*Ts;        % Vetor de tempo de simula��o, seg

y           = zeros (N,1);      % Inicializa��o do vetor de sa�da
yest        = zeros (N,1);      % Inicializa��o do vetor de sa�da estimada

umax        = 5;                % M�ximo valor do sinal de controle
umin        = 0;                % M�nimp valor do sinal de controle

Te          = zeros (N,1);      % Inicializa��o do tempo de espera no ciclo
    
Stop        = 1;
ysaida      = line (nan,nan,'Color','k','LineWidth',2); 
ysaidaest   = line (nan,nan,'Color','r','LineWidth',2);
uicontrol ('Style','Pushbutton','String','Parar','Callback','Stop = 0;');

%% Sinal de Exita��o Binario Pseudo Randomico (PRBS)
% -----------------------------------------------------
wmin        = 0.01;
wmax        = 0.5;
amp         = 4.8;

Band        = [wmin wmax];      % Faixa de frequencias de entrada
Niveis      = [0 amp];          % Amplitude do sinal
u           = idinput(N, 'prbs', Band, Niveis);

%% Modelo 1
% -------------------------------------------------------------------------
Kp              = 1.3795;
tau             = 0.16546;
theta           = 0.0367;
Gps             = tf(Kp,[tau 1]);
Gpsd            = Gps;
Gps.ioDelay     = theta;

Gpz             = c2d(Gps,Ts,'zoh');
d               = round(theta/Ts);
Gpz.Variable    = 'z^-1';
Gpz.ioDelay     = d;

figure
step(Gpsd,5), hold on, step(Gpz,5),

%% Algoritmo para exita��o do sistema MTG
% -----------------------------------------------------
for k=2:N
    Tc=cputime;
    % Saida do processo
    % ----------------------------------------------
    y(k)    = readVoltage(ar,'a0');
    yest(k) = 0.5464*yest(k-1)+0.8257*u(k-1);

    % Satura��o do sinal de entrada
    % ----------------------------------------------
    if yest(k) >= 5
        yest(k) = 5;
    elseif yest(k) <= 0
        yest(k) = 0;
    end
    
    % Satura��o do sinal de controle
    % ----------------------------------------------
    if u(k) >= umax
        u(k) = umax;
    elseif u(k) <= umin
        u(k) = umin;
    end
    
    % Lei de controle
    % ----------------------------------------------
    writePWMVoltage(ar, 'D9', u(k))
    
    set(ysaida,'xdata',t(1:k),'ydata',y(1:k)); drawnow
    set(ysaidaest,'xdata',t(1:k),'ydata',yest(1:k)); drawnow
    
    Te(k)=Ts-(cputime-Tc);          
    if Te(k)>0
        pause(Te(k));
    end
    if Stop == 0
        writePWMVoltage(ar,'D9', 0);
        break
    end
end
writePWMVoltage(ar,'D9', 0);

save MTG_data u y

%% Impress�o dos resultados
% -----------------------------------------------------
figure
subplot(2,1,1), plot(y,'k','linewidth',2)
subplot(2,1,2), plot(u,'k','linewidth',2)