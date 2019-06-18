% -------------------------------------------------------------------------
% Projeto do controlador em avanço
% João Gustavo Atkinson Amorim
% Prof. Rodrigo Iván Goytia Mejia
% -------------------------------------------------------------------------
close all
clear all
clc

% -------------------------------------------------------------------------
%                       Etapas
% 1. Consideramos G(s) aproximada a uma planta de 2ª ordem
% 2. Representação do lugar de raizes considerando C(s) = Kc
% 3. Verificar se o problema do sistema em MF se encontra no comportamento transitorio.
%     3.1 Se isso for verdade projeta o controlador em avanço
% 4. Tradução das especificações em termos da equação caracteristica de MF
% 5. Encontrar o zero e o pólo do C(s) usando a condição de fase
% 6. Encontrar o ganho Kc usando a condição de módulo
% 7. Respeitando (5) e (6) o lugar das raizes do sistema cumpiram com as especificações
% 8. Simular e realizar sintonia fina nos parametros z, p e Kc do controlador
% -------------------------------------------------------------------------

%% Especificações de projeto

Nit = 100;
t = 0:1:Nit;
rampa = t;
degrau = ones(1, Nit+1);

% ------------------
% G(s) = 0.1 / ((s+1)*(s+0.5))
%   Especificações de MF
%       ep(inf) <= 0.1  %erro no infinito
%       Mp% <= 10   
%       ts <= 2 %segundos
%-----------------
K_g = 0.1;
Numerador = K_g;
Denominador = conv([1 1],[1 0.5]);

tsEspMax = 2;
tsEspMin = -inf;
MpEspMax = 10;
MpEspMin = 0;
epEstacionarioEspMax = 0.1;
epEstacionarioEspMin = -inf;


%% 1. Consideramos G(s) aproximada a uma planta de 2ª ordem
%Funçao de transferencia em malha aberta (MA)
Gma = tf(Numerador, Denominador)
ep_Gma = 1 - dcgain(Gma)        %erro de posição co m ganho unitário
%Pega os polos e zeros
polos = pole(Gma);
zeros = zero(Gma);

%% 2. Representação do lugar de raizes considerando C(s) = Kc = 1   

%Pega as informações do sistema
infoGma = stepinfo(Gma)

%grafica a resposta do sistema em MA a entrada de uma rampa e um degrau 
figure
subplot(2,2,1), lsim(Gma, degrau, t), grid
subplot(2,2,2), lsim(Gma, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gma), sgrid

%% 3. Tradução das especificações em termos da equação caracteristica de MF
%1. ganho do controlador , Kc 
syms Kp
eqn = epEstacionarioEspMax == 1/(1+Kp);
Kp = solve(eqn,Kp);

syms Kc
eqn = Kp == Kc*dcgain(Gma);
Kc = solve(eqn,Kc)

%2. coeficiente de amortecimento, psi
psi = 0:0.01:1;
MpVetor = 100*exp(-psi*pi./sqrt(1-psi.^2));
Mp_folga = 5;   %5% de folga
psi  = round(psi(find(MpVetor >= double(MpEspMax-Mp_folga),1,'last')),1)

%3. frequencia natural, Wn
syms wn
eqn = tsEspMax == 4/(psi*wn);
wn = round(double(solve(eqn, wn)),3)

%parametros
sigma = psi * wn
wd = wn*sqrt(1-psi^2)

%% 4. Encontrar o zero e o pólo do C(s) usando a condição de fase

%determinando a posição do zero
%a) polos dominantes do 1sistema em MF
s1 = -sigma+1i*wd;
s2 = -sigma-1i*wd;
%b) escolhendo a posição do zero
zero_c = -sigma

if abs(sigma) > abs(real(zero_c))
    thetaZero = 180 - atand(wd/abs(-sigma -  real(zero_c)))
else
    thetaZero = atand(wd/abs(-sigma -  real(zero_c)))
end
% -------------------------------------------------------------------------
% determinando a posição do polo
% a) determinando phi3 pela condição de fase
for k=1:length(polos)
    if abs(real(s1)) > abs(polos(k))
        phipolo(k) = 180-atand(abs(real(s1))/abs(real(s1)-polos(k)))
    else
        phipolo(k) = atand(abs(real(s1))/abs(real(s1)-polos(k)))
    end
end
phi3 = 180 - sum(phipolo) + thetaZero

%b) determinaçao da posição do polo
syms d
eqnx = tand(phi3) == imag(s1)/d;
polo_c = - (abs(double(solve(eqnx,d)))+abs(zero_c))

%% 5. Encontrar o ganho Kc usando a condição de módulo

for k=1:length(polos)
    h(k) = sqrt(( abs(imag(s1)) - abs(imag(polos(k))) )^2 + ( abs(real(s1)) - abs(real(polos(k))) )^2); %Distancia dos polos da planta ate um polo dominante
end
h(k+1) = sqrt( ( abs(imag(s1)) - abs(imag(polo_c)) )^2 + ( abs(real(s1)) - abs(real(polo_c)) )^2 ); %Distancia do polo do compensador ate um polo dominante
c = sqrt( ( abs(imag(s1)) - abs(imag(zero_c)) )^2 + ( abs(real(s1)) - abs(real(zero_c)) )^2 );  %Distancia do zero do compensador ate um polo dominante

Gmazpk = zpk(Gma);
Kplanta = Gmazpk.K;
Kc = prod(h) / (c*Kplanta)

%% 6. Respeitando (5) e (6) o lugar das raizes do sistema cumpiram com as especificações
%função de transferencia do controlador
C = Kc * tf([1 abs(zero_c)], [1 abs(polo_c)])

%avaliando  ocomportamento do controlador em MF
Gmf = feedback(series(C,Gma), 1)
infoGmf = stepinfo(Gmf)

yGmf_rampa = lsim(Gmf, rampa, t);
ev_WC = rampa(end) - yGmf_rampa(end)    % erro de velocidade

yGmf_degrau = lsim(Gmf, degrau, t);
ep_WC = degrau(end) - yGmf_degrau(end)    % erro de velocidade

figure
subplot(2,2,1), lsim(Gmf, degrau, t), hold on
subplot(2,2,2), lsim(Gmf, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gmf), sgrid