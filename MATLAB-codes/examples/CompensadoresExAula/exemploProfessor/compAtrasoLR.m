% -------------------------------------------------------------------------
% Projeto do compensador em atraso
% Prof. Rodrigo Iv�n Goytia Mej�a
% -------------------------------------------------------------------------
close all
clear
clc

% Aplicar o controlador quando existam problemas de desempenho em regime
% permanente

Nit     = 100;              % N�mero de itera��es
t       = 0:1:Nit;          % Tempo
rampa   = t;
degrau  = ones(1,Nit+1);    % Entrada degrau


% Passo 1. Especifica��es de projeto
% --------------------------------------------------------------------
Mpd = 10        % M�ximo sobre-sinal
tsd = 2         % Tempo de estabiliza��o
epd = 0.1       % Erro de posi��o desejado

% Passo 2. An�lise do comportamento do sistema em malha aberta
% --------------------------------------------------------------------
Gma = tf(30,conv(conv([1 5],[1 3]),[1 2.5]));
polos = pole(Gma);
zeros = zero(Gma);
infoGma = stepinfo(Gma)

ep = 1-dcgain(Gma)                  % Erro de posi��o com ganho unit�rio

figure
subplot(2,2,1), lsim(Gma,degrau,t)
subplot(2,2,2), lsim(Gma,rampa,t)
subplot(2,2,[3 4]), rlocus(Gma), sgrid

% Em conclus�o existe erro em regime permanente e o erro em regime
% transit�rio n�o � consider�vel, portanto se projetara um compensador em
% atraso

% Passo 3. Par�metros desejados a atingir os requisitos de desempenho
% --------------------------------------------------------------------
% 1. Ganho con controlador, Kc
syms Kp
eqn = epd == 1/(1+Kp);
Kp = double(solve(eqn,Kp))

syms Kc
eqn = Kp == Kc*dcgain(Gma);
Kc = double(solve(eqn,Kc))

% 2. Coeficiente de amortecimento, zeta
zeta = 0:0.01:1;
Mp = 100*exp(-zeta*pi./sqrt(1-zeta.^2));
Mp_folga = 5;       % Folga de Mp devido ao ganho da malha ser de ordem maior a 2
zeta = round(zeta(find(Mp>=Mpd-Mp_folga,1,'last')),1);

% 3. Frequencia natural, wn
syms wn
eqn = tsd == 4/(zeta*wn);
wn = round(double(solve(eqn,wn)),2);

% 4. P�los dominantes do sistema em malha fechada
s1 = -zeta*wn+1i*wn*sqrt(1-zeta^2)
s2 = -zeta*wn-1i*wn*sqrt(1-zeta^2)

% Passo 4. Projeto do controlador por atraso de fase via LR.
% -------------------------------------------------------------

% a) Determinando o zero e o p�lo do controlador
%    p�lo = tem que ser um valor pequeno
%    zero = p�lo+delta
%    p�lo e o zero tem que estar pr�ximos de zero para amplificar
%    Kc � aproximadamente 1, mais n�o foi calculado

% Primeira tentativa
polo_c = 0.01;      % Valor do p�lo escolhido pelo usu�rio
zero_c = double((Kp/(dcgain(Gma)))*polo_c);

% Segunda tentativa
polo_c = 0.16;      % Valor do p�lo escolhido pelo usu�rio
zero_c = double((Kp/(dcgain(Gma)))*polo_c);

% b) Determina��o do ganho Kc, pela condi��o de m�dulo
h(1) = sqrt(imag(s1)^2+3.16^2);
h(2) = sqrt(imag(s1)^2+1.16^2);
h(3) = sqrt(imag(s1)^2+0.66^2);
h(4) = sqrt(imag(s1)^2+1.83^2);
c    = sqrt(imag(s1)^2+(1.84-zero_c)^2);

Gmazpk = zpk(Gma);
Kplanta = Gmazpk.K;
Kc = prod(h)/(c*Kplanta);
% Kc = 1;

% c) Montando o compensador em atraso de fase
C = Kc*tf([1 zero_c],[1 polo_c]);

% Passo 5. Compensador no sistema realimentado
% --------------------------------------------------------------
Gmf = feedback(series(C,Gma),1);
infoGmf = stepinfo(Gmf)

ep = 1-dcgain(Gmf)                  % Erro de posi��o com ganho unit�rio

figure
subplot(2,2,1), lsim(Gmf,degrau,t), grid
subplot(2,2,2), lsim(Gmf,rampa,t), grid
subplot(2,2,[3 4]), rlocus(Gmf), sgrid