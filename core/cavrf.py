# -*- coding: utf-8 -*-

from misc import *

def cavrf(e_esp, Kp_MA, G_MA, MFd, MFseg, mag_MA):
    """
        e_esp : erro esperado em regime permanente
        Kp_MA : Ganho em Malha Aberta da planta
        MFd   : Margem de Fase desejada
        MFseg : Margem de Fase de segurança
        mag_MA: resposta do bode (uma lista) das magnitudes da planta em Malha Aberta
    """
    # Determina o ganho do controlador
    Kc              = get_kc_rf(e_esp, Kp_MA)

    print(f"Kc = {Kc}")
    print("*********************************************\n")


    # Verifica o comportamento do sistema apenas com o ganho do controlador
    Cav                  = Kc
    Gma_Cav              = G_MA*Cav
    bode(G_MA)
    bode(Gma_Cav)

    [gm, pm, wcg, wcp]   = margin(Gma_Cav)             # Verificando a MF e MG do sistema, MF= margem de fase, MG = margem de ganho
    MFkc                 = pm;                         # margem de fase após o Kc
    phiMax               = MFd - MFkc + MFseg          # em graus

    print(f"φ_max = {phiMax}")
    print("*********************************************\n")


    # Determina o valor a do compensador
    a               = get_a_av(phiMax, deg=True)
    print(f"a = {a}")
    print("*********************************************\n")

    
    # Determinar a localização da resposnta em frequencia (RF) do compensador, Wm
    C_jWm, Wm       = get_Wm(Kc,a,mag_MA)
    print(f"C(jWm) = {C_jWm}")
    print(f"Wm = {Wm}")
    print("*********************************************\n")

    
    # Determinar do parametro T do compensador
    T               = get_T(a, Wm)
    print(f"T = {T}")
    print("*********************************************\n")

    
    # Monta controlador com os parametros determinados"""
    numC            = np.array([T, 1], dtype=float)
    denC            = np.array([T*a, 1], dtype=float)
    C               = tf(float(Kc)*numC, denC)           # Controlador m avanço
    print(f"Controlador em avanço = Kc * (T*s+1)/(T*a*s+1) = ")
    print(f"\t= {Kc} *  ({round(T,2)}*s+1)/({round(T,2)}*{round(a,2)}*s+1) = \t{C}")


    # Plota os locais dos polos e zeros do controlador
    plot_c(polesDominant, zero_c, polo_c)


    # Retorna o controlador
    return C
    