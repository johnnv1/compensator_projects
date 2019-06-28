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
# Controlador desejado
#controlUse      = "sc"                                                  # Sem controlador
#controlUse      = "cavlr1"                                              #Cavlr 1ª ord    **********  Controlador em avanço por lugar das raizes para modelo de primeira ordem
#controlUse      = "catlr1"                                              #Catlr 1ª ord    **********  Controlador em atraso por lugar das raizes para modelo de primeira ordem
#controlUse      = "cavatlr1"                                            #Cavatlr 1ª ord   **********  Controlador em avanço-atraso por lugar das raizes para modelo de primeira ordem
#controlUse      = "cavrf1"                                              #Cavrf 1ª ord    **********  Controlador em avanço por resposta em frequencia para modelo de primeira ordem
#controlUse      = "catrf1"                                              #Catrf 1ª ord    **********  Controlador em atraso por resposta em frequencia para modelo de primeira ordem
#controlUse      = "cavlr2"                                              #Cavlr 2ª ord    **********  Controlador em avanço por lugar das raizes para modelo de segunda ordem
#controlUse      = "catlr2"                                              #Catlr 2ª ord    **********  Controlador em atraso por lugar das raizes para modelo de segunda ordem
#controlUse      = "cavatlr2"                                            #Cavatlr 2ª ord   **********  Controlador em avanço-atraso por lugar das raizes para modelo de segunda ordem
#controlUse      = "cavrf2"                                              #Cavrf 2ª ord    **********  Controlador em avanço por resposta em frequencia para modelo de segunda ordem    
controlUse      = "catrf2"                                              #Catrf 2ª ord    **********  Controlador em atraso por resposta em frequencia para modelo de segunda ordem
         


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
srcImage        = './../../Controles/PRBS-FS10/ord2/real/graph-'+controlUse+'.svg'    # Endereço e nome da imagem a ser salva, se setar como None não salva
#srcImage        = None
formatImage     = "svg"                                                 # Tipo de imagem a ser salva
width           = 1920                                                  # Largura em px (pixels) da imagem salva
height          = 1080                                                  # Altura em px (pixels) da imagem salva

#-------------------------------
# dados para salvar csv dos dados
srcFile             = './../../Controles/PRBS-FS10/ord2/real/data-'+controlUse+'.csv'# Endereço e nome do csv a ser salva, se setar como None não salva
#srcFile             # None

#-------------------------------
# frequência de amostragem
freq            = 10                                                    # Em amostras por seg (Hz)

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
if controlUse == "sc":
    controlName = "Sem controlador"
elif controlUse == "cavlr1":
    #*******    Cavlr 1ª ord    **********  Controlador em avanço por lugar das raizes para modelo de primeira ordem
    controlName = "Controlador avanço - LR"
    # Kc= Kc
    # b0 = 2.244
    # b1 = -1.964
    # b2 = 0
    # a1 = -0.4845
    # a2 = 0
    # Kc= Kc  # fs = 100
    # b0 = 2.758
    # b1 = -2.722
    # b2 = 0
    # a1 = -0.9329
    # a2 = 0
    # Kc= Kc e zero em 3/4*sigma
    b0 = 1.13
    b1 = -1.022
    b2 = 0
    a1 = -0.6931
    a2 = 0
    # Kc= 5*Kc
    #b0 = 11.23
    #b1 = -9.823
    #b2 = 0
    #a1 = -0.4845
    #a2 = 0
    # Kc= 10*Kc
    # b0 = 22.44
    # b1 = -19.64
    # b2 = 0
    # a1 = -0.4845
    # a2 = 0
    # Kc= 10*Kc   # fs = 100
    # b0 = 27.58
    # b1 = -27.22
    # b2 = 0
    # a1 = -0.9329
    # a2 = 0
    # Kc= 10*Kc   # zero = 3/4*sigma
    # b0 = 11.3
    # b1 = -10.22
    # b2 = 0
    # a1 = -0.6931
    # a2 = 0
    # Kc= 10*Kc   # zero = *sigma/3
    # b0 = 4.89
    # b1 = -4.652
    # b2 = 0
    # a1 = -0.8415
    # a2 = 0
elif controlUse == "cavlr2":
    #*******    Cavlr 2ª ord    **********  Controlador em avanço por lugar das raizes para modelo de segunda ordem
    controlName = "Controlador avanço - LR"
    # # Colocando zero em sigma *2
    # b0 = 3.882
    # b1 = -1.664
    # b2 = 0
    # a1 = -0.0007006
    # a2 = 0
    # Colocando zero em sigma *3
    # b0 = 4.05
    # b1 = -1.012
    # b2 = 0
    # a1 = -0.02119
    # a2 = 0
    # Colocando zero em sigma *4.5
    b0 = 4.061
    b1 = -0.214
    b2 = 0
    a1 = 0.0184
    a2 = 0
elif controlUse == "cavrf1":
    #*******    Cavrf 1ª ord    **********  Controlador em avanço por resposta em frequencia para modelo de primeira ordem
    controlName = "Controlador avanço - RF"
    # b0 = 31.73
    # b1 = 20.49
    # b2 = 0
    # a1 = 0.09445
    # a2 = 0
    # Kc = Kc /2 -> ficou mais instavel
    # b0 = 12.56
    # b1 = 5.048
    # b2 = 0
    # a1 = -0.2618
    # a2 = 0
    # trocando o erro esperado para 0.1
    # b0 = 1.118
    # b1 = -0.4326
    # b2 = 0
    # a1 = -0.8546
    # a2 = 0
    # trocando o erro esperado para 0.03
    b0 = 10.7
    b1 = -5.587
    b2 = 0
    a1 = -0.6781
    a2 = 0
elif controlUse == "cavrf2":
    #*******    Cavrf 2ª ord    **********  Controlador em avanço por resposta em frequencia para modelo de segunda ordem
    controlName = "Controlador avanço - RF"
    b0 = 0.4338
    b1 = -0.1238
    b2 = 0
    a1 = -0.9367
    a2 = 0
elif controlUse == "catlr1":
    #*******    Catlr 1ª ord    **********  Controlador em atraso por lugar das raizes para modelo de primeira ordem
    controlName = "Controlador atraso - LR"
    b0 = 0.825
    b1 = -0.651
    b2 = 0
    a1 = -0.997
    a2 = 0
elif controlUse == "catlr2":
    #*******    Catlr 2ª ord    **********  Controlador em atraso por lugar das raizes para modelo de segunda ordem
    controlName = "Controlador atraso - LR"
    b0 = 4.752
    b1 = -3.447
    b2 = 0
    a1 = -0.996
    a2 = 0
elif controlUse == "catrf1":
    #*******    Catrf 1ª ord    **********  Controlador em atraso por resposta em frequencia para modelo de primeira ordem
    # b0 = 29.22
    # b1 = -15.25
    # b2 = 0
    # a1 = -0.7072
    # a2 = 0
    # alterando o erro esperado para 0.1
    b0 = 1.086
    b1 = -0.5667
    b2 = 0
    a1 = -0.8912
    a2 = 0
    controlName = "Controlador atraso - RF"
elif controlUse == "catrf2":
    #*******    Catrf 2ª ord    **********  Controlador em atraso por resposta em frequencia para modelo de segunda ordem
    controlName = "Controlador atraso - RF"
    b0 = 13.91
    b1 = 7.194
    b2 = 0
    a1 = -0.3594
    a2 = 0
elif controlUse == "cavatlr1":
    #*******   Cavatlr 1ª ord   **********  Controlador em avanço-atraso por lugar das raizes para modelo de primeira ordem
    controlName = "Controlador avanço-atraso - LR"
    # b0 = 2.823
    # b1 = -4.129
    # b2 = 1.452
    # a1 = -1.481
    # a2 = 0.483
    # Colocando o zero do controlador de avanço em sigma/2
    # b0 = 1.133
    # b1 = -1.29
    # b2 = 0.2146
    # a1 = -1.79
    # a2 = 0.7911
    # Colocando o zero do controlador de avanço em sigma*3/4
    b0 = 1.583
    b1 = -2.105
    b2 = 0.6091
    a1 = -1.69
    a2 = 0.691
elif controlUse == "cavatlr2":
    #*******   Cavatlr 2ª ord   **********  Controlador em avanço-atraso por lugar das raizes para modelo de segunda ordem
    controlName = "Controlador avanço-atraso - LR"
    # colocando o zero em sigma * 4.5
    b0 = 4.355
    b1 = -4.072
    b2 = 0.2026
    a1 = -0.9776
    a2 = -0.01833
elif controlUse == "cavatrf1":
    #****************
    #*******   Cavatrf 1ª ord   **********  Controlador em avanço-atraso por resposta em frequencia para modelo de primeira ordem
    controlName = "Controlador avanço-atraso - RF"
elif controlUse == "cavatrf2":
    #****************
    #*******   Cavatrf 2ª ord   **********  Controlador em avanço-atraso por resposta em frequencia para modelo de segunda ordem
    controlName = "Controlador avanço-atraso - RF"
else: 
    controlName = "Sem controlador"

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
    if controlName != "Sem controlador":
        u[i] = b0* e[i] + b1*e[i-1] + b2*e[i-2] - a1*u[i-1] - a2*u[i-2]
    else:
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
u                   = u.astype(np.float64) * maxValue
y                   = y.astype(np.float64) * maxValue
e                   = e.astype(np.float64) * maxValue
logger.info(f"Montando data frame")
data                = pd.DataFrame()
data.loc[:, 'yr']   = yr
data.loc[:, 'u']    = u
data.loc[:, 'y']    = y
data.loc[0, 'fs']   = freq

if srcFile != None:
    logger.info(f"Salvando csv de dados...")
    data.to_csv(srcFile, index=False)

# Monta o grafico de resultado
x                   = [i for i,a in enumerate(yr)]                   # Monta eixo x dos graficos

sizeImage           = (width/dpiImage,height/dpiImage)
fig, axs            = plt.subplots(4, sharex=True, figsize=sizeImage, dpi=dpiImage)
axs[0].plot(x,yr, color='blue', linewidth=4)
axs[0].set_ylim(-0.5,5.5)
axs[0].set_title('Referencia - yr(k)', fontsize=21)
axs[0].grid(color='gray')

axs[1].plot(x,u,'--', color='green', linewidth=4)
axs[1].set_ylim(-0.5,5.5)
axs[1].set_title('Saída controlador - u(k)', fontsize=21)
axs[1].grid(color='gray')

axs[2].plot(x,y , color='red', linewidth=4,label='y')
axs[2].plot(x,yr,'--', color='blue', linewidth=2, label='yr')
axs[2].set_ylim(-0.5,5.5)
axs[2].set_title('Dados Lidos - y(k)', fontsize=21)
axs[2].legend(loc="upper right")
axs[2].grid(color='gray')

axs[3].plot(x,e, color='black', linewidth=4)
axs[3].set_ylim(-5.5,5.5)
axs[3].set_title('Erro - e(k)', fontsize=21)
axs[3].grid(color='gray')

plt.suptitle(controlName, fontsize=26)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
for ax in axs.flat:
    ax.set_ylabel('Voltagem (V)', fontsize=16)
    ax.set_xlabel('Amostras (k)', fontsize=18)
for ax in axs.flat:
    ax.label_outer()

if srcImage != None:
    logger.info(f"Salvando grafico...")
    plt.savefig(srcImage, format=formatImage)

plt.show()

logger.info(f"Encerrando execução!")
