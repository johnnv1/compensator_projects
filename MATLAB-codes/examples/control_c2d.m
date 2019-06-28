% -------------------------------------------------------------------------
% Converter controle de continuo para discreto
% -------------------------------------------------------------------------
close all
clear all
clc

%% Planta de primeira ordem
fs = 10
[u,t]           = gensig('square',200, 450, 1/fs);

Gs              = tf([2.096], [1 3.759])
Gz              = c2d(Gs, 1/fs, 'tustin');
Gz.variable     = 'z^-1'

% Controlador em avanço por lugar das raizes Kc = Kc
% Cs              = tf([2.835 3.78], [1 6.946])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes Kc = 5*Kc
% Cs              = tf([14.18 18.9], [1 6.946])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes Kc = 10*Kc
% Cs              = tf([28.35 37.8], [1 6.946])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes Kc = 10*Kc e colocando o zero
% em 3/4*sigma
% Cs              = tf([12.71 12.71], [1 3.625])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes Kc = 10*Kc e colocando o zero
% em sigma/3
% Cs              = tf([5.1814 2.584], [1 1.722])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes colocando o zero em 3/4*sigma
% Cs              = tf([1.271 1.271], [1 3.625])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em atraso por lugar das raizes Kc = Kc
% Cs              = tf([0.7391 1.742], [1 0.03])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço-atraso por lugar das raizes
% Cs              = tf([2.835 18.51 19.64], [1 6.976 0.2084])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% 
% yGmf = lsim(feedback(Cz*Gz,1),u, t);
% figure
% plot(t, yGmf), hold on
% plot(t, u)
% figure
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço-atraso por lugar das raizes com o zero em sigma/2
% Cs              = tf([0.7364 10.26 6.513], [1 2.333 0.0691])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% 
% yGmf = lsim(feedback(Cz*Gz,1),u, t);
% figure
% plot(t, yGmf), hold on
% plot(t, u)
% figure
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço-atraso por lugar das raizes com o zero em sigma*3/4
% Cs              = tf([1.271 11.52 10.25], [1 3.655 0.1088])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% 
% yGmf = lsim(feedback(Cz*Gz,1),u, t);
% figure
% plot(t, yGmf), hold on
% plot(t, u)
% figure
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal


% Controlador em avanço por resposta em frequencia
% Cs              = tf([0.5134 47.71], [0.04137 1])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por resposta em frequencia fazendo Kc = Kc / 2
% Cs              = tf([0.5089 23.85], [0.08546 1])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por resposta em frequencia alternando o erro
% esperado para 0.1
% Cs              = tf([0.533 4.711], [0.6376 1])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em atraso por resposta em frequencia
% Cs              = tf([7.593 47.71], [0.2915 1])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em atraso por resposta em frequencia alternando o erro
% esperado para 0.1
% Cs              = tf([0.7593 4.771], [0.8689 1])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em atraso por resposta em frequencia alternando o erro
% esperado para 0.03
% Cs              = tf([2.531 15.9], [0.2607 1])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal



%% Planta de segunda ordem
fs = 10
[u,t]           = gensig('square',200, 450, 1/fs);

Gs              = tf([0.2023 8.817 96.12], [1 30.25 77.26])
Gz              = c2d(Gs, 1/fs, 'tustin');
Gz.variable     = 'z^-1'

% Controlador em avanço por lugar das raizes Kc = Kc
% Cs              = tf([6.497 25.99], [1 23.94])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes colocando o zero em sigma/2
% Cs              = tf([7.357 14.71], [1 28.32])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes colocando o zero em sigma/10
% Cs              = tf([8.46 3.384], [1 34])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes colocando o zero em sigma/10 e
% mudando o tempo de estabelecimento para 2
% Cs              = tf([59.05 11.81], [1 205.6])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal
% 

% Controlador em avanço por lugar das raizes colocando o zero em sigma*2 e
% mudando o tempo de estabelecimento para 1
% Cs              = tf([5.542 44.33], [1 19.97])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes colocando o zero em sigma*2 e
% mudando o tempo de estabelecimento para 1
% Cs              = tf([5.542 44.33], [1 19.97])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal


% Controlador em avanço por lugar das raizes colocando o zero em sigma*1.5 e
% mudando o tempo de estabelecimento para 1
% Cs              = tf([5.942 35.65], [1 21.39])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanço por lugar das raizes colocando o zero em sigma*4.5 e
% mudando o tempo de estabelecimento para 1
% Cs              = tf([4.355 78.38], [1 20.75])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em atraso por lugar das raizes
% Cs              = tf([4.108 13.08], [1 0.04])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanco-atraso por lugar das raizes com o zero em sigma*4.5
% Cs              = tf([4.355 82.79 79.25], [1 20.79 0.8299])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal

% Controlador em avanco por resposta em frequencia
% Cs              = tf([0.4402 4.894], [1.529 1])
% Cz              = c2d(Cs, 1/fs, 'tustin');
% Cz.variable     = 'z^-1'
% rlocus(feedback(Cz*Gz,1))
% zgrid
% axis equal


% Controlador em atraso por resposta em frequencia
Cs              = tf([7.867 494.3], [1.592 1])
Cz              = c2d(Cs, 1/fs, 'tustin');
Cz.variable     = 'z^-1'
rlocus(feedback(Cz*Gz,1))
zgrid
axis equal

% Controlador em atraso por resposta em frequencia erro esperado = 0.15
Cs              = tf([0.5245 32.95], [0.1061 1])
Cz              = c2d(Cs, 1/fs, 'tustin');
Cz.variable     = 'z^-1'
rlocus(feedback(Cz*Gz,1))
zgrid
axis equal