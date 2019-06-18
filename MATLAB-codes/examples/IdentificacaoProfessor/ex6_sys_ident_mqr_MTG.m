% ------------------------------------------------------------------------
% Algoritmo de M�nimos Quadrados Recursivo
% Rodrigo Ivan Goytia Mejia
% ------------------------------------------------------------------------
close all
clear
clc

%% Definindo o modelo cont�nuo do processo para gerar dados
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sys = tf(1,[1 2 1]);        % Modelo do processo de 2da Ordem

Nit = 100;                  % Quantidade de amostras
Ts  = 0.1;              	% Per�odo de amostragem
t   = 0:Ts:Nit*Ts;      	% Vetor de tempo
t   = t';

u   = rand(Nit+1,1);      	% Vetor de entrada
y   = lsim(sys,u,t);      	% Vetor de sa�da

%% Identificando o modelo de 2da ordem com um modelo de 1ra ordem
%  G(z) = b0/(z+a1) = b0*z^-1/(1+a1*z^-1) = Y/U
%  y(k) = -a1*y(k-1)+b0*u(k-1)
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
yest2    = zeros(Nit+1,1);

 theta   = [0;0];            % Par�metros inicias do sistema de 1ra ordem
% theta   = [0.977; 0.02426];


% Experimentar:
% 1. Testar com uma matriz P como a matriz identidade
% 2. Testar com uma matriz P = 1000 vezes maior a matriz identidade
% % P       = eye(2);           % Inicializa��o da Matriz de covari�ncia
P       = 10*eye(2);           % Inicializa��o da Matriz de covari�ncia

% Observa��o:
% Os valores da matriz P no processo iterativo come�am a diminuir e a
% convergencia dos par�metros � mais r�pida portanto a estima��o melhora
% quando se tem valores da matriz P grandes (com um ganho inicial do
% estimador maior). P tende a zero.

% A matriz de covari�ncia est� relacionada com o grau de confian�a que se
% tem nos dados observados, quanto maior esta matriz maior incerteza se tem
% nos dados observados.

% Se sei os valores dos par�metros pr�ximos ao valor verdadeiro devo usar
% uma matriz P pequena. Assim se controla os valores de ganho do estimador.

teta    = zeros(2,Nit+1);
m = 1; 
for k=2:Nit+1
    phi         = [-y(k-1); u(k-1)];                 % Matriz de observa��o
    yest2(k)    = phi'*theta;                       % Sa�da estimada
    eest        = (y(k)-yest2(k));                  % Erro de estima��o
    theta       = theta+P*phi*eest;                 % Par�metros estimados MQR
    P           = P-P*(phi*phi')*P/(1+phi'*P*phi);  % Atualiza��o de P
    
    teta(:,m)   = theta;
    m           = m+1;
    
    figure(1)
    subplot(1,2,1), plot(t,[y yest2])
    subplot(1,2,2), plot(t,[teta'])
    pause(0.1)
end

% O algoritmo de proje��o inicialmente tem uma pobre estima��o devido ao
% par�metros iniciais serem zero, mais ao usar os par�metros obtidos via
% m�nimos quadrados, o desempenho da estima��o melhora consider�velmente.

%% Identificando o processo como um modelo de 2da ordem
%  G(z) = (b0*z+b1)/(z^2+a1*z+a2) = (b0+b1*z^-1)*z^-1/(1+a1*z^-1+a2*z^-2) = Y/U
%  y(k) = -a1*y(k-1)-a2*y(k-2)+b0*u(k-1)+b1*u(k-2)
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
yest2    = zeros(Nit+1,1);

theta   = [0.52;0.43;0.02;0.04];         	% Par�metros inicias do sistema de 2da ordem

% Experimentar:
% 1. Testar com uma matriz P como a matriz identidade
% 2. Testar com uma matriz P = 10 vezes maior a matriz identidade
 P       = eye(4);               % Inicializa��o da Matriz de covari�ncia
% P       = 10*eye(4);       	% Inicializa��o da Matriz de covari�ncia

teta    = zeros(4,Nit+1);
m = 1; 
for k=3:Nit+1
    phi         = [y(k-1); y(k-2); u(k-1); u(k-2)];     % Matriz de observa��o
    
    yest2(k)     = phi'*theta;                          % Sa�da estimada
    eest        = (y(k)-yest2(k));                      % Erro de estima��o
    theta       = theta+P*phi*eest;                     % Par�metros estimados MQR
    P           = P-P*(phi*phi')*P/(1+phi'*P*phi);      % Atualiza��o de P
    
    teta(:,m)   = theta;
    m           = m+1;
    
    figure(1)
    subplot(1,2,1), plot(t,[y yest2])
    subplot(1,2,2), plot(t,[teta'])
    pause(0.1)
end

% Mesmo que os par�metros n�o sejam exatamente iguais a resposta do sistema
% frente a mesma entrada � a mesma, assim os modelos obtidos via MQ online
% s�o v�lidos para projeto de controladores, otimiza��o e outros.