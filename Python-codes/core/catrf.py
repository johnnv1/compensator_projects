# -*- coding: utf-8 -*-

from .misc import *

def catrf(e_esp, Kp_MA, G_MA, MFd, MFseg, phase_MA, wout_MA):
    """
        e_esp   : erro esperado em regime permanente
        Kp_MA   : Ganho em Malha Aberta da planta
        MFd     : Margem de Fase desejada
        MFseg   : Margem de Fase de segurança
        phase_MA: resposta do bode (uma lista) das fase da plata em Malha Aberta
        wout_MA : resposta do bode (uma lista) das frequencias da planta em Malha Aberta
    """
    # Determina o ganho do controlador
    Kc              = get_kc_rf(e_esp, Kp_MA)

    print(f"Kc = {Kc}")
    print("*********************************************\n")


    # Verifica o comportamento do sistema apenas com o ganho do controlador
    Cat             = Kc
    Gma_Cat         = G_MA*Cat
    bode(G_MA)
    [mag_Cat,phase_Cat,wout_Cat]    = bode(Gma_Cat)
    print("*********************************************\n")
    

    # Determinar a localização da resposta em frequencia (RF) do compensador, Wcd
    Wcd             = get_Wcd(phase_MA, MFd, MFseg, wout_MA)
    print(f"Wcd = {Wcd}")
    print("*********************************************\n")

    
    # Determina o valor a do compensador
    a               = get_a_at(mag_Cat, wout_MA, Wcd)
    print(f"a = {a}")
    print("*********************************************\n")


    # Determinar do parametro T do compensador
    T               = get_T_at(Wcd)
    print(f"T = {T}")
    print("*********************************************\n")

    
    # Monta controlador com os parametros determinados
    numC    = np.array([T, 1], dtype=float)
    denC    = np.array([T*a, 1], dtype=float)
    C       = tf(float(Kc)*numC, denC)           # Controlador em atraso
    print(f"Controlador em atraso = Kc * (T*s+1)/(T*a*s+1) = ")
    print(f"\t= {Kc} *  ({round(T,2)}*s+1)/({round(T,2)}*{round(a,2)}*s+1) = \t{C}")


    # Plota os locais dos polos e zeros do controlador
    #plot_c(polesDominant, zero_c, polo_c)


    # Retorna o controlador
    return C

    
