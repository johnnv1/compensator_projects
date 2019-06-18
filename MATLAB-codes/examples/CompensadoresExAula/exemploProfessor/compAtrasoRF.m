% -------------------------------------------------------------------------
% Projeto do controlador em atraso via resposta em frequência
% Prof. Rodrigo Iván Goytia Mejía
% -----------------------------------------------------------
close all
clear
clc

%% Passo 1. Comportamento do sistema em malha aberta
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nit = 100;
t = 0:1:Nit;
rampa = t;
degrau = ones(1,Nit+1);

Gma = tf(1,conv([1 0],[1 1]));
Gmazpk = zpk(Gma);

figure
subplot(2,1,1), lsim(Gma,degrau,t), grid
subplot(2,1,2), lsim(Gma,rampa,t), grid

figure
bode(Gma), grid;
[gm,pm,wcg,wcp] = margin(Gma); % Verificando a MF e MG do sistema

% Especificações do controlador
MFd = 50;
Mfolga = 5;
evd = 0.02;

%% Passo 1. Calculando o ganho do controlador Kc
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kv = 1/evd;
Kc = Kv/Gmazpk.k;

%% Passo 2. Determinando a frequencia de corte de projeto
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[mag,phase,w] = bode(Gma);

w = squeeze(w);
mag = squeeze(mag);
phase = squeeze(phase);

MFd = MFd+Mfolga;
wcd = round(w(find(180+phase<=MFd,1,'first')),2)

%% Passo 3. Determinando o valor do parâmetro a
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[magKGma,phaseKGma,wKGma] = bode(Kc*Gma);

figure
bode(Kc*Gma), grid;

wKGma = squeeze(wKGma);
magKGma = squeeze(magKGma);
phaseKGma = squeeze(phaseKGma);

KcGma_wcd = 20*log10(round(magKGma(find(wKGma>=wcd,1,'first')),2))

a = inv(10^(-(KcGma_wcd/20)))

%% Passo 4. Determinando o valor do parâmetro T
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T = 10/wcd

%% Passo 5. Determinação do controlador C
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C = Kc*tf([T 1],[T*a 1]);

%% Passo 6. Avaliação do comportamento do sistema realimentado
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gmf = feedback(Gma*C,1);

yGmf=lsim(Gmf,rampa,t);
evr = rampa(end)-yGmf(end)

figure
bode(Gma), hold on
bode(C)
bode(Gma*C), grid
legend('Gma','C','Gma*C')

figure
subplot(2,1,1), 
lsim(Gmf,degrau,t), hold on,  grid
legend('yref','y')
title('Avaliando regime transitório')

subplot(2,1,2), 
lsim(Gmf,rampa,t), grid
legend('yref','y')
title('Avaliando regime estacionário')