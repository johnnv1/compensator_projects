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
* ts_esp          = 1  
* Mp_esp          = 50          
* Mp_folga        = 5   

Polos de G(s) -> [-27.43376212  -2.81623788]\
Zeros de G(s) -> [-21.79189323+0.49932582j ,  -21.79189323-0.49932582j]\
ξ  = 0.25\
Wn = 16.0000000000000    rad/s\
σ  = 4.00000000000000\
Wd = 15.4919333848297\


Polo dominante 1 -> (-4+15.491933384829668j)\
Polo dominante 2 -> (-4-15.491933384829668j)


Zero controlador -> (-4+0j)


φ0 = 0.5841 rad\
φ1 = 1.6471 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 90.0º = 1.5708 rad\
Angulo entre o polo do controlador e o polo dominante = φ2 =\
        = 180 - (+ 33.468 + 94.37 ) + 90.0 =\
        = 142.162º = 2.4812 rad\
Polo controlador -> (-23.94472249196986+0j)


Kc  = 6.497155770499008


Controle de avanço = Kc * (s+z)/(s+p) = \
        = 6.497155770499008 *  (s+z)/(s+p) = \
	= (6.497 s + 25.99)/(s + 23.94)

Malha Aberta\
C(s) * G(s) = (1.314 s^3 + 62.54 s^2 + 853.6 s + 2498)/(s^3 + 54.19 s^2 + 801.6 s + 1850)


Malha Fechada
Gmf = (1.314 s^3 + 62.54 s^2 + 853.6 s + 2498)/(2.314 s^3 + 116.7 s^2 + 1655 s + 4348)


stepinfo: 
* RiseTime: 0.0
* SettlingTime: 0.597497884702595
* SettlingMin: 0.5196662340108967
* SettlingMax: 0.574444411719635
* Overshoot: 0.0
* Undershoot: 0.5196662340108967
* Peak: 0.574444411719635
* PeakTime: 2.0725707875621264
* SteadyStateValue: 0.574444411719635

ev(∞) = 84.69217342067924
ep(∞) = 0.42547633046577193


#### Correção de variação no permanente (v1)
AO testar o controlador na planta real ele mostrou uma variação no regime permanente, para corrigir isto, colocando o zero em (sigma*3)

Zero controlador -> (-12+0j)

φ0 = 0.5841 rad\
φ1 = 1.6471 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 62.6883º = 1.0941 rad\
Angulo entre o polo do controlador e o polo dominante = φ2 =\
        = 180 - (+ 33.468 + 94.37 ) + 62.688 =\
        = 114.8502º = 2.0045 rad\
Polo controlador -> (-19.174765558397297+0j)


Kc  = 4.957101913049167


Controle de avanço = Kc * (s+z)/(s+p) = \
        = 4.957101913049167 *  (s+z)/(s+p) = \
	=(4.957 s + 59.49)/(s + 19.17)

Malha Aberta\
C(s) * G(s) = (1.003 s^3 + 55.74 s^2 + 1001 s + 5718)/(s^3 + 49.42 s^2 + 657.3 s + 1481)


Malha Fechada\
Gmf = (1.003 s^3 + 55.74 s^2 + 1001 s + 5718)/(2.003 s^3 + 105.2 s^2 + 1658 s + 7199)


stepinfo: 
* RiseTime: 0.1948119168899028
* SettlingTime: 0.4191407908843363
* SettlingMin: 0.7146906273964402
* SettlingMax: 0.7939299653567609
* Overshoot: 0.0
* Undershoot: 0.5007044353937952
* Peak: 0.7939299653567609
* PeakTime: 0.9829146715808733
* SteadyStateValue: 0.7939299653567609

ev(∞) = 40.994090092004285\
ep(∞) = 0.2057798370718762

#### Correção de variação no permanente (v2)
AO testar o controlador na planta real ele mostrou uma variação no regime permanente, para corrigir isto, colocando o zero em (sigma*4.5)

Zero controlador -> (-18+0j)


φ0 = 0.5841 rad\
φ1 = 1.6471 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 47.896º = 0.8359 rad\
Angulo entre o polo do controlador e o polo dominante = φ2 =\
        = 180 - (+ 33.468 + 94.37 ) + 47.896 =\
        = 100.058º = 1.7463 rad\
Polo controlador -> (-20.747807471859684+0j)


Kc  = 4.35463679301675


Controle de avanço = Kc * (s+z)/(s+p) = \
        = 4.35463679301675 *  (s+z)/(s+p) = \
	= (4.355 s + 78.38)/(s + 20.75)

Malha Aberta\
C(s) * G(s) = (0.8809 s^3 + 54.25 s^2 + 1110 s + 7534)/(s^3 + 51 s^2 + 704.9 s + 1603)


Malha Fechada\
Gmf = (0.8809 s^3 + 54.25 s^2 + 1110 s + 7534)/(1.881 s^3 + 105.2 s^2 + 1815 s + 9137)


stepinfo: 
* RiseTime: 0.17328401503832344
* SettlingTime: 0.3528692669871314
* SettlingMin: 0.7421380182128929
* SettlingMax: 0.8242134579889446
* Overshoot: 0.0
* Undershoot: 0.4683517854335546
* Peak: 0.8242134579889446
* PeakTime: 0.7868669591967505
* SteadyStateValue: 0.8242134579889446

ev(∞) = 34.95369493585241\
ep(∞) = 0.1754341218361981

**************************
## Controlador em atraso por lugar das raizes
**Especificações:**
* e_esp           = 0.01
* ts_esp          = 1  
* Mp_esp          = 50          
* Mp_folga        = 5  

Kc = 79.5749063670412\
Kp = 99.0000000000000\
ξ  = 0.25\
Wn = 16.0000000000000    rad/s\
σ  = 4.00000000000000\
Wd = 15.4919333848297


Polo dominante 1 -> (-4+15.491933384829668j)\
Polo dominante 2 -> (-4-15.491933384829668j)


Polo controlador -> (-0.04+0j)


Zero controlador -> (-3.182996254681648+0j)


Kc  = 4.107999672421004


Controle de atraso = Kc * (s+z)/(s+p) = \
        = 4.107999672421004 *  (s+z)/(s+p) = \
		= (4.108 s + 13.08)/(s + 0.04)

Malha Aberta\
C(s) * G(s) = (0.831 s^3 + 38.87 s^2 + 510.1 s + 1257)/(s^3 + 30.29 s^2 + 78.47 s + 3.09)


Malha Fechada\
Gmf = (0.831 s^3 + 38.87 s^2 + 510.1 s + 1257)/(1.831 s^3 + 69.16 s^2 + 588.6 s + 1260)


stepinfo: 
* RiseTime: 0.20230179499990697
* SettlingTime: 0.3582427619790019
* SettlingMin: 0.899130323429953
* SettlingMax: 1.0010229977609502
* Overshoot: 0.6285247164138479
* Undershoot: 0.45386477157460087
* Peak: 1.0010229977609502
* PeakTime: 0.7080562824996743
* SteadyStateValue: 0.997605453183839


ev(∞) = 0.5492488663812196\
ep(∞) = 0.002452832234987712

************
## Controlador em avanço-atraso por lugar das raizes
**especificações**
* e_esp           = 0.01
* ts_esp          = 1  
* Mp_esp          = 50          
* Mp_folga        = 5  

Kc = 79.5749063670412\
Kp = 99.0000000000000\
ξ  = 0.25\
Wn = 16.0000000000000    rad/s\
σ  = 4.00000000000000\
Wd = 15.4919333848297


Polo dominante 1 -> (-4+15.491933384829668j)\
Polo dominante 2 -> (-4-15.491933384829668j)


Zero controlador av -> (-18+0j)


φ0 = 0.5841 rad\
φ1 = 1.6471 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 47.896º = 0.8359 rad\
Angulo entre o polo do controlador e o polo dominante = φ2 =\
        = 180 - (+ 33.468 + 94.37 ) + 47.896 =\
        = 100.058º = 1.7463 rad\
Polo controlador av -> (-20.747807471859684+0j)


Kc  = 4.35463679301675


Controle de avanço = Kc * (s+z)/(s+p) = \
        = 4.35463679301675 *  (s+z)/(s+p) =     
		= 4.35463679301675*(s + 18)/(s + 20.75)



Polo controlador at -> 0.04\
Zero controlador at -> (-1.011032555484913+0j)


Controle de atraso = Kc * (s+z)/(s+p) = \
        = 4.35463679301675 *  (s+z)/(s+p) = \
		= 4.35463679301675*(s + 1.011)/(s + 0.04)



Controle em atraso e avanço = Kc * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
        = 4.35463679301675 * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
		= (4.355 s^2 + 82.79 s + 79.25)/(s^2 + 20.79 s + 0.8299)


Malha Aberta\
C(s) * G(s) = (0.8809 s^4 + 55.14 s^3 + 1165 s^2 + 8656 s + 7617)/(s^4 + 51.04 s^3 + 706.9 s^2 + 1631 s + 64.12)


Malha Fechada\
Gmf = (0.8809 s^4 + 55.14 s^3 + 1165 s^2 + 8656 s + 7617)/(1.881 s^4 + 106.2 s^3 + 1871 s^2 + 1.029e+04 s + 7681)


stepinfo: 
* RiseTime: 0.4613437690297052
* SettlingTime: 2.1714973956053365
* SettlingMin: 0.8935387200208207
* SettlingMax: 0.9915298745052169
* Overshoot: 0.0
* Undershoot: 0.4683517854335546
* Peak: 0.9915298745052169
* PeakTime: 7.9462487113909575
* SteadyStateValue: 0.9915298745052169

ev(∞) = 1.8622745771989457\
ep(∞) = 0.008347245409016657

*****
## Controlador em avanço por resposta em frequencia
**especificações**
* e_esp           = 1.01
* MFd             = 50
* MFseg           = 5

**Obs.:** Colocando e_esp menor ou igual a 1 não é possivel realizar o projeto

Kc = 4.894211615921849


φ_max = -117.26933192846434


a = 16.995742461429852


C(jWm) = 1.4902534534332146\
Wm = 2.6967018282621806


T = 0.08994913673018978


Controlador em avanço = Kc * (T*s+1)/(T*a*s+1) = \
        = 4.894211615921849 *  (0.09 * s+1)/(0.09 * 17.0 *s+1) = \
		= (0.4402 s + 4.894)/(1.529 s + 1)

Malha Aberta\
C(s) * G(s) = (0.08906 s^3 + 4.872 s^2 + 85.47 s + 470.4)/(1.529 s^3 + 47.24 s^2 + 148.4 s + 77.26)


Malha Fechada\
Gmf = (0.08906 s^3 + 4.872 s^2 + 85.47 s + 470.4)/ (1.618 s^3 + 52.12 s^2 + 233.8 s + 547.7)


stepinfo: 
* RiseTime: 0.5488385832938912
* SettlingTime: 1.5652063301344303
* SettlingMin: 0.7745134902262143
* SettlingMax: 0.907275971979747
* Overshoot: 6.08251484973629
* Undershoot: 0.05504880110720384
* Peak: 0.907275971979747
* PeakTime: 1.054118548866045
* SteadyStateValue: 0.8584113270425151


ev(∞) = 28.282551435319505\
ep(∞) = 0.1410647837304997



*****
## Controlador em atraso por resposta em frequencia
**especificações**
* e_esp           = 0.15
* MFd             = 50
* MFseg           = 5


Kc = 32.95435821387378

Wcd = 628.3185307179585

a = 6.668261649766948


T = 0.015915494309189537


Controlador em atraso = Kc * (T*s+1)/(T*a*s+1) = \
        = 32.95435821387378 *  (0.02*s+1)/(0.02*6.67*s+1) = \
		= (0.5245 s + 32.95)/(0.1061 s + 1)

Malha Aberta\
C(s) * G(s) = (0.1061 s^3 + 11.29 s^2 + 341 s + 3168)/(0.1061 s^3 + 4.21 s^2 + 38.45 s + 77.26)


Malha Fechada \
Gmf = (0.1061 s^3 + 11.29 s^2 + 341 s + 3168)/(0.2122 s^3 + 15.5 s^2 + 379.4 s + 3245)

stepinfo: 
* RiseTime: 0.03978670885007753
* SettlingTime: 0.0643506769227341
* SettlingMin: 0.8804429688651458
* SettlingMax: 0.9949290866098339
* Overshoot: 3.8509521805558085
* Undershoot: 0.49994019528780237
* Peak: 0.9949290866098339
* PeakTime: 0.12108998345675771
* SteadyStateValue: 0.9765741412736237

ev(∞) = 4.747287713298363
ep(∞) = 0.023810162836357396