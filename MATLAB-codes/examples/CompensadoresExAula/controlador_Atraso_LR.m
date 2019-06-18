% -------------------------------------------------------------------------
% Projeto do controlador em atraso
% João Gustavo Atkinson Amorim
% Prof. Rodrigo Iván Goytia Mejia
% -------------------------------------------------------------------------
close all
clear all
clc


%% 1. Especificações de projeto
% aplicar o controlador quando existtam problemas de desempenho em regime
% permanente

Nit = 100;
t = 0:1:Nit;
rampa = t;
degrau = ones(1, Nit+1);

% ------------------
% G(s) = 30 / ((s+5)*(s+3)*(s+2.5))
%   Especificações de MF
%       ep(inf) <= 0.1  %erro no infinito
%       Mp% <= 10   
%       ts <= 2 %segundos
%-----------------
K_g = 30;
Numerador = K_g;
Denominador = conv(conv([1 5],[1 3]), [1 2.5]);
    %especificações de projeto
tsEsp = 2;
MpEsp = 10;     %10% de sobre sinal
Mp_folga = 5;   %5% de folga -- folga serve para garantir a aproximaçã ode sistema de ordem 3 ou superior para modelagem de 2 ordem
epEstacionarioEsp = 0.1;

%% 2. Analise do comportamento do sistema eem MA
%Funçao de transferencia em malha aberta (MA)
Gma = tf(Numerador, Denominador)

polos = pole(Gma);
zeros = zero(Gma);
infoGma = stepinfo(Gma);

ep_Gma = 1 - dcgain(Gma)        %erro de posição com ganho unitário
%grafica a resposta do sistema em MA a entrada de uma rampa e um degrau 
figure
subplot(2,2,1), lsim(Gma, degrau, t), grid
subplot(2,2,2), lsim(Gma, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gma), sgrid


% Em conclusão existe erro em regime permanente e o erro em regime
% transitorio nao é consideravel portanto se projetara um compensador em
% atraso


%% 3. parametros desejados a atingir os requisistos de desempenho
%1 ganho com controlador, Kc
syms Kp
eqn = epEstacionarioEsp == 1/(1+Kp);
Kp = solve(eqn,Kp)

syms Kc
eqn = Kp == Kc*dcgain(Gma);
Kc = solve(eqn,Kc)

%2. coeficiente de amortecimento, psi
psi = 0:0.01:1;
MpVetor = 100*exp(-psi*pi./sqrt(1-psi.^2));
psi  = round(psi(find(MpVetor >= double(MpEsp-Mp_folga),1,'last')),1)

%3. frequencia natural, Wn
syms wn
eqn = tsEsp == 4/(psi*wn);
wn = round(double(solve(eqn, wn)),2)

%parametros
sigma = psi * wn
wd = wn*sqrt(1-psi^2)

%4. polos dominantes do 1sistema em MF
s1 = -sigma+1i*wd;
s2 = -sigma-1i*wd;


%% 4. Projeto do controlkador por atraso de fase via LR
% A) determinando o zero e o polo do controlador
    % polo =  tem que ser um valor pequeno
    % zero = polo + delta
    % polo e o zero tem que estar proximos de zero para amplificar 
    % Kc deve ser aproximadamente 1, mas nao foi calculado ainda, isto deve
    % ocorrer para que nao ocorra erro no regime transitorio
    
% Primeira tentativa / chute
polo_c = 0.01;  % polo do controlador
    %Kp = lim {Kc *G(s)*(s+Z_c)/(s+P_c)} quando s tende a 0
zero_c = double(polo_c*(Kp / dcgain(Gma)));

% Segunda tentativa / chute
polo_c = 0.165134;  % polo do controlador
    %Kp = lim {Kc *G(s)*(s+Z_c)/(s+P_c)} quando s tende a 0
zero_c = double(polo_c*(Kp / dcgain(Gma)));

% B) determinação do ganho Kc, pela condição de modulo
%polo sistema - sigma = polo sistema - polo dominante 
for k=1:length(polos)
    h(k) = sqrt(( abs(imag(s1)) - abs(imag(polos(k))) )^2 + ( abs(real(s1)) - abs(real(polos(k))) )^2); %Distancia dos polos da planta ate um polo dominante
end
h(k+1) = sqrt( ( abs(imag(s1)) - abs(imag(polo_c)) )^2 + ( abs(real(s1)) - abs(real(polo_c)) )^2 ); %Distancia do polo do compensador ate um polo dominante
c = sqrt( ( abs(imag(s1)) - abs(imag(zero_c)) )^2 + ( abs(real(s1)) - abs(real(zero_c)) )^2 );  %Distancia do zero do compensador ate um polo dominante

Gmazpk = zpk(Gma);
Kplanta = Gmazpk.K;
Kc = prod(h) / (c*Kplanta)


%   C) montando o compensador em atraso de fase
%função de transferencia do controlador
C = Kc * tf([1 abs(zero_c)], [1 abs(polo_c)])

%% 5. compensador no sistema realimentado
%avaliando  ocomportamento do controlador em MF
Gmf = feedback(series(C,Gma), 1);
infoGmf = stepinfo(Gmf)

yGmf_rampa = lsim(Gmf, rampa, t);
ev_WC = rampa(end) - yGmf_rampa(end)    % erro de vel   ocidade

yGmf_degrau = lsim(Gmf, degrau, t);
ep_WC = degrau(end) - yGmf_degrau(end)    % erro de velocidade
figure
subplot(2,2,1), lsim(Gmf, degrau, t), grid
subplot(2,2,2), lsim(Gmf, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gmf), sgrid

