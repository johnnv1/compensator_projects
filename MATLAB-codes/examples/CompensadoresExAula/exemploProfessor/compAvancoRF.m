% -------------------------------------------------------------------------
% Projeto do controlador em avanço via resposta em frequência
% Prof. Rodrigo Iván Goytia Mejía
% -----------------------------------------------------------
close all
clear

%% Passo 1. Comportamento do sistema em malha aberta
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nit = 100;
t = 0:1:Nit;
rampa = t;
degrau = ones(1,Nit+1);

Gma = tf(5,conv([1 0],[1 1]));
Gmazpk = zpk(Gma);

figure
subplot(2,1,1), lsim(Gma,degrau,t), grid
subplot(2,1,2), lsim(Gma,rampa,t), grid

figure
bode(Gma)
[gm,pm,wcg,wcp] = margin(Gma) % Verificando a MF e MG do sistema

% Especificações do controlador
MFd = 50;
evd = 0.02;

%% Passo 2. Determinar o ganho Kc do controlador
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kv = 1/evd;
Kc = Kv/Gmazpk.k;

figure
bode(Gma), hold on,
bode(Gma*Kc)
legend('Gma','Gma.Kc')

[gm,pm,wcg,wcp] = margin(Gma*Kc) % Verificando a MF e MG do sistema
MFkc = pm;  % Em graus
MFseg = 3;  % Em graus
phimax = MFd - MFkc + MFseg; % Em graus

%% Passo 3. Determinar o valor de a do controlador
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a = (1 - sind(phimax))/(1+sind(phimax))

%% Passo 4. Determinando a localização da RF do controlador, wm
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C_wm = 20*log10(Kc/sqrt(a)); % Em dB

% w = logspace(-2,2,50);
[mag,phase,w] = bode(Gma);

w = squeeze(w);
mag = squeeze(mag);
phase = squeeze(phase);

figure
subplot(2,1,1),semilogx(w,20*log10(mag),[0.01 100],[-C_wm -C_wm])
ylabel('ganho(dB)'), grid
subplot(2,1,2),semilogx(w,phase)
ylabel('fase(graus)')
xlabel('frequecia(rad/s)')

wm = round(w(find(20*log10(mag)>=-C_wm,1,'last')),2);

%% Passo 5. Determinação do parâmetro do controlador T
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T = 1/(sqrt(a)*wm);

%% Passo 6. Determinação do controlador C
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C = Kc*tf([T 1],[T*a 1]);

%% Passo 7. Avaliação do comportamento do sistema realimentado
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gmf = feedback(Gma*C,1);

yGmf=lsim(Gmf,rampa,t);
evr = rampa(end)-yGmf(end)

figure
bode(Gma), hold on
bode(Gma*C), grid
legend('Gma','Gmf')

figure
subplot(2,1,1), 
lsim(Gmf,degrau,t), grid
title('Avaliando regime transitório')

subplot(2,1,2), 
lsim(Gmf,rampa,t), grid
title('Avaliando regime estacionário')