# Leituras das plantas

Este projeto é realizado com um motor girando um taco gerador, os dados lidos pelo arduino são os valores da nossa planta a saída da planta é a saida da placa condicionadora onde em sua entrada entra os valores do taco. Ou seja, nosso sistema se comporta da seguinte forma:

Arduino PWM (u)     ->  regulador de tensão ->  motor DC    -conexão via correia->      Taco    ->  placa condicionadora    ->      arduino lê (y)

## Arquivos
* Nome dos arquivos ttttt-FSxxxx.{csv,svg}
  * Onde *ttttt* é referente ao tipo de dado de entrada
    * **Degrau**: Gera um degrau na entrada
    * **Escada**: Gera uma sequencia de degrau incrementando de 1 em 1V na entrada
    * **Rampa**: Gera uma rampa na entrada
    * **PRBS**: Gera um sinal pseudo randomico na entrada
  * Onde *xxxx* é referente a frequency sample (frequencia de amostragem) utilizada
* Valores de **u**: valores de entrada da planta
* Valores de **y**: valores de saida da planta
* Valor **Fs**: frequency sample (frequencia de amostragem) utilizada

## Pastas
* Pasta [gerados-com-python](./gerados com python/)
  * possui os arquivos gerados utilizando o algoritmo [LeituraMA.py](./../../Python-codes/Testar-Planta/LeituraMA.py)
  * Possui arquivos com o seguinte padrão de nome yyyymmdd-H:M:S-FsX-NK-NvP onde:
    * yyyy é o ano que foi executado o algoritmo
    * mm é o mes que foi executado o algoritmo
    * dd é o dia que foi executado o algoritmo
    * H é a hora que foi executado o algoritmo
    * M é em qual minuto que foi executado o algoritmo
    * S é em qual segundo  que foi executado o algoritmo
    * X é a frequencia de amostragem utilizada
    * K é a quantidade de amostras utilizadas
    * P é a quantidae de trocas de sinal realizadas
