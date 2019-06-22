# Leituras das plantas

Este projeto é realizado com um motor girando um taco gerador, os dados lidos pelo arduino são os valores da nossa planta a saída da planta é a saida da placa condicionadora onde em sua entrada entra os valores do taco. Ou seja, nosso sistema se comporta da seguinte forma:

Arduino PWM (u)     ->  regulador de tensão ->  motor DC    -conexão via correia->      Taco    ->  placa condicionadora    ->      arduino lê (y)

## Arquivos
* Valores de **u**: valores de entrada da planta
* Valores de **y**: valores de saida da planta
* Valor **Fs**: frequency sample (frequencia de amostragem) utilizada