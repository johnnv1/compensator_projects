# Controles para a planta gerada com o PRBS (fs=10) de primeira ordem

*******
## Planta (Controlador = 1)
Gma= 2.096/(s + 1.663)


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
* e_esp           = 0.01
* ts_esp          = 3  
* Mp_esp          = 10          
* Mp_folga        = 5   


ξ  = 0.7000000000000001\
Wn = 1.90476190476190    rad/s\
σ  = 1.33333333333333\
Wd = 1.36027208162721

Polo dominante 1 -> (-1.3333333333333335+1.3602720816272094j)\
Polo dominante 2 -> (-1.3333333333333335-1.3602720816272094j)

**Zero controlador** -> (-1.3333333333333335+0j)

φ0 = 1.333 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 90.0º = 1.5708 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
        = 180 - (+ 76.377 ) + 90.0 =\
        = 193.6232º = 3.3794 rad\
**Polo controlador** -> (-6.946094110040374+0j)

Kc  = 2.83512759702944

Controle de avanço = Kc * (s+z)/(s+p) = \
	= 2.83512759702944 *  (s+z)/(s+p) = 	\
= (2.835 s + 3.78) / (s + 6.946)

Malha Aberta\
C(s) * G(s) = (5.942 s + 7.923) / (s^2 + 8.609 s + 11.55)

Malha Fechada\
Gmf = (5.942 s + 7.923) / (s^2 + 14.55 s + 19.47)

stepinfo:
* RiseTime: 0.12217832931631734
* SettlingTime: 1.2734741247969998
* SettlingMin: 0.3688043374508202
* SettlingMax: 0.43448053605645476
* Overshoot: 6.778335642209723
* Undershoot: 0.0
* Peak: 0.43448053605645476
* PeakTime: 0.371234154461118
* SteadyStateValue: 0.4068995208094474

ep(∞) = 0.5931500408896189\
ev(∞) = 118.03572119432432

#### Visto que o erro de posição está muito grande aumentamos Kc
Aumentamos Kc, modificando o controlador anterior de atraso para tentar melhorar o resultado no regie permanete. Multiplicamos por 5 o valor do Kc calculado

Kc  = 14.175637985147201

Controle de avanço = Kc * (s+z)/(s+p) = \
	= 14.175637985147201 *  (s+z)/(s+p) = 	\
= (14.18 s + 18.9) / (s + 6.946)

Malha Aberta\
C(s) * G(s) = (29.71 s + 39.62) / (s^2 + 8.609 s + 11.55)

Malha Fechada\
Gmf = (29.71 s + 39.62) / (s^2 + 38.32 s + 51.17)

stepinfo:
* RiseTime: 0.05058095516395193
* SettlingTime: 0.5108676471559145
* SettlingMin: 0.7000904777553626
* SettlingMax: 0.7976426280431275
* Overshoot: 3.018258824500962
* Undershoot: 0.0
* Peak: 0.7976426280431275
* PeakTime: 0.18209143859022697
* SteadyStateValue: 0.7742730629935896

ep(∞) = 0.2257555293498712\
ev(∞) = 44.92452685457059

#### Visto que o erro de posição ainda esta grande aumentamos Kc
Aumentamos Kc, modificando o controlador anterior de atraso para tentar melhorar o resultado no regie permanete. Multiplicamos por 10 o valor do Kc calculado inicialmente.

Kc  = 28.351275970294402

Controle de avanço = Kc * (s+z)/(s+p) = \
	= 28.351275970294402 *  (s+z)/(s+p) = 	\
= (28.35 s + 37.8) / (s + 6.946)

Malha Aberta\
C(s) * G(s) = (59.42 s + 79.23) / (s^2 + 8.609 s + 11.55)

Malha Fechada\
Gmf = (59.42 s + 79.23) / (s^2 + 68.03 s + 90.78)

stepinfo:
* RiseTime: 0.03087574587827893
* SettlingTime: 0.05145957646379821
* SettlingMin: 0.810017290338665
* SettlingMax: 0.8885328724768058
* Overshoot: 1.805271250500667
* Undershoot: 0.0
* Peak: 0.8885328724768058
* PeakTime: 0.11835702586673588
* SteadyStateValue: 0.8727768823389251

ep(∞) = 0.12724037362627516\
ev(∞) = 25.320311161762675

