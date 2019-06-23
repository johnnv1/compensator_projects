# Projetos de compensadores em python

Este projeto foi realizado como trabalho final da cadeira de **Sistemas de controle** no curso *Engenharia de Computação* pela **Universidade Estadual do Rio Grande do Sul**. Realizado entre maio e julho de 2019.


O trabalho foi desenvolvido pelos alunos e avaliado pelo professor indicado na tabela abaixo.

| Atribuição        | Responsabilidade       | Nome                             | e-mail                            |
| -----             | ----------------       | -----------                      | ---------                         |
| Aluno             | Autor                  | `João Gustavo Atkinson Amorim`   | `joaogustavoamorim@gmail.com`     |
| Aluno             | Autor                  | `Lucas Silva Ennes`              | `lucassilvaennes@gmail.com`       |
| Professor         | Co-autor               | `Rodrigo Iván Goytia Mejia`      | `rodrigo-mejia@uergs.edu.br`      |

## Instalação
Utilizando o pip do python3/*pip3* para instalar as bibliotecas utilizadas
> pip install -r requeriments.txt

## Documentação


blablabla

### Lista de abreviaturas
| abreviatura       | Significado       |
| -----             | -----             |
| `MA`              | `Malha aberta`                |
| `MF`              | `Malha fechada`                |
| `cav`             | `Controlador em avanço`                |
| `cat`             | `Controlador em atraso`                |
| `lr`              | `lugar das raizes`                |
| `rf`              | `resposta em frequencia`                |
| `cavlr`           | `Controlador em avanço por lugar das raizes`                |
| `catlr`           | `Controlador em atraso por lugar das raizes`                |
| `cavatlr`         | `Controlador em avanço-atraso por lugar das raizes`                |
| `cavrf`           | `Controlador em avanço por resposta em frequencia`                |
| `catrf`           | `Controlador em atraso por resposta em frequencia`                |
| `cavatrf`         | `Controlador em avanço-atraso por resposta em frequencia`                |



### Estruturas do projeto
* No arquivo [makeControlOrd1.py](./makeControlOrd1.py) é desenvolvido os controladores realizados para a aproximação de **primeira** ordem da planta. 
* No arquivo [makeControlOrd2.py](./makeControlOrd2.py) é desenvolvido os controladores realizados para a aproximação de **segunda** ordem da planta.
* No arquivo [Trabalho_final_sistemas_de_controle.ipynb](./Trabalho_final_sistemas_de_controle.ipynb) foi realizado um jupyter notebook como rascunho deste projeto desenvolvido.
* Na pasta [core/](./core/) encontra-se os arquivos com as funções utilizadas ao longo do trabalho
    * Arquivo [cavlr.py](./core/cavlr.py) monta o controlador em avanço por lugares das raizes
    * Arquivo [catlr.py](./core/catlr.py) monta o controlador em atraso por lugares das raizes
    * Arquivo [cavatlr.py](./core/catavlr.py) monta o controlador em avanço e atraso por lugares das raizes
    * Arquivo [cavrf.py](./core/cavrf.py) monta o controlador em avanço por resposta em frequencia
    * Arquivo [catrf.py](./core/catrf.py) monta o controlador em atraso por resposta em frequencia
    * Arquivo [cavatrf.py](./core/catavrf.py) monta o controlador em avanço e atraso por resposta em frequencia
    * Arquivo [misc.py](./core/misc.py) possui uma miscelânea de funções utilizadas ao longo do projeto
* Na pasta [MATLAB-code/](./MATLAB-code/) possui codigos matlabs que envolvem o trabalho
* Na pasta [leituras/](./leituras/) possui arquivos *csv* com os dados lidos pelo arduino e esses dados plotados nos arquivos *svg*
* Na pasta [out/](./out/) possui arquivos referente aos controladores projetados