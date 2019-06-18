% -------------------------------------------------------------------------
% Identificando o Motor-Taco-Gerador
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
N           = 2000;             % N�mero de amostras
Fs          = 500;               % Frequencua de amostragem, Hz
Ts          = 1/Fs;             % Periodo de amostragem, seg
t           = 0:Ts:N*Ts;        % Vetor de tempo de simula��o, seg

kini        = 5;
y           = zeros (kini,1); 	% Inicializa��o do vetorx de sa�da

umax        = 5;                % M�ximo valor do sinal de controle
umin        = 0;                % M�nimp valor do sinal de controle

Te          = zeros (kini,1); 	% Inicializa��o do tempo de espera no ciclo
    
Stop        = 1;
ysaida      = line (nan,nan,'Color','k','LineWidth',2); 
uctrle      = line (nan,nan,'Color','r','LineWidth',2);
uicontrol ('Style','Pushbutton','String','Parar','Callback','Stop = 0;');

%% Sinal de Exita��o Binario Pseudo Randomico (PRBS)
% -----------------------------------------------------
wmin        = 0.01;
wmax        = 0.8;
amp         = 4.95;

Band        = [wmin wmax];      % Faixa de frequencias de entrada
Niveis      = [0 amp];          % Amplitude do sinal
u           = idinput(N, 'prbs', Band, Niveis);

yest2    = zeros(N+1,1);
theta   = [0;0];            % Par�metros inicias do sistema 
P       = eye(2);           % Inicializa��o da Matriz de covari�ncia


%% Algoritmo para exita��o do sistema MTG
% -----------------------------------------------------
teta    = zeros(2,N+1);
m = 1; 
for k=kini:N
    Tc=cputime;
    % Saida do processo
    % ----------------------------------------------
    y(k) = readVoltage(ar,'A0');

    % Identifica��o via MQR
    % ----------------------------------------------
    phi         = [-y(k-1); u(k-1)];  % Matriz de observa��o
    yest2(k)    = phi'*theta;                                           % Sa�da estimada
    eest        = (y(k)-yest2(k));                                      % Erro de estima��o
    theta       = theta+P*phi*eest;                                     % Par�metros estimados MQR
    P           = P-P*(phi*phi')*P/(1+phi'*P*phi)                       % Atualiza��o de P
    
    teta(:,m)   = theta;
    m           = m+1;
    
    
    % Satura��o do sinal de controle
    % ----------------------------------------------
    if u(k) >= umax
        u(k) = umax;
    elseif u(k) <= umin
        u(k) = umin;
    end
    
    % Lei de controle
    % ----------------------------------------------
    writePWMVoltage(ar,'D9', u(k))
    
    set(ysaida,'xdata',t(1:k),'ydata',y(1:k)); drawnow
    set(uctrle,'xdata',t(1:k),'ydata',u(1:k)); drawnow
    
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

u = u(1:length(y));
% save MTG_data_prbs u y

%% Impress�o dos resultados
% -----------------------------------------------------
figure
subplot(2,1,1), plot(y,'k','linewidth',2)
subplot(2,1,2), plot(u,'k','linewidth',2)
teta'