% -------------------------------------------------------------------------
% Projeto do controlador em atraso e avanço
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
% G(s) = 1 / ((s+5)*(s+1)*s)
%   Especificações de MF
%       ep(inf) <= 0.1  %erro no infinito
%       Mp% <= 10   
%       ts <= 4 %segundos
% -----------------
K_g = 1;
Numerador = K_g;
Denominador = conv(conv([1 5],[1 1]), [1 0]);
    %especificações de projeto
tsEsp = 4;
MpEsp = 10;     %10% de sobre sinal
Mp_folga = 5;   %5% de folga -- folga serve para garantir a aproximaçã ode sistema de ordem 3 ou superior para modelagem de 2 ordem
evEstacionarioEsp = 0.1;


%% 2. Analise do comportamento do sistema eem MA
%Funçao de transferencia em malha aberta (MA)
Gma = tf(Numerador, Denominador)

polos = pole(Gma);
zeros = zero(Gma);
infoGma = stepinfo(Gma)

ev_Gma = 1 - dcgain(Gma)        % erro de velocidade
%grafica a resposta do sistema em MA a entrada de uma rampa e um degrau 
figure
subplot(2,2,1), lsim(Gma, degrau, t), grid
subplot(2,2,2), lsim(Gma, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gma), sgrid


%% 3. Analise do sistema em MF

for K = 10:10:31
    Gmf = feedback(Gma, K);
    yGmf = lsim(Gmf, rampa, t);
    ev_Gmf = rampa(end) - yGmf(end)    % erro de velocidade
%     figure
%     subplot(2,2,1), lsim(Gmf, degrau, t), grid
%     subplot(2,2,2), lsim(Gmf, rampa, t), grid
%     subplot(2,2,[3 4]), rlocus(Gmf), sgrid
end

%% 4. parametros desejados a atingir os requisitos de desempenho
%1. coeficiente de amortecimento, psi
psi = 0:0.01:1;
MpVetor = 100*exp(-psi*pi./sqrt(1-psi.^2));
psi  = round(psi(find(MpVetor >= double(MpEsp-Mp_folga),1,'last')),1)

%2. frequencia natural, Wn
syms wn
eqn = tsEsp == 4/(psi*wn);
wn = round(double(solve(eqn, wn)),2)

wn = 3 %consideração feita devido a planta ser de 3ra ordem

%parametros
sigma = psi * wn
wd = wn*sqrt(1-psi^2)

%3. polos dominantes do 1sistema em MF
s1 = -sigma+1i*wd;
s2 = -sigma-1i*wd;

%% 4. Projeto do controlador por avanço de fase via LR
% for zero = max(polos)-0.1:-0.01:-2*sigma
% a) define a posição do zero
% zero_c = zero
zero_c = -sigma

if abs(sigma) > abs(real(zero_c))
    thetaZero = 180 - atand(wd/abs(-sigma -  real(zero_c)))
else
    thetaZero = atand(wd/abs(-sigma -  real(zero_c)))
end

% b) determina o angulo do polo

for k=1:length(polos)
    if abs(real(s1)) > abs(polos(k))
        phipolo(k) = 180-atand(abs(real(s1))/abs(real(s1)-polos(k)))
    else
        phipolo(k) = atand(abs(real(s1))/abs(real(s1)-polos(k)))
    end
end
phiPolo_C = 180 - sum(phipolo) + thetaZero
%     if(phi > 0)
%         break
%     end
% end

% c) deter,omamdp a posição do pólo
syms d
eqnx = tand(phiPolo_C) == imag(s1)/d;
polo_c = - (abs(double(solve(eqnx,d)))+abs(zero_c))

% d)determinando o ganho Kc do controlador via condição de modulo
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
Cav = Kc * tf([1 abs(zero_c)],[1 abs(polo_c)]);

%% 5. compensador no sistema realimentado
%avaliando  ocomportamento do controlador em MF
Gmf = feedback(series(Cav,Gma), 1)
yGmf_rampa = lsim(Gmf, rampa, t);
ev_WC = rampa(end) - yGmf_rampa(end)    % erro de vel   ocidade

yGmf_degrau = lsim(Gmf, degrau, t);
ep_WC = degrau(end) - yGmf_degrau(end)    % erro de velocidade

figure
subplot(2,2,1), lsim(Gmf, degrau, t), grid  %%erro aqui vai ser 0
subplot(2,2,2), lsim(Gmf, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gmf), sgrid

% para analizar o quanto pode aumentar o Kc na mao
% figure
% rlocus(Gma), 
% figure
% rlocus(Gmf)
%Kc = 2.45 * Kc

%% -------------------------------------------------------------------------
%% Controlador em atraso
% ajuste de Kc na mao
Kc2 = 2.45 * Kc
Cav = tf([1 abs(zero_c)],[1 abs(polo_c)])
%% controlador em avanço
Cat = tf([1 abs(0.12)],[1 abs(0.02)])
%% Controlador geral
C = Kc2*series(Cav,Cat)
%% Verifica o sistema com o novo controlador
Gmf = feedback(series(C,Gma), 1)

infoGmf = stepinfo(Gmf)
yGmf_rampa = lsim(Gmf, rampa, t);
ev_WC = rampa(end) - yGmf_rampa(end)    % erro de vel   ocidade

yGmf_degrau = lsim(Gmf, degrau, t);
ep_WC = degrau(end) - yGmf_degrau(end)    % erro de velocidade

figure
subplot(2,2,1), lsim(Gmf, degrau, t), grid  %%erro aqui vai ser 0
subplot(2,2,2), lsim(Gmf, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gmf), sgrid
