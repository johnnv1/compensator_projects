# -*- coding: utf-8 -*-
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
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from loguru import logger
import pandas as pd

#-------------------------------#-------------------------------#-------------------------------#-------------------------------
### INICIO MUDANÇAS PERMITIDAS ###
#-------------------------------
# Configuração do arduino
"""
    x:n:t -> ordem de configuração dos pinos sendo:
        x - a letra referente ao pino
        n - numero do pino
        t - tipo que sera utilizado o pino
            p - PWM
            i - input
            o - output
"""
serialPort      = '/dev/ttyACM0'                                        # Porta que o arduino esta conectada
outPin          = 'd:9:p'                                               # Pino de escrita PWM
inPin           = 'a:0:i'                                               # Pino utilizado para ler
#-------------------------------
# frequência de amostragem
freq            = 10                                                    # Em amostras por seg (Hz)

#-------------------------------
# Numero total de amostras
N               = 4000                                                 # Total de amostras

#-------------------------------
# vetor de entrada (yr)
qtdTrocas       = 100                                                     # Quantas vezes o sinal vai trocar de nivel
sizeStep        = 20                                                    # Calcula o tamanho das janelas

#-------------------------------
# dados para salvar imagem
nomeFile        = datetime.now().strftime('%Y%m%d-%H:%M:%S')
dpiImage        = 100                                                   # Dpi da imagem
srcImage        = './../../Dados-de-leitura/gerados com python/'+nomeFile+'-Fs'+str(freq)+'-N'+str(N)+'-Nv'+str(qtdTrocas)+'.svg'    # Endereço e nome da imagem a ser salva, se setar como None não salva
#srcImage        = None
formatImage     = "svg"                                                 # Tipo de imagem a ser salva
width           = 4000                                                  # Largura em px (pixels) da imagem salva
height          = 3000                                                  # Altura em px (pixels) da imagem salva

#-------------------------------
# dados para salvar csv dos dados
srcFile             = './../../Dados-de-leitura/gerados com python/'+nomeFile+'-Fs'+str(freq)+'-N'+str(N)+'-Nv'+str(qtdTrocas)+'.csv'# Endereço e nome do csv a ser salva, se setar como None não salva
#srcFile              = None             # None

#-------------------------------
# Valores do arduino
maxValue        = 5                                                     # O arduino só aguenta ler/escrever até 5V
minValue        = 0                                                     # O arduino só aguenta ler/escrever a partir de 0V

#-------------------------------
# Valores do arduino
erroAcc         = 1.15                                                  # quantas vezes é aceito que a frequencia real seja superior a desejada

### FIM MUDANÇAS PERMITIDAS ###
#-------------------------------#-------------------------------#-------------------------------#-------------------------------
# Configurando DEBUG
debugOn             = False
#-------------------------------#-------------------------------#-------------------------------#-------------------------------
# Funções
def signalStep(qtdNivel=5, T=10, N=100, maxValue=5, minValue=0):
    out             = np.zeros(T)
    listMag         = np.random.rand(qtdNivel)
    contChange      = 0
    for x in range(0,int(N/qtdNivel),2*T):
        for amplitude in listMag:
            out         = np.append(out,amplitude*np.ones(T))
            out         = np.append(out,np.zeros(T))
            contChange += 2
            if len(out) >= N:
                break
        if len(out) >= N:
                break
    out             = maxValue * (out[:N]-min(out[:N]))/(max(out[:N])-min(out[:N]))
    return out, contChange


#-------------------------------#-------------------------------#-------------------------------#-------------------------------
# Configuração do arduino
logger.info(f"Configurando conexão com o arduino...")
board               = pyfirmata.Arduino(serialPort)
pwmPin              = board.get_pin(outPin)
readPin             = board.get_pin(inPin)
it                  = pyfirmata.util.Iterator(board)
it.start()
readPin.enable_reporting()
time.sleep(0.5) # espera as configurações surtirem efeito

# Monta o vetor de saida (y) zerado, o de erro e de controle também
logger.info(f"Inicializando vetoros utilizados...")
yr, qtdTrocas       = signalStep(qtdNivel=qtdTrocas, T=sizeStep, N=N, maxValue=maxValue, minValue=minValue) #valor de referencia
y                   = np.zeros(len(yr))                                 # vetor de saida
e                   = np.zeros(len(yr))                                 # vetor de erro

#--**----**----**----**----**----**----**----**----**----**--
# Normaliza os dados de entrada 
yr                  = yr/maxValue

# Loop de operações com o arduino
logger.info(f"Tempo total estimado para executar as medições: {len(yr)/freq}")

t_ini               = time.time()                                       # registra o tempo de inicio
contLevel           = 0                                                 # Inicia o contador de leveis atingidos do yr
for i in range(2,len(yr)):
  t_ini_loop      = time.time()                                       # registra horario de inicio da interação
  #------------------------------
  aux             = readPin.read()                                    # lê com a porta analogica
  if(aux != None):
    y[i]        = float(aux)                                        # salva no vetor resultado
  #------------------------------
  e[i]            = yr[i] - y[i]                                      # calcula o erro
  #------------------------------
  # garante que o sinal estara entre os valores acc pelo arduino
  if(yr[i] > 1):
      yr[i] = 1
  elif(yr[i] < minValue):
      yr[i] = minValue
  #------------------------------
  pwmPin.write(yr[i])                                                 # escreve no PWM
  #------------------------------
  if debugOn:
    logger.debug(f"{i}:In: {y[i]*maxValue}")
    logger.debug(f"{i}:yr: {yr[i]*maxValue}")
  else:
    if(i > contLevel):
      contLevel += sizeStep
      logger.info(f"Já foram realizados {contLevel/sizeStep}/{qtdTrocas} trocas de niveis!")
  #------------------------------
  try:
      time.sleep((1/freq)-(time.time() - t_ini_loop))                     # gera delay para esperar pelo período de amostragem
  except:
      pass
pwmPin.write(0)                                                         # Desliga o motor
t_end               = time.time()                                       # registra o tempo de término
#--**----**----**----**----**----**----**----**----**----**--
board.exit()                                                            # Encerra conexão com o arduino


# Exibe informações
logger.info(f"Tempo total gasto para executar as medições: {t_end-t_ini}")
logger.info(f"frequencia real: {len(yr)/(t_end-t_ini)}")
if len(yr)/(t_end-t_ini) > erroAcc * freq:
    logger.warning(f"frequencia real {len(yr)/(t_end-t_ini)} está superioa a {erroAcc} vezes acima da desejada {freq}")
    logger.warning(f"Encerrando execução")
    exit()

# Monta dados de saida
yr                  = yr.astype(np.float64) * maxValue
y                   = y.astype(np.float64) * maxValue
e                   = e.astype(np.float64) * maxValue
logger.info(f"Montando data frame")
data                = pd.DataFrame()
data.loc[:, 'yr']   = yr
data.loc[:, 'y']    = y
data.loc[0, 'fs']   = freq

if srcFile != None:
    logger.info(f"Salvando csv de dados...")
    data.to_csv(srcFile, index=False)

# Monta o grafico de resultado
x                   = [i for i,a in enumerate(yr)]                   # Monta eixo x dos graficos

sizeImage           = (width/dpiImage,height/dpiImage)
fig, axs            = plt.subplots(2, sharex=True, figsize=sizeImage, dpi=dpiImage)
axs[0].plot(x,y , color='red', linewidth=4,label='y')
axs[0].plot(x,yr,'--', color='blue', linewidth=2, label='yr')
axs[0].set_ylim(-0.5,5.5)
axs[0].set_title('Dados Lidos - y(k)', fontsize=35)
axs[0].legend(loc="upper right", fontsize=25)
axs[0].grid(color='gray')

axs[1].plot(x,e, color='black', linewidth=4)
axs[1].set_ylim(-5.5,5.5)
axs[1].set_title('Erro - e(k)', fontsize=35)
axs[1].grid(color='gray')

plt.suptitle("G(s) - Planta em MA", fontsize=45)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
for ax in axs.flat:
    ax.set_ylabel('Voltagem (V)', fontsize=30)
    ax.set_xlabel('Amostras (k)', fontsize=30)
for ax in axs.flat:
    ax.label_outer()

if srcImage != None:
    logger.info(f"Salvando grafico...")
    plt.savefig(srcImage, format=formatImage)

logger.info(f"Encerrando execução!")
