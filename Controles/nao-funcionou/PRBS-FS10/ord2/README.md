# Controles para a planta gerada com o PRBS (fs=10) de primeira ordem

*******
## Planta (Controlador = 1)
Gma= (0.2023 * s^2 + 8.817 * s+96.12) / (s^2+30.25 * s+77.26)


Polos de G(s) -> [-27.43376212  -2.81623788]\
Zeros de G(s) -> [-21.79189323+0.49932582j -21.79189323-0.49932582j]

Malha Aberta\
C(s) * G(s) = (0.2023 s^2 + 8.817 s + 96.12) / (s^2 + 30.25 s + 77.26)

Malha Fechada\
Gmf = (0.2023 s^2 + 8.817 s + 96.12) / (1.202 s^2 + 39.07 s + 173.4)

stepinfo: 
* RiseTime: 0.36992290998655425
* SettlingTime: 0.6685035444757016
* SettlingMin: 0.4989385868830104
* SettlingMax: 0.5540295222825732
* Overshoot: 0.0
* Undershoot: 0.16826083340264494
* Peak: 0.5540295222825732
* PeakTime: 1.3198320967020276
* SteadyStateValue: 0.5540295222825732

ep(∞) = 0.4456107970930905\
ev(∞) = 88.750613236763

*************
## Controlador em avanço por lugar das raizes
**Especificações:**
* e_esp           = 0.01
* ts_esp          = 0.4  
* Mp_esp          = 50          
* Mp_folga        = 5   


ξ  = 0.25\
Wn = 40.0000000000000	 rad/s\
σ  = 10.0000000000000\
Wd = 38.7298334620742

Polo dominante 1 -> (-10+38.72983346207417j)\
Polo dominante 2 -> (-10-38.72983346207417j)

**Zero controlador** -> (-10+0j)

φ0 = 1.1478 rad\
φ1 = 1.7542 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
	= 90.0º = 1.5708 rad\
Angulo entre o polo do controlador e o polo dominante = φ2 =\
	= 180 - (+ 65.766 + 100.508 ) + 90.0 =\
	= 103.7263º = 1.8104 rad\
**Polo controlador** -> (-19.460141271442986+0j)

Kc  = 8513.131231004896

Controle de avanço = Kc * (s+z)/(s+p) = \
	= 8513.131231004896 *  (s+z)/(s+p) = \	
	= (8513 s + 8.513e+04) / (s + 19.46)
    

Malha Aberta\
C(s) * G(s) =  (1722 s^3 + 9.228e+04 s^2 + 1.569e+06 s + 8.183e+06) / (s^3 + 49.71 s^2 + 665.9 s + 1503)
         

Malha Fechada\
Gmf = (1722 s^3 + 9.228e+04 s^2 + 1.569e+06 s + 8.183e+06) / (1723 s^3 + 9.233e+04 s^2 + 1.57e+06 s + 8.184e+06)

ep(∞) = 0.000183703661868595\
ev(∞) = 0.03660316532275942






**************************
## Controlador em atraso por lugar das raizes
**Especificações:**
* e_esp           = 0.01
* ts_esp          = 0.4  
* Mp_esp          = 50          
* Mp_folga        = 5   


Kc = 79.5749063670412\
Kp = 99.0000000000000\
ξ  = 0.25\
Wn = 40.0000000000000	 rad/s\
σ  = 10.0000000000000\
Wd = 38.7298334620742

Polo dominante 1 -> (-10+38.72983346207417j)\
Polo dominante 2 -> (-10-38.72983346207417j)

**Polo controlador** -> (-0.02+0j)

**Zero controlador** -> (-1.591498127340824+0j)

Kc  = 8345.727546342298

Controle de atraso = Kc * (s+z)/(s+p) = \
	= 8345.727546342298 *  (s+z)/(s+p) = \
	= (8346 s + 1.328e+04) / (s + 0.02)

Malha Aberta\
C(s) * G(s) = (1688 s^3 + 7.627e+04 s^2 + 9.193e+05 s + 1.277e+06) / ( s^3 + 30.27 s^2 + 77.87 s + 1.545)

Malha Fechada\
Gmf = (1688 s^3 + 7.627e+04 s^2 + 9.193e+05 s + 1.277e+06) / (1689 s^3 + 7.63e+04 s^2 + 9.194e+05 s + 1.277e+06)

ep(∞) = 1.2103196300738972e-06\
ev(∞) = 0.0003009718854229959

************
## Controlador em avanço-atraso por lugar das raizes
**Especificações:**
* e_esp           = 0.01
* ts_esp          = 0.4  
* Mp_esp          = 50          
* Mp_folga        = 5   


Kc = 79.5749063670412\
Kp = 99.0000000000000\
ξ  = 0.25\
Wn = 40.0000000000000	 rad/s\
σ  = 10.0000000000000\
Wd = 38.7298334620742

Polo dominante 1 -> (-10+38.72983346207417j)\
Polo dominante 2 -> (-10-38.72983346207417j)

**Zero controlador av** -> (-10+0j)

φ0 = 1.1478 rad\
φ1 = 1.7542 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
	= 90.0º = 1.5708 rad\
Angulo entre o polo do controlador e o polo dominante = φ2 =\
	= 180 - (+ 65.766 + 100.508 ) + 90.0 =\
	= 103.7263º = 1.8104 rad\
**Polo controlador** -> (-19.460141271442986+0j)

Kc  = 8513.131231004896

Controle de avanço = Kc * (s+z)/(s+p) = \
	= 8513.131231004896 *  (s+z)/(s+p) = \
	=	8513.131231004896 * (s + 10) / (s + 19.460141)

**Polo controlador at** -> 0.02\
**Zero controlador at** -> (-0.0004365600982890086+0j)

Controle de atraso = Kc * (s+z)/(s+p) = \
	= 89.81766929039748 *  (s+z)/(s+p) = \
	= 89.81766929039748 * (s + 0.03624) / (s + 0.02)

Controle em atraso e avanço = Kc * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
	= 8513.131231004896 * (s+zav)/(s+pav) * (s+zat)/(s+pat) = 	\
	= (8513 s^2 + 8.514e+04 s + 37.16) / (s^2 + 19.48 s + 0.3892)


Malha Aberta\
C(s) * G(s) = (1722 s^4 + 9.228e+04 s^3 + 1.569e+06 s^2 + 8.184e+06 s + 3572) /(s^4 + 49.73 s^3 + 666.9 s^2 + 1517 s + 30.07)

Malha Fechada\
Gmf = (1722 s^4 + 9.228e+04 s^3 + 1.569e+06 s^2 + 8.184e+06 s + 3572) / (1723 s^4 + 9.233e+04 s^3 + 1.57e+06 s^2 + 8.185e+06 s + 3602)

ep(∞) = 0.0008691583646575074\
ev(∞) = 0.10588980732924824

*****
## Controlador em avanço por resposta em frequencia
**Especificações:**
* e_esp           = 1.1			
* MFd             = 90
* MFseg           = 5

**Observação:** com um e_esp menor que 1.1 não esta funcionando (acha φ_max = inf)

Kc = 4.493776120073697

φ_max = -62.751595735438855

a = 17.02287174184123

C(jWm) = 0.7419003715776502\
Wm = 1.534387212302052

T = 0.15796054231817191

Controlador em avanço = Kc * (T*s+1)/(T*a*s+1) = \
	= 4.493776120073697 *  (0.16*s+1)/(0.16*17.02*s+1) = \
	= (0.7098 s + 4.494) / (2.689 s + 1)

Malha Aberta\
C(s) * G(s) = (0.1436 s^3 + 7.168 s^2 + 107.9 s + 431.9) / (2.689 s^3 + 82.34 s^2 + 238 s + 77.26)

Malha Fechada\
Gmf = (0.1436 s^3 + 7.168 s^2 + 107.9 s + 431.9) / (2.833 s^3 + 89.51 s^2 + 345.8 s + 509.2)

ep(∞) =  0.15172767647078667\
ev(∞) = 30.558148053571728

*****
## Controlador em atraso por resposta em frequencia
**Especificações:**
* e_esp           = 0.01
* MFd             = 50
* MFseg           = 5


Kc = 494.31537320810673

Wcd = 628.3185307179585

a = 100.03485703961142

T = 0.015915494309189537

Controlador em atraso = Kc * (T*s+1)/(T*a*s+1) = \
	= 494.31537320810673 *  (0.02*s+1)/(0.02*100.03*s+1) = \
	= (7.867 s + 494.3) / (1.592 s + 1)

Malha Aberta
C(s) * G(s) = (1.592 s^3 + 169.4 s^2 + 5115 s + 4.751e+04) / (1.592 s^3 + 49.16 s^2 + 153.3 s + 77.26)

Malha Fechada
Gmf = (1.592 s^3 + 169.4 s^2 + 5115 s + 4.751e+04) / (3.184 s^3 + 218.5 s^2 + 5268 s + 4.759e+04)

ep(∞) = 0.0016234211836443357\
ev(∞) = 0.3261014008904226