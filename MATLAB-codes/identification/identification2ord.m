close all

%% CHANGE HERE
freq = 10;
mat = csvread('identification.csv');

%% program
stepsize = 1/freq;
N = length(u);
u = mat(:,1);
y = mat(:,2);
time = N/freq;
t = 0:stepsize:(time-stepsize);

%% algoritmo
teta    = [0;0;0;0];            % Par�metros inicias do sistema
theta   = [0;0;0;0];            % Par�metros inicias do sistema 
P       = eye(4);               % Inicializa��o da Matriz de covari�ncia

% -----------------------------------------------------
yest2   = zeros(N+1,1);

ys = zeros (3,1); 	% Inicializa��o do vetorx de sa�da

m = 1; 
for k= 3:N

    % Identifica��o via MQR
    % ----------------------------------------------
    phi         = [-y(k-1); -y(k-2); u(k-1); u(k-2)];   % Matriz de observa��o
    yest2(k)    = phi'*theta;                            % Sa�da estimada
    eest        = (y(k)-yest2(k));                      % Erro de estima��o
    theta       = theta+P*phi*eest;                     % Par�metros estimados MQR
    P           = P-P*(phi*phi')*P/(1+phi'*P*phi);      % Atualiza��o de P
    
    teta(:,m)   = theta;
    ys(k) = teta(1,m)*ys(k-1)+teta(2,m)*ys(k-2)+teta(3,m)*u(k-1)+teta(4,m)*u(k-2);
    
    m = m+1;
end

% theta
figure
dma = tf([theta(3) theta(4)],[1 theta(1) theta(2)],stepsize);
dma.Variable = 'z^-1'
ma = d2c(dma,'tustin')
lsim(dma,'r--',ma,'g-',u,t)
hold on
plot(t,y)
legend('modelo gerado','entrada','original')

stepinfo(ma)
    