% -------------------------------------------------------------------------
% Projeto do compensador em atraso de fase via resposta em Freq
% João Gustavo Atkinson Amorim
% Prof. Rodrigo Iván Goytia Mejia
% -------------------------------------------------------------------------
close all
clear all
clc

%% 1. Especificações de projeto
Nit = 100;
t = 0:1:Nit;
rampa = t;
degrau = ones(1, Nit+1);

% ------------------
% G(s) = 1 / ((s+1)*s)=
%       ev(inf) <= 0.02  %erro no infinito 
%       50 < MFd < 60        % em graus, margem de fase desejada
%-----------------
K_g = 1;
Numerador = K_g;
Denominador = conv([1 1], [1 0]);
    %especificações de projeto
MFd = 50;               %em graus, margem de fase desejada
MFseg   = 5;                        % margem de fase de segurança, variavel
eVelocidade = 0.02;   %erro no tempo infinito


%% 2. Analise do comportamento do sistema em MA
%Funçao de transferencia em malha aberta (MA)
Gma = tf(Numerador, Denominador)

Gma_zpk = zpk(Gma);  % ganho com valores do polo e zero, zpk = zero polo ganho

[mag,phase,wout] = bode(Gma);
wout = squeeze(wout);       % transforma em um vetor, os w, vetor de frequencia
mag = squeeze(mag);         % transforma em um vetor, a magnitude, vetor de magnitude em valor (ñ Db)
phase = squeeze(phase);     % transforma em um vetor, as fases, vetor de fases
% figure
% bode(Gma)

%% 3. Determinar o ganho do compensador  (passo 1)
Kv_min  = 1 / eVelocidade
Kp      = Gma_zpk.K

Kc = Kv_min / Kp

%% 4. Avaliação do comportamento do sistema sendo o compensador = Kc
Cat = Kc
Gma_Cat = series(Gma,Cat)
[gm, pm, wcg, wcp] = margin(Gma)
figure
bode(Gma), hold on,
bode(Gma_Cat)
legend('Gma', 'Gma * Kc')
[gm, pm, wcg, wcp] = margin(Gma_Cat)    % Verificando a MF e MG do sistema, MF= margem de fase, MG = margem de ganho

%% 5. Determinar a localização da resposnta em frequencia (RF) do compensador, Wm (passo 3)
magDb = 20*log10(mag);

% Lugar em que cruzar pela reta [-C_jwm -C_jwm] é referente a frequencia Wm
figure
subplot(2,1,1), semilogx(wout, magDb)
ylabel('ganho(dB)'), grid
subplot(2,1,2), semilogx(wout,phase)
ylabel('fase(graus)')
xlabel('frequencia (rad/s)')

Wcd  = round(wout(find(180+phase <= (MFseg+MFd),1,'first')),3)   %frequencia de corte desejada

%% 6. Determinar o valor de a do compensador (passo 2)
[mag,phase,wout] = bode(Gma_Cat);
wout_Cat = squeeze(wout);       % transforma em um vetor, os w, vetor de frequencia
mag_Cat = squeeze(mag);         % transforma em um vetor, a magnitude, vetor de magnitude em valor (ñ Db)
phase_Cat = squeeze(phase);     % transforma em um vetor, as fases, vetor de fases
magDb_Cat = 20*log10(mag_Cat);
KcG_WCD = round(magDb_Cat(find(wout >= Wcd,1,'first')),3)
a = 10^(abs(KcG_WCD)/20)
%% 7. Determinar do parametro T do compensador (passo 4)
T = 10 /(Wcd)

%% 8. Monta/constroi o controlador em avanço
Cav = Kc * tf([T 1], [a*T 1])

%% Avaliação do comportamento do sistema sendo o compensador = Kc * ((T*s+1)/(T*a*s+1))
Gma_Cav = series(Gma,Cav)
Gmf = feedback(series(Gma,Cav),1)

figure
bode(Gma), hold on,
bode(Gma_Cav)
legend('Gma', 'Gma * Kc * ((T*s+1)/(T*a*s+1)')

[gm, pm, wcg, wcp] = margin(Gmf)    % Verificando a MF e MG do sistema, MF= margem de fase, MG = margem de ganho

infoGmf = stepinfo(Gmf)
yGmf = lsim(Gmf, rampa, t);
ev_WC = rampa(end) - yGmf(end)    % erro de velocidade,     WC = with control
figure
subplot(2,2,1), lsim(Gmf, degrau, t), grid  %%erro aqui vai ser 0
subplot(2,2,2), lsim(Gmf, rampa, t), grid
subplot(2,2,[3 4]), rlocus(Gmf), sgrid
