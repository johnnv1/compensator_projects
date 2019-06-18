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
N           = 2047;             % Número de amostras
Fs          = 500;               % Frequencua de amostragem, Hz
Ts          = 1/Fs;             % Periodo de amostragem, seg
t           = 0:Ts:N*Ts;        % Vetor de tempo de simulação, seg

kini        = 1;
y           = zeros (kini,1); 	% Inicialização do vetorx de saída

umax        = 5;                % Máximo valor do sinal de controle
umin        = 0;                % Mínimp valor do sinal de controle

Te          = zeros (kini,1);   % Inicialização do tempo de espera no ciclo
    
Stop        = 1;
ysaida      = line (nan,nan,'Color','k','LineWidth',2); 
uctrle      = line (nan,nan,'Color','r','LineWidth',2);
uicontrol ('Style','Pushbutton','String','Parar','Callback','Stop = 0;');

%% Sinal de Exitação Binario Pseudo Randomico (PRBS)
% -----------------------------------------------------
wmin        = 0.1;
wmax        = 1;
amp         = 4.8;

u           = 2.5*ones(N,1);

%% Algoritmo para exitação do sistema MTG
% -----------------------------------------------------
for k=kini:N
    Tc=cputime;
    % Saida do processo
    % ----------------------------------------------
    y(k) = readVoltage(ar,'a0');

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
% save MTG_data_step u y

%% Impressão dos resultados
% -----------------------------------------------------
figure
subplot(2,1,1), plot(y,'k','linewidth',2)
subplot(2,1,2), plot(u,'k','linewidth',2)