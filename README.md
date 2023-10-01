# <p align="center">Projeto: AtomiKingdom </p>

## 1) Integrantes da `Equipe 7`:
<br>

- André Campos
- Mateus Ataíde
- Matheus Pessoa 
- Rodrigo César

<br>
     
## 2) Link para repositório git
  
   https://github.com/MOPDeveloper/AtomiKingdom

<br>

## 3) Como rodar o projeto

### Pré-requisitos

Antes de baixar o projeto você vai precisar ter instalado na sua máquina as seguintes ferramentas:

* [Python 3.9 ou superior](https://www.python.org/downloads/)
* [Pygame](https://www.pygame.org/news)

### Em seguida:

```bash
# Clone o repositório
$ git clone https://github.com/Dev-JoseRonaldo/projeto-p1-equipe7.git

# Abrir o projeto
Abra a pasta clonada em seu editor de código favorito.

# Iniciar o jogo
Execute o arquivo main.py presente na raiz do repositório.

# O seu editor de código rodará o jogo em uma nova janela.
```

<br>

## 4) A organização do código; 
<br>
Para a organização do código, seguimos uma estrutura com arquivo main.py, arquivo README.md e arquivos separados por classes e funções dentro do jogo e a pasta "assets". O arquivo main.py foi utilizado para ser o arquivo principal do código, com todos os elementos e funcionalidades sendo chamados dentro do mesmo.  

<br>
<br>

O arquivo main.py está estruturado da seguinte forma: 


        1. Importações 

        2. Parâmetros Tela geral do pygame 

        3. Definição de Sprites   

        4. Variáveis e Funções necessárias para os desenhos do jogo.

        5. Loop principal
 

Os arquivos armazenam as diferentes classes. Dentro da pasta “assets” temos todas as imagens utilizadas no jogo, as "sprites".

<br>

## 5) Ferramentas, bibliotecas, frameworks utilizados com as respectivas justificativas para o uso;  

- `pygame`: Utilizamos o pygame, pois ele fornece diversas ferramentas e recursos integrados para a criação dos jogos 2D. Além de sua facilidade de uso para a criação de jogos por iniciantes em programação.
  
- `pygame.mixer`: Contido dentro da biblioteca do pygame, o módulo .mixer é usado para carregar sons dentro do jogo, o que utilizamos para carregar o som principal do jogo.
  
- `time`: Utilizamos a biblioteca time para funções como medir o tempo de início do jogo e armazená-lo em uma variável para uso posterior, controlar a taxa de atualização da tela do jogo e para medir o tempo desde a última atualização e controlar o intervalo de tempo entre as atualizações do sprite do jogador. 

- `random`: A biblioteca random foi utilizada para gerar aleatoriamente os itens a serem coletados pelo jogador, como também os itens dos quais o jogador deve desviar.
  
- `sys`: Este módulo fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador. Sempre disponível.
<br>

## 6) A divisão de trabalho dentro do grupo (quem fez o que); 

`André`: Coletáveis e função de tempo

`Matheus`: Programação da main e debugando.

`Mateus`: Lógica e programação da bomba e player.

`Rodrigo`: 
 <br>   

## 7) Conceitos que foram apresentados durante a disciplina e utilizados no projeto (indicando onde foram usados);    

Programação orientada a objetos, condicionais, estruturas de repetição, funções, listas.

Usamos POO, e seus 3 principais conceitos (encapsulamento, herança e polimorfismo) para definir entidades importantes do nosso jogo, como por exemplo o Player, a bomba, os elementos quebráveis e inquebráveis, etc. Dessa forma, conseguimos instaciar diversos elementos com caracteríscias e ações semelhantes. As funcionalidades das listas foram usadas principalmente para a organização do mapa do jogo, já que toda a distribuição dos elementos de tela foram distribuidos a partir de uma matriz. O conhecimento sobre funções também foi essencial para a construção dos métodos dessas classes, onde tentamos sempre usar funções para modificar propriedades das classes (encapsulamento).
Condicionais e estruturas de repetição foram usadas em diversas partes do código para limitar certas funcionalidades a certas situações, em geral, foram estruturas indispensáveis para a construção de toda a lógica do jogo.   
<br>

## 8) Os desafios e erros enfrentados no decorrer do projeto e as lições aprendidas. 

Nosso principal desafio foi abstrair nossa imaginação em códigos, utilizando pygame e paradigma de orientação a objeto sem ter experiência. Nosso principal erro foi relacionado ao mapa. Fizemos boa parte do jogo e no fim, percebemos que teríamos que modificar tudo, para uma estrutura em matriz, nos empenhamos e conseguimos voltar ao estado anterior em apenas 2 dias, mesmo tendo que refazer praticamente todo o código. Sobre lições aprendidas, a principal foi sobre a importância de uma base teórica e de pesquisa. Nosso principal erro seria evitado, caso houvesse uma pesquisa prévia acerca da forma de criação de mapas para jogos como o nosso.
 <br>

## 9) Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele? 

Não diríamos um erro em si, mas a organização e distribuição de tarefas de acordo com o tempo que tinhamos para desenvolver o projeto e com a quantidade de tarefas a serem distribuídas para as pessoas do grupo, o que gerou um pouco de atrasos no andamento inicial do projeto. Tentamos distribuir as tarefas de acordo com a disponibilidade de cada um e nos ajudamos quando alguma tarefa do projeto estava pendente. 

<br>

## 10) Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele? 

De início, estávamos seguindo com uma estruturação um pouco mais complicada para a organização do mapa do jogo, o que fez com que estivéssemos caminhando para algo mais complexo do que poderíamos ir pelo prazo estabelecido. Ao conversar com os integrantes e com o professor, estruturamos melhor o código. Dessa forma, caminhou de uma maneira mais fácil de lidar com as modularizações do código.

Outro ponto foi estruturar o código em POO. Assistimos vários vídeos no youtube que pudessem nos ajudar com a refatoração do código e também conversávamos entre nós para implementar o código da melhor forma possível. 

<br>        

## 11) Quais as lições aprendidas durante o projeto? 

- É muito importante planejar um projeto com antecedência, dividir nosso projeto em sprints e tarefas de cada pessoa foi muito importante para que pudéssemos concluir o projeto no prazo determinado.  

- A comunicação é indispensável em trabalhos em equipe e projetos como esse, então nos comunicávamos diariamente para saber como estava o andamento do projeto e se iríamos conseguir as tarefas das sprints no prazo. 

- Todo mundo tem algo a ensinar e algo a aprender. No processo de construção do jogo pudemos trocar muito conhecimento entre nós a respeito das ferramentas que utilizamos nesse projeto. 

- Aprender a identificar e corrigir os erros do código é crucial para o desenvolvimento do jogo e andamento do projeto. 

- Aprender a escutar a opinião dos outros e implementar aquilo em seu código é importante para melhorar o jogo e tornar a experiência a melhor possível para o usuário final. 

- Colaborar com outros programadores compartilhando códigos e ideias desenvolve habilidades muito importantes para os desenvolvedores. 

- É importante ter paciência e persistência para superar os obstáculos e dificuldades que possam surgir no processo de criação do projeto.  

- A principal e mais importante foi o verdadeiro trabalho em equipe, pois se não programássemos em conjunto, o projeto não daria certo. 

 <br>
 <br>

## 12) Capturas de tela do sistema funcionando para compor a galeria de projetos 
<br>

### <p align="center">Tela Inicial </p>
<p align="center">
  <img alt="Banner menu" src="/assets/Teladojogo.png" width="80%">
</p>

<br>
<br>

### <p align="center">Tela de Game Over </p>
<p align="center">
  <img alt="Banner gameover" src="/assets/TeladoGanhador.png" width="80%">
</p>
