close all

%% CHANGE HERE
freq = 10;
mat = csvread('PRBS-FS10.csv',1,0);

%% program
stepsize = 1/freq;
u = mat(:,1);
y = mat(:,2);
N = length(u);
time = N/freq;
t = 0:stepsize:(time-stepsize);

%% algoritmo
teta    = [0;0];            % Parâmetros inicias do sistema
theta   = [0;0];            % Parâmetros inicias do sistema 
P       = eye(2);               % Inicialização da Matriz de covariância

% -----------------------------------------------------
yest2   = zeros(N+1,1);

ys = zeros (2,1); 	% Inicialização do vetorx de saída

m = 1; 
for k= 2:N

    % Identificação via MQR
    % ----------------------------------------------
    phi         = [-y(k-1); u(k)];   % Matriz de observação
    yest2(k)    = phi'*theta;                            % Saída estimada
    eest        = (y(k)-yest2(k));                      % Erro de estimação
    theta       = theta+P*phi*eest;                     % Parâmetros estimados MQR
    P           = P-P*(phi*phi')*P/(1+phi'*P*phi);      % Atualização de P
    
%    teta(:,m)   = theta;
%    ys(k) = teta(1,m)*ys(k-1)+teta(2,m)*ys(k-2)+teta(3,m)*u(k-1)+teta(4,m)*u(k-2);    
%    m = m+1;
end

% theta
figure
dma = tf([theta(2)],[1 theta(1)],stepsize);
dma.Variable = 'z^-1'
ma = d2c(dma,'tustin')
lsim(dma,'r--',ma,'g-',u,t)
hold on
plot(t,y)
legend('modelo gerado','entrada','original')

stepinfo(ma)
    