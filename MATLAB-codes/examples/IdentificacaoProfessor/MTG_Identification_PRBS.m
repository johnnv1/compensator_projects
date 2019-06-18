% -------------------------------------------------------------------------
% Identificando o Motor-Taco-Gerador
% Rodrigo Ivan Goytia Mejia
% -------------------------------------------------------------------------
close all
clc

%% Configurando o Arduino
% -------------------------------------------------------------------------
if exist ('ar','var')&& isa (ar,'arduino')&& isvalid(ar)
    %Não Fazer Nada
else
    ar = arduino ('COM9');
end
configurePin(ar,'D9','PWM');

%% Parâmetros iniciais
% -------------------------------------------------------------------------
N           = 200;             % Número de amostras
Nit         = 200;
Fs          = 500;               % Frequencua de amostragem, Hz
Ts          = 1/Fs;             % Periodo de amostragem, seg
t           = 0:Ts:N*Ts;        % Vetor de tempo de simulação, seg

kini        = 5;
y           = zeros (kini,1); 	% Inicialização do vetorx de saída

umax        = 5;                % Máximo valor do sinal de controle
umin        = 0;                % Mínimp valor do sinal de controle

Te          = zeros (kini,1); 	% Inicialização do tempo de espera no ciclo
    
Stop        = 1;
ysaida      = line (nan,nan,'Color','k','LineWidth',2); 
uctrle      = line (nan,nan,'Color','r','LineWidth',2);
uicontrol ('Style','Pushbutton','String','Parar','Callback','Stop = 0;');

%% Sinal de Exitação Binario Pseudo Randomico (PRBS)
% -----------------------------------------------------
wmin        = 0.01;
wmax        = 0.8;
amp         = 4.95;

Band        = [wmin wmax];      % Faixa de frequencias de entrada
Niveis      = [0 amp];          % Amplitude do sinal
u           = idinput(N, 'prbs', Band, Niveis);

yest2    = zeros(Nit+1,1);
theta   = [0;0;0;0];            % Parâmetros inicias do sistema 
P       = 100*eye(4);           % Inicialização da Matriz de covariância


%% Algoritmo para exitação do sistema MTG
% -----------------------------------------------------
teta    = zeros(4,Nit+1);
m = 1; 
for k=kini:N
    Tc=cputime;
    % Saida do processo
    % ----------------------------------------------
    y(k) = readVoltage(ar,'A0');

    % Identificação via MQR
    % ----------------------------------------------
    phi         = [-y(k-1); -y(k-2); u(k-1); u(k-2)];  % Matriz de observação
    yest2(k)    = phi'*theta;                                           % Saída estimada
    eest        = (y(k)-yest2(k));                                      % Erro de estimação
    theta       = theta+P*phi*eest;                                     % Parâmetros estimados MQR
    P           = P-P*(phi*phi')*P/(1+phi'*P*phi)                       % Atualização de P
    
    teta(:,m)   = theta;
    m           = m+1;
    
    
    % Saturação do sinal de controle
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

%% Impressão dos resultados
% -----------------------------------------------------
figure
subplot(2,1,1), plot(y,'k','linewidth',2)
subplot(2,1,2), plot(u,'k','linewidth',2)
teta'