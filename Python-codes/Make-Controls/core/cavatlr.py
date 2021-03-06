# -*- coding: utf-8 -*-

from .misc import *

def cavatlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, zeros_MA, Kp_MA, gaindc, pos_polo_c=0.02,zeroGain=1.2):
    """
        e_esp       : erro esperado em regime permanente
        Mp_esp      : Overshoot máximo esperado
        Mp_folga    : Folga dada ao overshoot maximo esperado -> em casos de aproximações de plantas que não sejam de segunda ordem
        ts_esp      : Tempo de pico / tempo de subida desejado
        polos_MA    : Polos da planta em MA -> obitido pela função pole(G_MA)
        zeros_MA    : Polos da planta em MA -> obitido pela função zero(G_MA)
        Kp_MA       : Ganho em Malha Aberta da planta
        gaindc      : Ganho da planta em MA quando s->0
        pos_polo_c  : Posição do polo do compensador desejado
        zeroGain    : Ganho/aumento do valor do zero
    """
    # Determinando as especificações do compensador
    Kp, Kc          = get_kc_lr(e_esp, gaindc)
    psi             = get_psi(Mp_esp, Mp_folga)
    Wn              = get_wn(ts_esp, psi)
    sigma, Wd       = get_paramOrd2(psi,Wn)


    print(f"Kc = {Kc}")
    print(f"Kp = {Kp}")
    print(f"ξ  = {psi}")
    print(f"Wn = {Wn}\t rad/s")
    print(f"σ  = {sigma}")
    print(f"Wd = {Wd}")
    print("*********************************************\n")


    # Polos dominantes do sistema
    polesDominant   = get_poleDominant(sigma, Wd)
    print(f"Polo dominante 1 -> {polesDominant[0]}")
    print(f"Polo dominante 2 -> {polesDominant[1]}")
    print("*********************************************\n")


    # Determinando zero do compensador
    zero_c          = complex(-sigma, 0)
    print(f"Zero controlador av -> {zero_c}")
    print("*********************************************\n")


    # Determinando polo do compensador
        # Calculando o angulo que se encontra o polo do compensador e o polo dominante
    textSum, thetaZero, thetaZeroD, phiPolo_C = get_phiByCF(polos_MA, polesDominant, zero_c)
    print(f"Angulo entre o zero do controlador e o polo dominante = ϴ =")
    print(f"\t= {round(thetaZeroD,4)}º = {round(thetaZero,4)} rad")
    print(f"Angulo entre o polo do controlador e o polo dominante = φ{len(polos_MA)} =")
    print(f"\t= 180 - {textSum} + {round(thetaZeroD,3)} =")
    print(f"\t= {round(phiPolo_C, 4)}º = {round(np.radians(phiPolo_C),4)} rad")

        # Calculando a posição do polo do compensador
    polo_c          = complex(get_posPole(polesDominant, phiPolo_C, zero_c), 0)
    print(f"Polo controlador av -> {polo_c}")
    print("*********************************************\n")


    # Determinando ganho do compensador, Kc, usando Condição de Modulo
    Kc              = get_KcByCM(polesDominant, polos_MA,zeros_MA, zero_c, polo_c, Kp_MA)
    print(f"Kc  = {Kc}")
    print("*********************************************\n")


    # Monta equação do controlador em avanço
    numC            = np.array([1, abs(zero_c)], dtype=float)
    denC            = np.array([1, abs(polo_c)], dtype=float)
    Cav             = tf(numC, denC)                  # Controlador
    print(f"Controle de avanço = Kc * (s+z)/(s+p) = ")
    print(f"\t= {Kc} *  (s+z)/(s+p) = \t{Kc}*{Cav}")
    print("*********************************************\n")

    
    # Determina o controlador em atraso
    # %Kp = lim {s * Kc * G(s) * (s+Z_c)/(s+P_c) * C_av} quando s tende a 0
    # z> Kp * p * polo_cav / zero_cav * 1/dcgain(G(s)) * 1/Kc
    pos_zero_c      = complex(-abs(float( zeroGain * pos_polo_c * abs(polo_c) * Kp / ( gaindc * Kc * abs(zero_c) ) )), 0)
    print(f"Polo controlador at -> {pos_polo_c}")
    print(f"Zero controlador at -> {pos_zero_c}")
    print("*********************************************\n")
    Cat             = tf([1, abs(pos_zero_c)],[1, abs(pos_polo_c)])    
    print(f"Controle de atraso = Kc * (s+z)/(s+p) = ")
    print(f"\t= {Kc} *  (s+z)/(s+p) = \t{Kc}*{Cat}")
    print("*********************************************\n")


    # Monta o controlador em atraso e avanço
    C = float(Kc) * Cat * Cav
    print(f"Controle em atraso e avanço = Kc * (s+zav)/(s+pav) * (s+zat)/(s+pat) = ")
    print(f"\t= {Kc} * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \t{C}")
    print("*********************************************\n")

    # Plota os locais dos polos e zeros do controlador
    plot_cavat(polesDominant, zero_c, polo_c, complex(-0.30, 0), complex(-abs(pos_polo_c), 0))

    # Retorna o controlador
    return C

#if __name__ == "__main__":
#    Cavatlr         = cavatlr(e_esp=0.01, Mp_esp=10, Mp_folga=5, ts_esp=0.01, polos_MA=[-47.93], Kp_MA=63.08, gaindc=63.08/47.93)