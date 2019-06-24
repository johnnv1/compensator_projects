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
import matplotlib.animation as animation
from matplotlib import style

### INICIO MUDANÇAS PERMITIDAS ###
# vetor de entrada (V)
sinal = 4*np.ones(50)
sinal = np.append(sinal,0*np.ones(50))
sinal = np.append(sinal,5*np.ones(50))
sinal = np.append(sinal,1*np.ones(50))
sinal = np.append(sinal,2*np.ones(50))
# frequência de amostragem
freq = 50
### FIM MUDANÇAS PERMITIDAS ###

x = [i for i,a in enumerate(sinal)]

# for live plotting
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

def animate(z):
  global i
  global entrada
  global saida
  global sinal
  global resposta
  global end
  try:
    # escreve no PWM
    entrada.write(sinal[i]/5)
    print("valor esperado:",sinal[i])
    # lê com a porta analogica
    aux = saida.read()
    if(aux != None):
      # salva no vetor resultado
      resposta[i] = float(aux)*5
      print("Valor lido:",resposta[i])
    i+=1
    # adiciona valor lido ao arquivo
    ax1.clear()
    ax1.plot(x[0:i], sinal[0:i])
    ax2.clear()
    ax2.plot(x[0:i], resposta[0:i])
    # plt.show()
  except IndexError as error:
    # Output expected IndexErrors.
    end = time.time()
    return 1
  except Exception as exception:
    # Output unexpected Exceptions.
    Logging.log_exception(exception, False)
    return -1


print("Tempo total para executar as medições:",len(sinal)/freq)

# configuration
board = pyfirmata.Arduino('COM8')
entrada = board.get_pin('d:3:p')
saida = board.get_pin('a:0:i')
it = pyfirmata.util.Iterator(board)
it.start()
saida.enable_reporting()

# main
#vetor de resposta
resposta = 0*np.copy(sinal)
# espera as configurações surtirem efeito
time.sleep(0.5)
#live plotting
i = 0
# ani = animation.FuncAnimation(fig, animate, interval=(1/freq-0.1))
ani = animation.FuncAnimation(fig, animate, interval=20)
ini = time.time()
end = time.time()
plt.show()
# registra o tempo de inicio
with open('exemplo.txt','w') as f:
  for i in range(len(sinal)):
    f.write(str(sinal[i])+","+str(resposta[i])+"\n")
# # gera delay para esperar pelo período de amostragem
# time.sleep(1/freq-0.001)
print("tempo:",end-ini)
print("frequencia real:",len(sinal)/(end-ini))
# print("media:",np.mean(resposta))
board.exit()