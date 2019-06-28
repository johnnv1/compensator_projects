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
# dados para salvar imagem
dpiImage        = 100                                                   # Dpi da imagem
srcImage        = './../../Controles/PRBS-FS10/ord1/real/graph-cavlr.svg'    # Endereço e nome da imagem a ser salva, se setar como None não salva
#srcImage        = None
formatImage     = "svg"                                                 # Tipo de imagem a ser salva
width           = 1920                                                  # Largura em px (pixels) da imagem salva
height          = 1080                                                  # Altura em px (pixels) da imagem salva

#-------------------------------
# dados para salvar csv dos dados
srcFile             = './../../Controles/PRBS-FS10/ord1/real/data-cavlr.csv'# Endereço e nome do csv a ser salva, se setar como None não salva
#srcFile             # None

#-------------------------------
# frequência de amostragem
freq            = 100                                                    # Em amostras por seg (Hz)

#-------------------------------
# Numero total de amostras
N               = 400                                                   # Total de amostras

#-------------------------------
# vetor de entrada (yr)
qtdTrocas       = 8                                                     # Quantas vezes o sinal vai trocar de nivel
sizeStep        = int(N/qtdTrocas)                                      # Calcula o tamanho das janelas

# Monta o vetor de entrada yr como um conjunto de degraus
yr              = np.zeros(sizeStep)
yr              = np.append(yr,4*np.ones(sizeStep))
yr              = np.append(yr, np.zeros(sizeStep))
yr              = np.append(yr,5*np.ones(sizeStep))
yr              = np.append(yr,1*np.ones(sizeStep))
yr              = np.append(yr,2*np.ones(sizeStep))
yr              = np.append(yr,0*np.ones(sizeStep))
yr              = np.append(yr,3*np.ones(sizeStep))

#-------------------------------
# Valores do arduino
maxValue        = 5                                                     # O arduino só aguenta ler/escrever até 5V
minValue        = 0                                                     # O arduino só aguenta ler/escrever a partir de 0V
#-------------------------------
# Valores do arduino
erroAcc         = 1.15                                                  # quantas vezes é aceito que a frequencia real seja superior a desejada

#-------------------------------
# coeficientes dos controladores
#*******    Cavlr 1ª ord    **********  Controlador em avanço por lugar das raizes para modelo de primeira ordem
controlName = "Controlador avanço - LR"
b0 = 0
b1 = 0
b2 = 0

a1 = 0
a2 = 0
#****************
#*******    Cavlr 2ª ord    **********  Controlador em avanço por lugar das raizes para modelo de segunda ordem
#controlName = "Controlador avanço - LR"

#****************
#*******    Cavrf 1ª ord    **********  Controlador em avanço por resposta em frequencia para modelo de primeira ordem
#controlName = "Controlador avanço - RF"

#****************
#*******    Cavrf 2ª ord    **********  Controlador em avanço por resposta em frequencia para modelo de segunda ordem
#controlName = "Controlador avanço - RF"

#****************
#*******    Catlr 1ª ord    **********  Controlador em atraso por lugar das raizes para modelo de primeira ordem
#controlName = "Controlador atraso - LR"

#****************
#*******    Catlr 2ª ord    **********  Controlador em atraso por lugar das raizes para modelo de segunda ordem
#controlName = "Controlador atraso - LR"

#****************
#*******    Catrf 1ª ord    **********  Controlador em atraso por resposta em frequencia para modelo de primeira ordem
#controlName = "Controlador atraso - RF"

#****************
#*******    Catrf 2ª ord    **********  Controlador em atraso por resposta em frequencia para modelo de segunda ordem
#controlName = "Controlador atraso - RF"

#****************
#*******   Cavatlr 1ª ord   **********  Controlador em avanço-atraso por lugar das raizes para modelo de primeira ordem
#controlName = "Controlador avanço-atraso - LR"

#****************
#*******   Cavatlr 1ª ord   **********  Controlador em avanço-atraso por lugar das raizes para modelo de segunda ordem
#controlName = "Controlador avanço-atraso - LR"

#****************
#*******   Cavatrf 1ª ord   **********  Controlador em avanço-atraso por resposta em frequencia para modelo de primeira ordem
#controlName = "Controlador avanço-atraso - RF"

#****************
#*******   Cavatrf 1ª ord   **********  Controlador em avanço-atraso por resposta em frequencia para modelo de segunda ordem
#controlName = "Controlador avanço-atraso - RF"


### FIM MUDANÇAS PERMITIDAS ###
#-------------------------------#-------------------------------#-------------------------------#-------------------------------
# Configurando DEBUG
debugOn             = False

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
y                   = np.zeros(len(yr))                                 # vetor de saida
e                   = np.zeros(len(yr))                                 # vetor de erro
u                   = np.zeros(len(yr))                                 # vetor de controle

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
    # malha de controle
    #u[i] = b0* e[i] + b1*e[i-1] + b2*e[i-2] - a1*u[i-1] - a2*u[i-2]
    u[i] = yr[i]
        # garante que o sinal estara entre os valores acc pelo arduino
    if(u[i] > 1):
        u[i] = 1
    elif(u[i] < minValue):
        u[i] = minValue
    #------------------------------
    pwmPin.write(u[i])                                                 # escreve no PWM
    #------------------------------
    if debugOn:
        logger.debug(f"{i}:In: {y[i]*maxValue}")
        logger.debug(f"{i}:PWM: {u[i]*maxValue}")
        logger.debug(f"{i}:yr: {yr[i]*maxValue}")
    else:
        if(i > contLevel):
            contLevel += sizeStep
            logger.info(f"Já foram realizados {contLevel/sizeStep}/{qtdTrocas} trocas de niveis!")
    #------------------------------
    time.sleep((1/freq)-(time.time() - t_ini_loop))                     # gera delay para esperar pelo período de amostragem

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
u                   = u.astype(np.float64) * maxValue
y                   = y.astype(np.float64) * maxValue
e                   = e.astype(np.float64) * maxValue
logger.info(f"Gravando dados no csv")
data                = pd.DataFrame()
data.loc[:, 'yr']   = yr
data.loc[:, 'u']    = u
data.loc[:, 'y']    = y
data.loc[0, 'fs']   = freq

#data.write_csv()

# Monta o grafico de resultado
x                   = [i for i,a in enumerate(yr)]                   # Monta eixo x dos graficos

sizeImage           = (width/dpiImage,height/dpiImage)
fig, axs            = plt.subplots(4, sharex=True, figsize=sizeImage, dpi=dpiImage)
axs[0].plot(x,yr, color='blue', linewidth=4)
axs[0].set_ylim(-0.5,5.5)
axs[0].set_title('Referencia - yr(k)')
axs[0].grid(color='gray')

axs[1].plot(x,u,'--', color='green', linewidth=4)
axs[1].set_ylim(-0.5,5.5)
axs[1].set_title('Saída controlador - u(k)')
axs[1].grid(color='gray')

axs[2].plot(x,y , color='red', linewidth=4,label='y')
axs[2].plot(x,yr,'--', color='blue', linewidth=2, label='yr')
axs[2].set_ylim(-0.5,5.5)
axs[2].set_title('Dados Lidos - y(k)')
axs[2].legend(loc="upper right")
axs[2].grid(color='gray')

axs[3].plot(x,e, color='black', linewidth=4)
axs[3].set_ylim(-5.5,5.5)
axs[3].set_title('Erro - e(k)')
axs[3].grid(color='gray')

plt.suptitle(controlName, fontsize=22)
for ax in axs.flat:
    ax.set(xlabel='Amostras (k)', ylabel='Voltagem (V)')
for ax in axs.flat:
    ax.label_outer()

if srcImage != None:
    logger.info(f"Salvando grafico...")
    plt.savefig(srcImage, format=formatImage)

plt.show()

logger.info(f"Encerrando execução!")
