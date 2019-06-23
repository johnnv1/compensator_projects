# Controles para a planta gerada com o PRBS (fs=10) de primeira ordem

## Planta (Controlador = 1)
Gma= 2.096/(s + 1.663


Polos de G(s) -> [-1.663]\
Zeros de G(s) -> []

Malha Aberta\
C(s) * G(s) = 2.096 / (s + 1.663)

Malha Fechada\
Gmf = 2.096 / (s + 3.759)

stepinfo: 
* RiseTime: 0.5815871737659447
* SettlingTime: 1.0308259842710494
* SettlingMin: 0.5015960519309117
* SettlingMax: 0.5570866441607296
* Overshoot: 0.0
* Undershoot: 0.0
* Peak: 0.5570866441607296
* PeakTime: 1.8621973929236497
* SteadyStateValue: 0.5570866441607296

ep(∞) = 0.4424048949188617\
ev(∞) = 88.18691011042336

*************
## Controlador em avanço por lugar das raizes
**Especificações:**
* e_esp           = 0.1
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

φ0 = 1.7828 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
	= 90.0º = 1.5708 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
	= 180 - (+ 102.148 ) + 90.0 =\
	= 167.8519º = 2.9296 rad\
**Polo controlador** -> (-189.92083483267314+0j)

Kc  = 89.81766929039748

Controle de avanço = Kc * (s+z)/(s+p) = \
	= 89.81766929039748 *  (s+z)/(s+p) = 	\
= (89.82 s + 898.2) / (s + 189.9)

Malha Aberta\
C(s) * G(s) = (188.3 s + 1883) / (s^2 + 191.6 s + 315.8)

Malha Fechada\
Gmf = (188.3 s + 1883) / (s^2 + 379.8 s + 2198)

stepinfo:
* RiseTime: 0.24196200463245046
* SettlingTime: 0.5149142167547714
* SettlingMin: 0.7704788101966191
* SettlingMax: 0.856006758322477
* Overshoot: 0.0
* Undershoot: 0.0
* Peak: 0.856006758322477
* PeakTime: 1.190739126245409
* SteadyStateValue: 0.856006758322477

ep(∞) = 0.14366627983109048\
ev(∞) = 28.651913355705744






**************************
## Controlador em atraso por lugar das raizes
**Especificações:**
* e_esp           = 0.1
* ts_esp          = 0.4  
* Mp_esp          = 50          
* Mp_folga        = 5   
Kc = 7.14074427480916\
Kp = 9.00000000000000\
ξ  = 0.25\
Wn = 40.0000000000000	 rad/s\
σ  = 10.0000000000000\
Wd = 38.7298334620742

Polo dominante 1 -> (-10+38.72983346207417j)\
Polo dominante 2 -> (-10-38.72983346207417j)

**Polo controlador** -> (-0.02+0j)

**Zero controlador** -> (-0.14281488549618324+0j)

Kc  = 18.91564411777193

Controle de atraso = Kc * (s+z)/(s+p) = \
	= 18.91564411777193 *  (s+z)/(s+p) = \
	= (18.92 s + 2.701) / (s + 0.02)

Malha Aberta\
C(s) * G(s) = (39.65 s + 5.662) / (s^2 + 1.683 s + 0.03326)

Malha Fechada\
Gmf = (39.65 s + 5.662) / (s^2 + 41.33 s + 5.695)

stepinfo: 
* RiseTime: 0.05067749480360033
* SettlingTime: 3.395392151841222
* SettlingMin: 0.9480377107162655
* SettlingMax: 0.9941313016474866
* Overshoot: 0.0
* Undershoot: 0.0
* Peak: 0.9941313016474866
* PeakTime: 50.62681730879673
* SteadyStateValue: 0.9941313016474866

ep(∞) = 0.005839729884324463\
ev(∞) = 1.4152272588946175

************
## Controlador em avanço-atraso por lugar das raizes
**Especificações:**
* e_esp           = 0.1
* ts_esp          = 0.4  
* Mp_esp          = 50          
* Mp_folga        = 5   


Kc = 7.14074427480916\
Kp = 9.00000000000000\
ξ  = 0.25\
Wn = 40.0000000000000	 rad/s\
σ  = 10.0000000000000\
Wd = 38.7298334620742

Polo dominante 1 -> (-10+38.72983346207417j)\
Polo dominante 2 -> (-10-38.72983346207417j)

**Zero controlador av** -> (-10+0j)

φ0 = 1.7828 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
	= 90.0º = 1.5708 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
	= 180 - (+ 102.148 ) + 90.0 =\
	= 167.8519º = 2.9296 rad\
**Polo controlador av** -> (-189.92083483267314+0j)

Kc  = 89.81766929039748

Controle de avanço = Kc * (s+z)/(s+p) = \
	= 89.81766929039748 *  (s+z)/(s+p) = \
	=	89.81766929039748 * (s + 10) / (s + 189.9)

**Polo controlador at** -> 0.02\
**Zero controlador at** -> (-0.036238111045530166+0j)

Controle de atraso = Kc * (s+z)/(s+p) = \
	= 89.81766929039748 *  (s+z)/(s+p) = \
	= 89.81766929039748 * (s + 0.03624) / (s + 0.02)

Controle em atraso e avanço = Kc * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
	= 89.81766929039748 * (s+zav)/(s+pav) * (s+zat)/(s+pat) = 	\
	= (89.82 s^2 + 901.4 s + 32.55) / (s^2 + 189.9 s + 3.798)


Malha Aberta\
C(s) * G(s) = (188.3 s^2 + 1889 s + 68.22) /(s^3 + 191.6 s^2 + 319.7 s + 6.317)

Malha Fechada\
Gmf = (188.3 s^2 + 1889 s + 68.22) / (s^3 + 379.9 s^2 + 2209 s + 74.54)

ep(∞) = 0.08481362608897158\
ev(∞) = 18.639499858786508

*****
## Controlador em avanço por resposta em frequencia
**Especificações:**
* e_esp           = 0.01
* MFd             = 50
* MFseg           = 5

**Observação:** se adicionado um disturbio em *dist_p* o sistema se tornou instavel

Kc = 47.70992366412214

φ_max = -35.95287273733294

a = 3.844017972277665

C(jWm) = 27.72432033879914\
Wm = 47.39482115236126

T = 0.010761589118108665

Controlador em avanço = Kc * (T*s+1)/(T*a*s+1) = \
	= 47.70992366412214 *  (0.01*s+1)/(0.01*3.84*s+1) = \
	= (0.5134 s + 47.71) /(0.04137 s + 1)

Malha Aberta\
C(s) * G(s) = (1.076 s + 100) / (0.04137 s^2 + 1.069 s + 1.663)

Malha Fechada\
Gmf = (1.076 s + 100) / (0.04137 s^2 + 2.145 s + 101.7)

stepinfo: 
* RiseTime: 0.027838364261900825
* SettlingTime: 0.15027311193802775
* SettlingMin: 0.8881103030195039
* SettlingMax: 1.1559460530604524
* Overshoot: 17.56120823301817
* Undershoot: 0.0
* Peak: 1.1559460530604524
* PeakTime: 0.061082236147471713
* SteadyStateValue: 0.983271667954663

ep(∞) = 0.016357967008649665\
ev(∞) = 3.26540341596197

*****
## Controlador em atraso por resposta em frequencia
**Especificações:**
* e_esp           = 0.01
* MFd             = 50
* MFseg           = 5


Kc = 47.70992366412214

Wcd = 62.83185307179585

a = 1.8316523655004704

T = 0.15915494309189537

Controlador em atraso = Kc * (T*s+1)/(T*a*s+1) = \
	= 47.70992366412214 *  (0.16*s+1)/(0.16*1.83*s+1) = \
	= (7.593 s + 47.71) / (0.2915 s + 1)

Malha Aberta
C(s) * G(s) = (15.92 s + 100) / (0.2915 s^2 + 1.485 s + 1.663)

Malha Fechada
Gmf = (15.92 s + 100) / (0.2915 s^2 + 17.4 s + 101.7)

stepinfo: 
* RiseTime: 0.036291484289204506
* SettlingTime: 0.13769416097962886
* SettlingMin: 0.8884454903578121
* SettlingMax: 1.0050600069766775
* Overshoot: 2.1726546078449416
* Undershoot: 0.0
* Peak: 1.0050600069766775
* PeakTime: 0.10994184946435481
* SteadyStateValue: 0.9836878672030782

ep(∞) = 0.016357967008649332\
ev(∞) = 3.267040699929794