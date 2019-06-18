from control.matlab import *              # Biblioteca de controle
import numpy as np                        # Biblioteca com funções matematicas
import matplotlib as mpl                  
import matplotlib.pyplot as plt           # Para realizar plotagens de funções
from sympy import *                       # Para adicionar simbolos e resolver a equações


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funções para auxiliar na avaliação dos controladores
def testControl(G_MA, C, step, ramp, t, dist_p, dist_n, stepInfoB = True):
    # Função para verificar comportamento do sistema com um controlador
    print("Malha Aberta")
    CG_MA       = C * G_MA
    print(f"C(s) * G(s) = {CG_MA}")

    print("*********************************************")
    print("Malha Fechada")
    G_MF        = feedback(CG_MA, 1)
    print(f"Gmf = {G_MF}")

    print("*********************************************")

    # Verifica as informações do sistema perante a uma entrada degrau
    if stepInfoB:
        infoG_MF     = stepinfo(G_MF)
        print(f"stepinfo: ")
        for info in infoG_MF:
            print(f"\t{info}: {infoG_MF[info]}")

    # Verifica a resposta em frequencia
    bode(G_MA)
    bode(CG_MA)
    print("Rlocus de C(s) * G(s):")
    rlocusCG_MA = rlocus(CG_MA)
    # resposta perante a entrada e root locus da planta
    y_step = lsim(G_MF, step, t)
    y_ramp = lsim(G_MF, ramp, t)
    plt.figure()                                                # create a plot figure
    plt.subplot(2, 2, 1) # (rows, columns, panel number)
    plt.plot(t, step)
    plt.plot(t, y_step[0])
    plt.legend(["R", "Gmf"])
    plt.subplot(2, 2, 2)
    plt.plot(t, ramp)
    plt.plot(t, y_ramp[0])
    plt.legend(["R", "Gmf"])
    plt.show()


    print("*********************************************")
    ymf_step2    = lsim(G_MF, dist_p, t);
    plt.figure()
    plt.plot(t, dist_p)
    plt.plot(t, ymf_step2[0])
    plt.legend(["R", "Gmf"])
    plt.ylabel("Amplitude")
    plt.show()

    # monta o sistema em MF com perturbações
    Gmf         = feedback(CG_MA, 1);
    Gd1         = feedback(G_MA, CG_MA);         # perturbação entre o controlador e a planta
    Gd2         = feedback(1, CG_MA);           # pertubação na saida da planta

    # verifica a resposta do sistema frente a um step
    yma_step    = lsim(G_MA, step, t);
    ymf_step    = lsim(G_MF, step, t);
    yd1_dist    = lsim(Gd1, dist_p, t);
    yd2_dist    = lsim(Gd2, dist_n, t);
    y_step      = ymf_step[0]+yd1_dist[0]+yd2_dist[0]


    # ----- calculo do erro
    yr = step
    er = yr-y_step

    #   u = lsim(C, er, t)
    print("*********************************************")
    plt.plot(t, step)
    plt.plot(t, dist_p)
    plt.plot(t, dist_n)
    plt.plot(t, y_step)
    plt.legend(["R","dist_p", "dist_n", "Gmf"])
    plt.ylabel("Amplitude")
    plt.show()
    plt.plot(t, er)
    plt.legend("e")
    plt.ylabel("Erro")
    plt.show()
    #   plt.plot(t, u[0])
    #   plt.legend("u")
    #   plt.ylabel("Controle")
    #   plt.show()
    plt.plot(t, dist_p)
    plt.plot(t, dist_n)
    plt.legend(["dist_p", "dist_n"])
    plt.ylabel("Amplitude")
    plt.show()
    print("*********************************************")
    ev_MF         = ramp[-1] - y_ramp[0][-1]     #erro apos ser adicionado o controlador ao
    print(f"ev(∞) = {ev_MF}")
    ep_MF         = step[-1] - y_ramp[0][-1]     #erro apos ser adicionado o controlador ao
    print(f"ep(∞) = {ep_MF}")
    print("*********************************************")
    print("Rlocus de gmf")
    rlocusG_MF = rlocus(G_MF)

def plot_c(polesDominant, zero_c, polo_c):
    plt.scatter(polesDominant[0].real,polesDominant[0].imag, color='red')
    plt.scatter(polesDominant[1].real,polesDominant[1].imag, color='red')
    plt.scatter(-abs(zero_c).real,-abs(zero_c).imag, color='blue')
    plt.scatter(-abs(polo_c).real,-abs(polo_c).imag, color='green', marker='X')
    plt.legend(["Polo dominante +", "Polo dominante -", "Zero controlador", "Polo controlador"])
    plt.grid(color='black', linestyle='-', linewidth=0.5)
    plt.show()

def plot_cavat(polesDominant, zero_cav, polo_cav, zero_cat, polo_cat):
    plt.scatter(polesDominant[0].real,polesDominant[0].imag, color='red')
    plt.scatter(polesDominant[1].real,polesDominant[1].imag, color='red')
    plt.scatter(-abs(zero_cav).real,-abs(zero_cav).imag, color='blue')
    plt.scatter(-abs(polo_cav).real,-abs(polo_cav).imag, color='green', marker='X')
    plt.scatter(-abs(zero_cat).real,-abs(zero_cat).imag, color='black')
    plt.scatter(-abs(polo_cat).real,-abs(polo_cat).imag, color='gray', marker='X')
    plt.legend(["Polo dominante +", "Polo dominante -", "Zero controlador avanço", "Polo controlador avanço", "Zero controlador atraso", "Polo controlador atraso"])
    plt.grid(color='black', linestyle='-', linewidth=0.5)
    plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funções para o controlador por lugar das raizes
def get_kc_lr(e_esp, gaindc):
    # Determinando ganho do compensador, Kc
    Kp_s    = symbols('Kp_s')
    eq_Kp   = [(1/(1+Kp_s)) - e_esp]
    Kp      = solve(eq_Kp, Kp_s)
    Kp      = Kp[Kp_s]

    Kc_s    = symbols('Kc_s')
    eq_Kc   = [((Kc_s*gaindc) - Kp)]
    Kc      = solve(eq_Kc, Kc_s)
    Kc      = Kc[Kc_s]

    #print(f"Kc = {Kc}")
    return Kp, Kc

def get_psi(Mp_esp, Mp_folga):
    # Determinando o coeficiente de amortecimento, psi = ξ
    psi     = np.arange(0, 1, 0.01)
    MpVetor = 100*np.exp(((-1*psi*np.pi)/np.sqrt(1-psi**2)))
    MpLoc   = np.where(MpVetor>=(Mp_esp-Mp_folga))[-1][-1] + 1
    psi     = psi[MpLoc]

    #print(f"ξ  = {psi}")
    return psi

def get_wn(ts_esp, psi):
    # Determinando a frequencia natural, Wn
    Wn_s    = symbols('Wn_s')
    eq_Wn   = [4/(psi*Wn_s)-ts_esp]
    Wn      = solve(eq_Wn, Wn_s)
    Wn      = Wn[Wn_s]

    #print(f"Wn = {Wn}\t rad/s")
    return Wn

def get_paramOrd2(psi,Wn):
    # Parametros de uma função de 2ª ordem
    sigma   = psi * Wn
    Wd      = Wn * np.sqrt(1-psi**2)

    #print(f"σ  = {sigma}")
    #print(f"Wd = {Wd}")
    return [sigma, Wd]

def get_poleDominant(sigma, Wd):
    s = []
    s.append(complex(-sigma, Wd))
    s.append(complex(-sigma, -Wd))
    return s

def get_phiByCF(polos_MA, polesDominant, zero_c):
    # Determinando phi pela condição de fase

    # Angulo entre o polo dominante e o zero do controlador
    thetaZero   = np.arctan2(polesDominant[0].imag, polesDominant[0].real - zero_c.real)
    thetaZeroD  = np.degrees(thetaZero)
    #print(f"Angulo entre o zero do controlador e o polo dominante = ϴ =")
    #print(f"\t= {round(thetaZeroD,4)}º = {round(thetaZero,4)} rad")

    # Angulo entre o polo dominante e o polo do controlador
    phiPolo = []
    textSum = "("
    for k in range(len(polos_MA)):
        phiPolo.append(np.arctan2(polesDominant[0].imag, polesDominant[0].real - polos_MA[k]))
        print(f"φ{k} = {round(phiPolo[-1], 4)} rad")
        textSum += f"+ {round(np.degrees(phiPolo[-1]), 3)} "
    textSum += ")"

    phiPoloD    = np.degrees(phiPolo)
    phiPolo_C   = (180 - np.sum(phiPoloD) + thetaZeroD)
    #print(polos_MA)
    #print(f"Angulo entre o polo do controlador e o polo dominante = φ{len(polos_MA)} =")
    #print(f"\t= 180 - {textSum} + {round(thetaZeroD,3)} =")
    #print(f"\t= {round(phiPolo_C, 4)}º = {round(np.radians(phiPolo_C),4)} rad")
    return [textSum, thetaZero, thetaZeroD, phiPolo_C]

def get_posPole(polesDominant, phiPolo_C, zero_c):
    d_s         = symbols('d_s')
    eq_d        = [polesDominant[0].imag/d_s - np.tan(np.radians(phiPolo_C))]
    d           = solve(eq_d, d_s)
    return (-1*(abs(d[d_s]) + abs(zero_c.real)))

def get_KcByCM(polesDominant, polos_MA, zero_c, polo_c, Kp_MA):
    h = []
    for k in range(len(polos_MA)): 
        h.append(np.sqrt((abs(polesDominant[0].imag)-abs(polos_MA[k].imag))**2 + (abs(polesDominant[0].real) - abs(polos_MA[k].real))**2))

    h.append(np.sqrt((abs(polesDominant[0].imag) - abs(polo_c.imag))**2 + (abs(polesDominant[0].real) - abs(polo_c.real))**2))

    c = np.sqrt((abs(polesDominant[0].imag) - abs(zero_c.imag))**2 + (abs(polesDominant[0].real) - abs(zero_c.real))**2)

    Kc = np.prod(h) / (c*Kp_MA) 

    #print(f"Kc  = {Kc}")
    return Kc


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funções para o controlador por resposta em frequencia
def get_kc_rf(e_esp, Kp_MA):
    # Determinando ganho do compensador, Kc
    Kv_min  = 1 / e_esp
    Kp      = Kp_MA

    Kc      = Kv_min / Kp

    #print(f"Kc = {Kc}")
    return Kc

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funções para o controlador em avanço por resposta em frequencia
def get_a_av(phiMax, deg=True):
    if deg:
        return (1-np.sin(np.radians(phiMax))) / (1+np.sin(np.radians(phiMax)))
    else:
        return (1-np.sin(phiMax)) / (1+np.sin(phiMax))

def get_Wm(Kc,a,mag_MA, wout_MA):
    C_jwm = 20 * np.log10(Kc/np.sqrt(a))        # em Db

    magDb = 20 * np.log10(mag_MA)
    # % Lugar em que cruzar pela reta [-C_jwm -C_jwm] é referente a frequencia Wm
    # % encontra o ponto de cruzamento
    magDbLoc  = np.where(magDb >= -float((C_jwm)))[-1][-1]
    Wm        = wout_MA[magDbLoc]
    #print(f"C(jWm) = {C_jwm}")
    #print(f"Wm = {Wm}")
    return [C_jwm, Wm ]

def get_T_av(a, Wm):
    return 1 /(np.sqrt(a)*Wm)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funções para o controlador em atraso por resposta em frequencia
def get_Wcd(phase_MA, MFd, MFseg, wout_MA):
    phaseLoc  = np.where(180+np.degrees(phase_MA) >= (MFseg+MFd))[-1][0] - 1  #primeiro seleciona o array (só retorna 1), depois seleciona qual item (0 ==first, -1 == last)
    Wcd       = wout_MA[phaseLoc]
    #print(f"C(jWm) = {C_jwm}")
    #print(f"Wcd = {Wcd}")
    return Wcd

def get_a_at(mag_Cat, wout_MA, Wcd):
    magDb_Cat                       = 20*np.log10(mag_Cat)
    wLoc                            = np.where(wout_MA >= Wcd)[-1][-1]-1
    KcG_WCD                         = magDb_Cat[wLoc]
    return 10**(abs(KcG_WCD)/20)

def get_T_at(Wcd):
    return 10 /(Wcd)
