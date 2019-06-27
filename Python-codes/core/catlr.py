# -*- coding: utf-8 -*-

from .misc import *

def catlr(e_esp, Mp_esp, Mp_folga, ts_esp, polos_MA, Kp_MA, gaindc, pos_polo_c=-0.01):
    """
        e_esp       : erro esperado em regime permanente
        Mp_esp      : Overshoot máximo esperado
        Mp_folga    : Folga dada ao overshoot maximo esperado -> em casos de aproximações de plantas que não sejam de segunda ordem
        ts_esp      : Tempo de pico / tempo de subida desejado
        polos_MA    : Polos da planta em MA -> obitido pela função poles(G_MA)
        Kp_MA       : Ganho em Malha Aberta da planta
        gaindc      : Ganho da planta em MA quando s->0
        pos_polo_c  : Posição do polo do compensador desejado
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


    # Determinando polo do compensador
    polo_c          = complex(-abs(pos_polo_c), 0)
    print(f"Polo controlador -> {polo_c}")
    print("*********************************************\n")

    # Determinando zero do compensador
    #     %Kp = lim {Kc *G(s)*(s+Z_c)/(s+P_c)} quando s tende a 0
    #      (P_c * Kp)/(Kc * dcgain(G))
    zero_c          = complex(-abs(float(polo_c*(Kp /(gaindc)))), 0)
    print(f"Zero controlador -> {zero_c}")
    print("*********************************************\n")


    # Determinando ganho do compensador, Kc, usando Condição de Modulo
    Kc              = get_KcByCM(polesDominant, polos_MA, zero_c, polo_c, Kp_MA)
    print(f"Kc  = {Kc}")
    print("*********************************************\n")

    # Monta equação do controlador
    numC            = np.array([1, abs(zero_c)], dtype=float)
    denC            = np.array([1, abs(polo_c)], dtype=float)
    C               = tf(float(Kc)*numC, denC)                  # Controlador
    print(f"Controle de atraso = Kc * (s+z)/(s+p) = ")
    print(f"\t= {Kc} *  (s+z)/(s+p) = \t{C}")
    
    
    # Plota os locais dos polos e zeros do controlador
    plot_c(polesDominant, zero_c, polo_c)

    # Retorna o controlador
    return C

#if __name__ == "__main__":
#    Catlr               = catlr(e_esp=0.01, Mp_esp=10, Mp_folga=5, ts_esp=0.01, polos_MA=[-47.93], Kp_MA=63.08, gaindc=63.08/47.93, pos_polo_c=-0.01)