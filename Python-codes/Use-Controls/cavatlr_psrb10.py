### ATENÇÃO ###
# Antes de executar instale o pyfirmata:
  # pip install pyfirmata --user
# E compile no arduino o código do ArduinoIDE encontrado em:
  # Arquivo -> Exemplos -> Firmata -> StandardFirmata

### IMPORTANTE ###
# O valor da frequencia fica aproximado

# imports
import pyfirmata
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# for live plotting
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

### INICIO MUDANÇAS PERMITIDAS ###
# vetor de entrada (V)
sinal = 4*np.ones(50)
sinal = np.append(sinal,0*np.ones(50))
sinal = np.append(sinal,5*np.ones(50))
sinal = np.append(sinal,1*np.ones(50))
sinal = np.append(sinal,2*np.ones(50))
# frequência de amostragem
freq = 10
# portas arduino
board = pyfirmata.Arduino('COM10')
entrada = board.get_pin('d:9:p')
saida = board.get_pin('a:0:i')
### FIM MUDANÇAS PERMITIDAS ###

x = [i for i,a in enumerate(sinal)]

### CONTROLADOR ###
b0 = 12.85
b1 = -17.09
b2 = 4.268
a1 = -0.1886
a2 = 0.8078
### FIM CONTROLADOR ###


print("Tempo total para executar as medições:",len(sinal)/freq)

# configuration
it = pyfirmata.util.Iterator(board)
it.start()
saida.enable_reporting()

# main
#vetor de resposta
resposta = 0*np.copy(sinal)
sinalnovo = 0*np.copy(sinal)
# cria arquivo
with open('exemplo.txt','w') as f:
  pass
# espera as configurações surtirem efeito
time.sleep(0.5)
#live plotting
# registra o tempo de inicio
ini = time.time()
for i in range(2,len(sinal)):
  # lê com a porta analogica
  aux = saida.read()
  if(aux != None):
    # salva no vetor resultado
    resposta[i] = float(aux)*5
    print("Valor lido:",resposta[i])
  sinalnovo[i] = b0*(sinal[i] - resposta[i]) + b1*(sinal[i-1] - resposta[i-1]) + b2*(sinal[i-2] - resposta[i-2]) - a1*(sinalnovo[i-1]) - a2*(sinalnovo[i-2])
  if(sinalnovo[i] > 5):
    sinalnovo[i] = 5
  if(sinalnovo[i] < 0):
    sinalnovo[i] = 0
  # escreve no PWM
  entrada.write(sinalnovo[i]/5)
  print("valor esperado:",sinal[i])
  print("valor escrito:",sinalnovo[i])
  # adiciona valor lido ao arquivo
  with open('exemplo.txt','a') as f:
    f.write(str(sinal[i])+','+str(resposta[i])+'\n')
  # gera delay para esperar pelo período de amostragem
  time.sleep(1/freq-0.001)
# registra o tempo de término
end = time.time()
# printa informações
print("tempo:",end-ini)
print("frequencia real:",(len(sinal)-2)/(end-ini))
# print("media:",np.mean(resposta))
entrada.write(0)
board.exit()
# plota os gráficos
ax1.plot(x,sinal)
ax2.plot(x,resposta)
ax3.plot(x,sinalnovo)
plt.show()