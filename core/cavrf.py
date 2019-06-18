# -*- coding: utf-8 -*-

from misc import *

def cavrf(e_esp, Kp_MA, G_MA, MFd, MFseg):
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

    