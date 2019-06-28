# -*- coding: utf-8 -*-
from core import *

#   Examples of use
# Catlr   = catlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, Kp_MA, gaindc=63.08/47.93, pos_polo_c=-0.01)
# Cavatlr = cavatlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, Kp_MA, gaindc=63.08/47.93)
# Cavlr   = cavlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, Kp_MA)


# Especificações dos sinais de entrada para simulação
Nit        = 200                    # Número de iterações
t          = range(Nit)             # Tempo
ramp       = t                      # Rampa
step       = np.ones(Nit)           # Degrau
dist_p     = np.concatenate((np.zeros(round(Nit/2)),np.ones(round(Nit/2))), axis=0)
med        = 0;
stdn       = 0.05;
dist_n     = med + stdn * np.random.rand(Nit);


#----------------------------------------------------------------------------------------------------------------------------
# Controle para a planta gerada com o PRBS (fs=10) de primeira ordem
    # G(z^-1) = (0.1931 * z^-1) /( 1 - 0.8468 * z^-1)
    # G(s) = 2.096 / (s+1.663)

# Especificações de projeto
Kp_MA           = 2.096
Numerador       = Kp_MA
Denominador     = np.array([1, 1.663], dtype=float)

ts_esp          = 3                        # tempo de estabelecimento
Mp_esp          = 10                         # overshoot esperado em porcentagem
Mp_folga        = 5                          # folga dada ao Mp, pq da aproximação de compensador para 2ª ordem
e_esp           = 0.01                        # margem de fase de segurança, variavel

MFd             = 50
MFseg           = 5

tau_MA          = 1/1.663
tauMF_esp       = ts_esp/4                   # tau em MF
p               = 10

# Planta
G_MA = tf(Numerador, Denominador)                          # FT em MA, C = 1
print(f"Gma={G_MA}")
    # Salva e exibe os polos e zeros da planta
polos_MA = pole(G_MA)
zeros_MA = zero(G_MA)
print(f"Polos de G(s) -> {polos_MA}")
print(f"Zeros de G(s) -> {zeros_MA}")

    # Calcula o ganho em MA, s -> 0
if 0 in polos_MA:
    gaindc_MA = np.inf
elif 0 in zeros_MA:
    gaindc_MA = 0
else:
    gaindc_MA = (Kp_MA*np.prod(-1*zeros_MA)) / (np.prod(-1*polos_MA))

    # Salva os dados de resposta em frequencia
#[mag_MA,phase_MA,wout_MA] = bode(G_MA,)

#testControl(G_MA, 1, step, ramp, t, dist_p, dist_n)

# Controladores
    # Controlador em avanço por lugar das raizes
#Cavlr   = cavlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, zeros_MA, Kp_MA)
#testControl(G_MA, Cavlr, step, ramp, t, dist_p, dist_n)

    # Controlador em atraso por lugar das raizes
Catlr   = catlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, zeros_MA, Kp_MA, gaindc_MA, pos_polo_c=0.03)
testControl(G_MA, Catlr, step, ramp, t, dist_p, dist_n)

    # Controlador em avanço-atraso por lugar das raizes
#Cavatlr = cavatlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, Kp_MA, gaindc_MA, pos_polo_c=0.02)
#testControl(G_MA, Cavatlr, step, ramp, t, dist_p, dist_n, stepInfoB=False)

    # Controlador em avanço por resposta em frequencia
#Cavrf = cavrf(e_esp, Kp_MA, G_MA, MFd, MFseg, mag_MA, wout_MA)
#testControl(G_MA, Cavrf, step, ramp, t, dist_p, dist_n)

    # Controlador em atraso por resposta em frequencia
#Catrf = catrf(e_esp, Kp_MA, G_MA, MFd, MFseg, phase_MA, wout_MA)
#testControl(G_MA, Catrf, step, ramp, t, dist_p, dist_n)

    # Controlador em avanço-atraso por resposta em frequencia
    
#----------------------------------------------------------------------------------------------------------------------------
# Controle para a planta gerada com o PRBS (fs=500) de primeira ordem
    # G(z^-1) = (0.1203 * z^-1) /( 1 - 0.9086 * z^-1)
    # G(s) = 63.08 / (s+47.93)


#----------------------------------------------------------------------------------------------------------------------------
# Controle para a planta gerada com o pulso (fs=500) de primeira ordem
    # G(z^-1) = (0.157 * z^-1) /( 1 - 0.8116 * z^-1)
    # G(s) = 86.9782 / (s+104.4)


#----------------------------------------------------------------------------------------------------------------------------
# Controle para a planta gerada com a escada (fs=500) de primeira ordem
    # G(z^-1) = (0.08944 * z^-1) /( 1 - 0.9065 * z^-1)
    # G(s) = 46.95 / (s+49.08)


