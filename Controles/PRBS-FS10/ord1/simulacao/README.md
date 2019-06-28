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


#### V3 de correção do controlador em avanço 
Visto que ao aumentar o ganho Kc O controlador se tornou muito variavel na planta, é nescessario aproximar seu zero da origem, tornando o sistema mais lento porem estavel (zero em 3/4*sigma) e para tentar corrigir o regime permanente colocar aumenta-se Kc = 10 *kc

Zero controlador -> (-1+0j)
 

φ0 = 1.333 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 103.7689º = 1.8111 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
        = 180 - (+ 76.377 ) + 103.769 =\
        = 207.3921º = 3.6197 rad\
Polo controlador -> (-3.6251150032662656+0j)
 

Kc  = 12.707151453019534
 

Controle de avanço = Kc * (s+z)/(s+p) = \
        = 12.707151453019534 *  (s+z)/(s+p) = \
        = (12.71 s + 12.71)/(s + 3.625)

Malha Aberta\
C(s) * G(s) = (26.63 s + 26.63)/(s^2 + 5.288 s + 6.029)

 
Malha Fechada\
Gmf = (26.63 s + 26.63)/(s^2 + 31.92 s + 32.66)

 
stepinfo: 
* RiseTime: 0.059590194694472215
* SettlingTime: 1.046138973525179
* SettlingMin: 0.7492799632381618
* SettlingMax: 0.8535056097874538
* Overshoot: 4.663636274184767
* Undershoot: 0.0
* Peak: 0.8535056097874538
* PeakTime: 0.2118762478025679
* SteadyStateValue: 0.8154748298172501

ev(∞) = 36.71095326032756\
ep(∞) = 0.18457004383060538


#### V4 de correção do controlador em avanço 
Visto que ao aumentar o ganho Kc O controlador se tornou muito variavel na planta, é nescessario aproximar seu zero da origem, tornando o sistema mais lento porem estavel (zero em sigma/3) e para tentar corrigir o regime permanente colocar aumenta-se Kc = 10 *kc

Zero controlador -> (-0.4444444444444445+0j)
 

φ0 = 1.333 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 123.1632º = 2.1496 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
        = 180 - (+ 76.377 ) + 123.163 =\
        = 226.7863º = 3.9582 rad\
Polo controlador -> (-1.7224354986211932+0j)
 

Kc  = 5.814227144835149
 

Controle de avanço = Kc * (s+z)/(s+p) = \
        = 5.814227144835149 *  (s+z)/(s+p) = \
        = (5.814 s + 2.584)/(s + 1.722)

Malha Aberta\
C(s) * G(s) = (12.19 s + 5.416)/(s^2 + 3.385 s + 2.864)

 
Malha Fechada\
Gmf = (12.19 s + 5.416)/(s^2 + 15.57 s + 8.281)

 
stepinfo: 
* RiseTime: 0.07626228031415654
* SettlingTime: 4.563026438797033
* SettlingMin: 0.5947232461034949
* SettlingMax: 0.7844564616097123
* Overshoot: 19.90452794031915
* Undershoot: 0.0
* Peak: 0.7844564616097123
* PeakTime: 0.34318026141370445
* SteadyStateValue: 0.6542342270845392

ev(∞) = 68.5953412592196\
ep(∞) = 0.3459146129001427

#### V5 de correção do controlador em avanço 
Visto que ao aumentar o ganho Kc O controlador se tornou muito variavel na planta, é nescessario aproximar seu zero da origem, tornando o sistema mais lento porem estavel (zero em sigma*3/4), sendo este o melhor resultado na planta real ele aprensenta um bom regime transiente porem não segue referencia (apresenta um erro em regime permanente), então ele cumpre seu papel o erro de regime transiente deve ser então corrigido com um controlador de atraso

Zero controlador -> (-1+0j)
 

φ0 = 1.333 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 103.7689º = 1.8111 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
        = 180 - (+ 76.377 ) + 103.769 =\
        = 207.3921º = 3.6197 rad\
Polo controlador -> (-3.6251150032662656+0j)
 

Kc  = 1.2707151453019534
 

Controle de avanço = Kc * (s+z)/(s+p) =\
        = 1.2707151453019534 *  (s+z)/(s+p) =\
        = (1.271 s + 1.271)/(s + 3.625)\

Malha Aberta\
C(s) * G(s) = (2.663 s + 2.663)/(s^2 + 5.288 s + 6.029)

 
Malha Fechada\
Gmf = (2.663 s + 2.663)/(s^2 + 7.952 s + 8.692)

 
stepinfo: 
* RiseTime: 0.17137017057466009
* SettlingTime: 2.2492334887924135
* SettlingMin: 0.2764146254202348
* SettlingMax: 0.3527502157177983
* Overshoot: 15.078636725789691
* Undershoot: 0.0
* Peak: 0.3527502157177983
* PeakTime: 0.5462424187067291
* SteadyStateValue: 0.3065297137281304

ev(∞) = 137.99583939483176\
ep(∞) = 0.6935776022617139

*************
## Controlador em atraso por lugar das raizes
**Especificações:**
* e_esp           = 0.01
* ts_esp          = 3  
* Mp_esp          = 10          
* Mp_folga        = 5   


Kc = 78.5481870229007\
Kp = 99.0000000000000\
ξ  = 0.7000000000000001\
Wn = 1.90476190476190    rad/s\
σ  = 1.33333333333333\
Wd = 1.36027208162721

Polo dominante 1 -> (-1.3333333333333335+1.3602720816272094j)\
Polo dominante 2 -> (-1.3333333333333335-1.3602720816272094j)

**Polo controlador** -> (-0.03+0j)

**Zero controlador** -> (-2.3564456106870226+0j)

Kc  = 0.7390956079446624

Controle de atraso = Kc * (s+z)/(s+p) = \
	= 0.7390956079446624 *  (s+z)/(s+p) = 	\
= (0.7391 s + 1.742) / (s + 0.03)

Malha Aberta\
C(s) * G(s) = (1.549 s + 3.65) / (s^2 + 1.693 s + 0.04989)

Malha Fechada\
Gmf = (1.549 s + 3.65) / (s^2 + 3.242 s + 3.7)

stepinfo:
* RiseTime: 0.95958437774295
* SettlingTime: 1.3875071407904818
* SettlingMin: 0.8884098023827827
* SettlingMax: 1.0038192852079877
* Overshoot: 1.727310276412728
* Undershoot: 0.0
* Peak: 1.0038192852079877
* PeakTime: 2.1136791023256873
* SteadyStateValue: 0.9867746256933532

ep(∞) = 0.013482455549998495\
ev(∞) = 3.1287182402709846

*************
## Controlador em avanço-atraso por lugar das raizes
**Especificações:**
* e_esp           = 0.01
* ts_esp          = 3  
* Mp_esp          = 10          
* Mp_folga        = 5   


Kc = 78.5481870229007\
Kp = 99.0000000000000\
ξ  = 0.7000000000000001\
Wn = 1.90476190476190    rad/s\
σ  = 1.33333333333333\
Wd = 1.36027208162721

Polo dominante 1 -> (-1.3333333333333335+1.3602720816272094j)\
Polo dominante 2 -> (-1.3333333333333335-1.3602720816272094j)

**Zero controlador av** -> (-1.3333333333333335+0j)

φ0 = 1.333 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 90.0º = 1.5708 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
        = 180 - (+ 76.377 ) + 90.0 =\
        = 193.6232º = 3.3794 rad\
**Polo controlador av** -> (-6.946094110040374+0j)

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

**Adicionando controlador de atraso**

**Polo controlador** -> (-0.03+0j)

**Zero controlador** -> (-5.195986132954385+0j)

Kc  = 0.7390956079446624

Controle de atraso = Kc * (s+z)/(s+p) = \
	= 2.83512759702944 *  (s+z)/(s+p) = 	\
= 2.83512759702944 * (s + 5.196) / (s + 0.03)

Controle em atraso e avanço = Kc * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
        = 2.83512759702944 * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
        = (2.835 s^2 + 18.51 s + 19.64) / (s^2 + 6.976 s + 0.2084)

Malha Aberta\
C(s) * G(s) = (5.942 s^2 + 38.8 s + 41.17) / (s^3 + 8.639 s^2 + 11.81 s + 0.3465)

Malha Fechada\
Gmf = (5.942 s^2 + 38.8 s + 41.17) / (s^3 + 14.58 s^2 + 50.61 s + 41.52)

stepinfo:
* RiseTime: 0.6525285433128843
* SettlingTime: 1.6254952105740603
* SettlingMin: 0.8931574871899357
* SettlingMax: 0.9915344807539686
* Overshoot: 0.0
* Undershoot: 0.0
* Peak: 0.9915344807539686
* PeakTime: 5.820321560442602
* SteadyStateValue: 0.9915344807539686

ep(∞) = 0.008347245409015547\
ev(∞) = 1.9353887319515195


#### Correção do controlador v1
Quando implementado na planta real o desempenho não foi tão bom quanto ao da simulação, apresentou um sinal com muita variação, para solucionar isto foi colocado o zero do controlador de avanço em (sigma/2) mais proximo do zero


Zero controlador av -> (-0.6666666666666667+0j)


φ0 = 1.333 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 116.1094º = 2.0265 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
        = 180 - (+ 76.377 ) + 116.109 =\
        = 219.7325º = 3.8351 rad\
Polo controlador av -> (-2.3032297562718633+0j)


Kc  = 0.7364447849781105


Controle de avanço = Kc * (s+z)/(s+p) = \
        = 0.7364447849781105 *  (s+z)/(s+p) =   \
        = 0.7364447849781105*(s + 0.6667)/(s + 2.303)


Controle em atraso e avanço = Kc * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
        = 0.7364447849781105 * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
        = (0.7364 s^2 + 10.26 s + 6.513) / (s^2 + 2.333 s + 0.0691)



Malha Aberta\
C(s) * G(s) = (1.544 s^2 + 21.51 s + 13.65)/(s^3 + 3.996 s^2 + 3.949 s + 0.1149)


Malha Fechada\
Gmf = (1.544 s^2 + 21.51 s + 13.65)/(s^3 + 5.54 s^2 + 25.45 s + 13.77)


stepinfo: 
* RiseTime: 0.36537639541816
* SettlingTime: 2.1580043354385077
* SettlingMin: 0.9059007598276427
* SettlingMax: 1.0801338463843355
* Overshoot: 8.931125065581769
* Undershoot: 0.0
* Peak: 1.0801338463843355
* PeakTime: 0.6964987537658676
* SteadyStateValue: 0.9915750394885237

ev(∞) = 1.9325518472195995\
ep(∞) = 0.008347245409015325

#### Correção do controlador v2
Quando implementado na planta real o desempenho não foi tão bom quanto ao da simulação, a correção do controlador 'v1' apresentou um grande overshoot na plata real, alem de deixa-lá muito lenta para a estabilização, para tentar melhorar o resultado o zero foi colocado em (3/4 * sigma) um pouco mais distante do zero que o a correção v1. **este foi o melhor resultado para cavat**

Zero controlador av -> (-1+0j)


φ0 = 1.333 rad\
Angulo entre o zero do controlador e o polo dominante = ϴ =\
        = 103.7689º = 1.8111 rad\
Angulo entre o polo do controlador e o polo dominante = φ1 =\
        = 180 - (+ 76.377 ) + 103.769 =\
        = 207.3921º = 3.6197 rad

Polo controlador av -> (-3.6251150032662656+0j)


Kc  = 1.2707151453019534


Controle de avanço = Kc * (s+z)/(s+p) = \
        = 1.2707151453019534 *  (s+z)/(s+p) =   \
        = 1.2707151453019534*(  s + 1)/(s + 3.625)


Controle em atraso e avanço = Kc * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
        = 1.2707151453019534 * (s+zav)/(s+pav) * (s+zat)/(s+pat) = \
        =(1.271 s^2 + 11.52 s + 10.25) /   (s^2 + 3.655 s + 0.1088)



Malha Aberta\
C(s) * G(s) = (2.663 s^2 + 24.15 s + 21.49) /(s^3 + 5.318 s^2 + 6.187 s + 0.1809)


Malha Fechada\
Gmf = (2.663 s^2 + 24.15 s + 21.49) /(s^3 + 7.982 s^2 + 30.34 s + 21.67)


stepinfo: 
* RiseTime: 0.4333726641877056
* SettlingTime: 1.9346993936951142
* SettlingMin: 0.8936488100791962
* SettlingMax: 0.991553720183133
* Overshoot: 0.0
* Undershoot: 0.0
* Peak: 0.991553720183133
* PeakTime: 7.731058777205677
* SteadyStateValue: 0.991553720183133

ev(∞) = 1.934978015543038\
ep(∞) = 0.008347245409015325


*************
## Controlador em avanço por resposta em frequencia
**Especificações:**
* e_esp           = 0.01
* MFd             = 50
* MFseg           = 5

**Observação:** se adicionado um disturbio em *dist_p* o sistema se tornou instavel

Kc = 47.70992366412214
 

φ_max = -35.95287273733294
 

a = 3.844017972277665
 

C(jWm) = 27.72432033879914
Wm = 47.39482115236126
 

T = 0.010761589118108665
 

Controlador em avanço = Kc * (T*s+1)/(T*a*s+1) = \
        = 47.70992366412214 *  (0.01*s+1)/(0.01*3.84*s+1) = \
        =(0.5134 s + 47.71)/(0.04137 s + 1)

Malha Aberta\
C(s) * G(s) = 
        (1.076 s + 100)/(0.04137 s^2 + 1.069 s + 1.663)

 
Malha Fechada\
Gmf = 
        (1.076 s + 100)/(0.04137 s^2 + 2.145 s + 101.7)

 
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
 
 
ev(∞) = 3.26540341596197\
ep(∞) = 0.016357967008649665


#### correção do controlador v1
Quando implentado o controlador acima na planta real ele se mostrou muito variavel no regime permanente, porem se comportou bem no regime transitorio, entao em busca de melhorar seu desempenho, foi alterado sua especificação de erro para um valor menos bruto. **este foi o melhor resultado**

**Especificações:**
* e_esp           = 0.1
* MFd             = 50
* MFseg           = 5

Kc = 4.770992366412213
 

φ_max = -44.572762436352264
 

a = 5.707233963846045
 

C(jWm) = 6.007917668808305
Wm = 3.7470550400381044
 

T = 0.11171129576223143
 

Controlador em avanço = Kc * (T*s+1)/(T*a*s+1) = \
        = 4.770992366412213 *  (0.11*s+1)/(0.11*5.71*s+1) = \
        = (0.533 s + 4.771) / (0.6376 s + 1)

Malha Aberta\
C(s) * G(s) = (1.117 s + 10)/(0.6376 s^2 + 2.06 s + 1.663)

 
Malha Fechada\
Gmf = (01.117 s + 1)\(0.6376 s^2 + 3.177 s + 11.66
)
 
stepinfo: 
* RiseTime: 0.3627487698901182
* SettlingTime: 1.2541546617906412
* SettlingMin: 0.7739498389037565
* SettlingMax: 0.9627064379928252
* Overshoot: 12.179625668042446
* Undershoot: 0.0
* Peak: 0.9627064379928252
* PeakTime: 0.7620536173660621
* SteadyStateValue: 0.8581829652753775

ev(∞) = 28.512750691367614\
ep(∞) = 0.14258767041070075


*************
## Controlador em atraso por resposta em frequencia

**Especificações:**
* e_esp           = 0.01
* MFd             = 50
* MFseg           = 5

Kc = 47.70992366412214
 

 

Wcd = 62.83185307179585
 

a = 1.8316523655004704
 

T = 0.15915494309189537
 

Controlador em atraso = Kc * (T*s+1)/(T*a*s+1) = 
        = 47.70992366412214 *  (0.16*s+1)/(0.16*1.83*s+1) = 
7.593 s + 47.71
---------------
  0.2915 s + 1

Malha Aberta
C(s) * G(s) = 
        15.92 s + 100
----------------------------
0.2915 s^2 + 1.485 s + 1.663

 
Malha Fechada
Gmf = 
       15.92 s + 100
---------------------------
0.2915 s^2 + 17.4 s + 101.7

 
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
 
 
 
ev(∞) = 3.267040699929794\
ep(∞) = 0.016357967008649332


#### v2 do controlador 
O controlador na planta real apresentou um comportamento varivavel no regime transitorio, para resolver isto foi alterado o erro esperado para um valor menos brusco. Assim se o controlador praticamente seguiu referencia, não demonstrando muitos problemas no regime transiente **melhor resultado**

**Especificações:**
* e_esp           = 0.03
* MFd             = 50
* MFseg           = 5

Kc = 15.903307888040713

Wcd = 62.83185307179585
 
a = 1.637865381283908

T = 0.15915494309189537

Controlador em atraso = Kc * (T*s+1)/(T*a*s+1) = \
        = 15.903307888040713 *  (0.16*s+1)/(0.16*1.64*s+1) = \
        = (2.531 s + 15.9)/( 0.2607 s + 1)

Malha Aberta\
C(s) * G(s) = (5.305 s + 33.33)/(0.2607 s^2 + 1.434 s + 1.663)

 
Malha Fechada\
Gmf = (5.305 s + 33.33)/(0.2607 s^2 + 6.739 s + 35)

 
stepinfo: 
* RiseTime: 0.08664947673176558
* SettlingTime: 0.3232317558982716
* SettlingMin: 0.8585764536040722
* SettlingMax: 0.9794437733051395
* Overshoot: 2.8086219118539284
* Undershoot: 0.0
* Peak: 0.9794437733051395
* PeakTime: 0.22781997253070949
* SteadyStateValue: 0.9526864139321848

 
ev(∞) = 9.488144996710787\
ep(∞) = 0.047519263922887856
