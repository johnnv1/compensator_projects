% -------------------------------------------------------------------------
% Projeto de compensador em avanço - atraso de fase
% Prof. Rodrigo Iván Goytia Mejía
% -------------------------------------------------------------------------
close all
clear 
clc

Nit = 100;
t = 0:1:Nit;
rampa = t;
degrau = ones(1,Nit+1);

%% Passo 1. Análise do comportamento do sistema em malha aberta
% ------------------------------------------------------------------
Gma = tf (1,conv(conv([1 5 ],[1 1]),[1 0]));
polos = pole(Gma);
zeros = zero(Gma);
infoGma = stepinfo(Gma)

figure
subplot(2,2,1), lsim(Gma,degrau,t), grid
subplot(2,2,2), lsim(Gma,rampa,t), grid
subplot(2,2,[3 4]), rlocus(Gma), sgrid

%% Passo 2. Análise do comportamento do sistema em malha fechada
% ------------------------------------------------------------------
K = 1;
Gmf1 = feedback(Gma,K);
yGmf1 = lsim(Gmf1,rampa,t);
ev1 = rampa(end) - yGmf1(end)
% Kv1 = dcgain(series(tf([1 0],1),Gma));
% ev1 = 1/Kv1;
% stepinfo(Gmf1)

K = 10;
Gmf2 = feedback(Gma,K);
yGmf2 = lsim(Gmf2,rampa,t);
ev2 = rampa(end) - yGmf2(end)
% Kv2 = dcgain(series(tf([1 0],1),Gma));
% ev2 = 1/Kv2;
% stepinfo(Gmf2)

figure
subplot(1,2,1), 
lsim(Gmf1,degrau,t), grid, hold on,
lsim(Gmf2,degrau,t)
legend('K=1','K=10')

subplot(1,2,2), 
lsim(Gmf1,rampa,t), grid, hold on,
lsim(Gmf2,rampa,t)
legend('K=1','K=10')

figure
rlocus(Gma)

%% Paso 2. Definir as especificações do sistema em malha fechada
% ------------------------------------------------------------------
evd = 0.1; % Erro de posição desejado,  epd <= 1/Kv
Mpd = 10;  % Máximo sobresinal desejado, Mp <=10
tsd = 4;   % Tempo de estabilização, ts <= 4 s

%% Paso 3. Parâmetros desejados a atingir os requisitos de desempenho
% ------------------------------------------------------------------
% 1. Coeficiente de amortecimento, zeta
zeta = 0:0.01:1;
Mp = 100*exp(-zeta*pi./sqrt(1-zeta.^2));
Mp_folga = 5;
zeta = round(zeta(find(Mp>=Mpd-Mp_folga,1,'last')),1)

% 2. Frequencia Natural, wn
syms wn
eqn = tsd == 4/(zeta*wn);
wn = round(double(solve(eqn,wn)),0)
wn = 3;  % Consideração feita devido a planta ser de 3ra ordem

% Paso 4. Projeto do Compensador em Avanço de fase via LR
% ----------------------------------------------------------
% 1. Determinando a posição do zero do controlador

% a) Pólos dominantes do sistema em MF
s1 = -zeta*wn+1i*wn*sqrt(1-zeta^2)
s2 = -zeta*wn-1i*wn*sqrt(1-zeta^2)

% ALTERNATIVA 1
% b) Definir a posição do zero
z_c = -zeta*wn;

% c) Determinando o ângulo do pólo via critério do ângulo
theta = 90;
phi1= 180-atand((wn*sqrt(1-zeta^2))/2.1);
phi2= 180-atand((wn*sqrt(1-zeta^2))/(2.1-1));
phi3= atand((wn*sqrt(1-zeta^2))/(5-2.1));
phi4= 180+theta-(phi1+phi2+phi3)
disp('Inconsistente modificar a posição do zero')

% ALTERNATIVA 2
% b) Definir a posição do zero
zero_c = 0.5;

% c) Determinando o ângulo do pólo via critério do ângulo
theta = 180-atand(wn*sqrt(1-zeta^2)/(2.1-0.5));
phi1= 180-atand((wn*sqrt(1-zeta^2))/2.1);
phi2= 180-atand((wn*sqrt(1-zeta^2))/(2.1-1));
phi3= atand((wn*sqrt(1-zeta^2))/(5-2.1));
phi4= 180+theta-(phi1+phi2+phi3)
disp('Ângulo consitente')

% d) Determinando a posição do pólo
polo_c = 2.1+2.1/tand(phi4)

% e) Determinando o ganho Kc do controlador via condição de módulo

h(1) = sqrt((wn*sqrt(1-zeta^2))^2+(polo_c-2.1)^2)
h(2) = sqrt((wn*sqrt(1-zeta^2))^2+(5-2.1)^2)
h(3) = sqrt((wn*sqrt(1-zeta^2))^2+(2.1-1)^2)
h(4) = sqrt((wn*sqrt(1-zeta^2))^2+(2.1-0)^2)
c =  sqrt((wn*sqrt(1-zeta^2))^2+(2.1-0.5)^2)

Gmazpk = zpk(Gma);
Kc = abs(prod(h)/(Gmazpk.k*c))

% 4. Definindo a função de transferência do controlador
C = Kc*tf([1 zero_c],[1 polo_c]);

% 5. Avaliando o comportamento do controlador em malha fechada
Gmf = feedback(series(C,Gma),1);
Gmf3 = lsim(Gmf,rampa,t); grid
% infoGmf = stepinfo(Gmf)
ev1 = rampa(end) - Gmf3(end)

figure
subplot(2,2,1), lsim(Gmf,degrau,t); grid
subplot(2,2,2), lsim(Gmf,rampa,t); grid
subplot(2,2,[3 4]), rlocus(Gmf); sgrid

figure
rlocus(Gma), hold, rlocus(Gmf)

%% 6. Avaliando o tempo de estabilização
figure
lsim(Gmf,degrau,t); grid

Kc2 = 2.3*Kc;
C = Kc2*tf([1 zero_c],[1 polo_c]);

Gmf = feedback(series(C,Gma),1);
Gmf4 = lsim(Gmf,rampa,t); grid
ev1 = rampa(end) - Gmf4(end)
figure
plot(rampa), hold on, plot(Gmf4)

% Projeto do compensador por atraso
Cav =  Kc2*tf([1 zero_c],[1 polo_c]);
Cat = tf([1 0.12],[1 0.02]);
C = series(Cav,Cat)

Gmf = feedback(series(C,Gma),1);
Gmf5 = lsim(Gmf,rampa,t); grid
ev2 = rampa(end) - Gmf5(end)
figure
plot(rampa), hold on, plot(Gmf5)