% -------------------------------------------------------------------------
% Projeto do controlador por avan�o de fase via LR
% Prof. Rodrigo Iv�n Goytia Mej�a
% -------------------------------------------------------------------------
close all
clear
clc

% Apliacr este controlador quando existams problemas de desempenho no
% regime transit�rio

Nit = 100;
t = 0:1:Nit;
rampa = t;
degrau = ones(1,Nit+1);

%% Paso 1. An�lise do comportamento do sistema em malha aberta
% ------------------------------------------------------------------
Gma = tf (0.1,conv([1 1],[1 0.5]));  % Planta em malha aberta
polos = pole(Gma);
zeros = zero(Gma);
infoGma = stepinfo(Gma);

figure
subplot(2,2,1), lsim(Gma,degrau,t), grid
subplot(2,2,2), lsim(Gma,rampa,t), grid
subplot(2,2,[3 4]), rlocus(Gma), sgrid

%% Paso 2. Definir as especifica��es do sistema em malha fechada
% ------------------------------------------------------------------
epd = 0.1; % Erro de posi��o desejado,  epd <= 1/(1+Kp)
Mpd = 10;  % M�ximo sobresinal desejado, Mp <=10
tsd = 2;   % Tempo de estabiliza��o, ts <= 2 s

%% Paso 3. Par�metros desejados a atingir os requisitos de desempenho
% ------------------------------------------------------------------

% 1. Ganho do controlador, Kc
syms Kp
eqn = epd == 1/(1+Kp);
Kp = solve(eqn,Kp);

syms Kc
eqn = Kp == Kc*dcgain(Gma);
Kc = solve(eqn,Kc);

% 2. Coeficiente de amortecimento, zeta
zeta = 0:0.01:1;
Mp = 100*exp(-zeta*pi./sqrt(1-zeta.^2));
Mp_folga = 5;
zeta = round(zeta(find(Mp>=Mpd-Mp_folga,1,'last')),1);

% 3. Frequencia Natural, wn
syms wn
eqn = tsd == 4/(zeta*wn);
wn = round(double(solve(eqn,wn)),0);

% Paso 4. Projeto do Compensador em Avan�o de fase via LR
% ----------------------------------------------------------

% 1. Determinando a posi��o do zero do controlador

% a) P�los dominantes do sistema em MF
s1 = -zeta*wn+1i*wn*sqrt(1-zeta^2);
s2 = -zeta*wn-1i*wn*sqrt(1-zeta^2);

% b) Escolhando a posi��o do zero
zero_c = -2.1;

% 2. Determinando a posi��o do p�lo do controlador

% a) Determinando phi3 pela condi��o de fase
for k=1:length(polos)
    if abs(real(s1))>abs(polos(k))
        phipolo(k) = 180-atand(abs(real(s1))/abs(real(s1)-polos(k)));
    else
        phipolo(k) = atand(abs(real(s1))/abs(real(s1)-polos(k)));
    end
end
phi3 = 180 - sum(phipolo) + 90;

% b) Determina��o da posi��o do p�lo 
syms d
eqnx = tand(phi3) == imag(s1)/d;
polo_c = - (double(solve(eqnx,d))+abs(zero_c));

% 3. Determinando o ganho do controlador pela condi��o de ganho

h(1) = sqrt(imag(s1)^2+1.6^2);
h(2) = sqrt(imag(s1)^2+1.1^2);
h(3) = sqrt(imag(s1)^2+4.5^2);
c = imag(s1);

Kc = abs(prod(h)/(0.1*c));

% 4. Definindo a fun��o de transfer�ncia do controlador
C = Kc*tf([1 -zero_c],[1 -polo_c]);

% 5. Avaliando o comportamento do controlador em malha fechada
Gmf = feedback(series(C,Gma),1);
infoGmf = stepinfo(Gmf)

figure
subplot(2,2,1), lsim(Gmf,degrau,t), grid
subplot(2,2,2), lsim(Gmf,rampa,t), grid
subplot(2,2,[3 4]), rlocus(Gmf), sgrid
