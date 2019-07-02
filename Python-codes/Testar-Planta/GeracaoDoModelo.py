# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
#-------------------------------#-------------------------------#-------------------------------#-------------------------------
### INICIO MUDANÇAS PERMITIDAS ###
#-------------------------------
# caminho do arquivo a ser lido com os dados
srcFile             = './../../Dados-de-leitura/gerados com python/20190701-23:37:34-Fs10-N4000-Nv100.csv'# Endereço e nome do csv a ser salva, se setar como None não salva


### FIM MUDANÇAS PERMITIDAS ###
#-------------------------------#-------------------------------#-------------------------------#-------------------------------
# Configurando DEBUG
debugOn             = False

#-------------------------------
# carregando dados
data                = pd.read_csv(srcFile)

freq                = data.loc[0,"fs"]              # pega a frequencia de amostragem utilizada
y                   = data.loc[:,"y"].values        # pega a saida da planta
yr                  = data.loc[:,"yr"].values       # pega p sinal de entrada


#-------------------------------
# https://en.wikipedia.org/wiki/Linear_least_squares#The_general_problem
# https://coredump.pt/questions/44587923/least-squares-method-in-practice
#-------------------------------
# calculo do modelo de primeira ordem pelo método dos minimos quadrados

phi                 = np.column_stack((-yr[:-1],y[:-1]))

MTM_inv             = np.linalg.inv(np.dot(phi.T, phi))
MTy                 = np.column_stack(np.dot(phi.T, yr[1:]))

theta               = np.dot(MTM_inv, MTy.T)

a1                  = np.float64(theta[0])
b0                  = np.float64(theta[1])

print(f"a1 = {a1}")
print(f"b0 = {b0}")


#-------------------------------
# calculo do modelo de segunda ordem pelo método dos minimos quadrados
# TEM QUE VERIFICAR SE ESTA CERTO O phi e a sequencia da resposta do theta
# phi                 = np.column_stack((-yr[1:-1], -yr[:-2],y[1:-1],y[:-2]))

# MTM_inv             = np.linalg.inv(np.dot(phi.T, phi))
# MTy                 = np.column_stack(np.dot(phi.T, yr[2:]))

# theta               = np.dot(MTM_inv, MTy.T)


# a1                  = np.float64(theta[0])
# a2                  = np.float64(theta[1])
# b0                  = np.float64(theta[2])
# b1                  = np.float64(theta[3])

# print(f"a1 = {a1}")
# print(f"a2 = {a2}")
# print(f"b0 = {b0}")
# print(f"b1 = {b1}")