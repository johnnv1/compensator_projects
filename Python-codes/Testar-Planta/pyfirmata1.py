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

#-------------------------------#-------------------------------#-------------------------------#-------------------------------
### INICIO MUDANÇAS PERMITIDAS ###

#-------------------------------
# dados para salvar imagem
dpiImage = 100
srcImage = '../Dados-de-leitura/ExComportamento.svg'
formatImage = "svg"
sizeImage = (1920/dpiImage,1080/dpiImage)


#-------------------------------
# vetor de entrada (V)
sinal = 4*np.ones(100)
sinal = np.append(sinal,0*np.ones(100))
sinal = np.append(sinal,5*np.ones(100))
sinal = np.append(sinal,1*np.ones(100))
sinal = np.append(sinal,2*np.ones(100))


#-------------------------------
# frequência de amostragem
freq = 10



### FIM MUDANÇAS PERMITIDAS ###
#-------------------------------#-------------------------------#-------------------------------#-------------------------------
x = [i for i,a in enumerate(sinal)]

print("Tempo total para executar as medições:",len(sinal)/freq)

# configuration
board = pyfirmata.Arduino('/dev/ttyACM0')
entrada = board.get_pin('d:9:p')
saida = board.get_pin('a:0:i')
it = pyfirmata.util.Iterator(board)
it.start()
saida.enable_reporting()

# main
#vetor de resposta
resposta = 0*np.copy(sinal)
# cria arquivo
with open('exemplo.txt','w') as f:
  pass
# espera as configurações surtirem efeito
time.sleep(0.5)
#live plotting
# registra o tempo de inicio
ini = time.time()
for i in range(len(sinal)):
  # escreve no PWM
  entrada.write(sinal[i]/5)
  print("valor esperado:",sinal[i])
  # lê com a porta analogica
  aux = saida.read()
  if(aux != None):
    # salva no vetor resultado
    resposta[i] = float(aux)*5
    print("Valor lido:",resposta[i])
  # adiciona valor lido ao arquivo
  with open('exemplo.txt','a') as f:
    f.write(str(sinal[i])+','+str(resposta[i])+'\n')
  # gera delay para esperar pelo período de amostragem
  time.sleep(1/freq-0.001)
entrada.write(0)
# registra o tempo de término
end = time.time()
# printa informações
print("tempo:",end-ini)
print("frequencia real:",len(sinal)/(end-ini))
# print("media:",np.mean(resposta))
board.exit()
# plota os gráfico

#plt.figure(figsize=sizeImage, dpi=dpiImage)
fig, axs = plt.subplots(2, sharex=True, figsize=sizeImage, dpi=dpiImage)
axs[0].plot(x,sinal, linewidth=4)
plt.ylim(-0.5,5.5)
axs[0].set_title('Dados escritos (PWM)')
axs[0].grid(color='r')

axs[1].plot(x,resposta,'--', linewidth=4)
plt.ylim(-0.5,5.5)
axs[1].set_title('Dados Lidos')
axs[1].grid(color='r')

for ax in axs.flat:
    ax.set(xlabel='Amostras', ylabel='Voltagem (V)')

for ax in axs.flat:
    ax.label_outer()
#plt.savefig(srcImage, format=formatImage)
plt.show()

