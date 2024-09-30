# Aventura do Pinguim

## Descrição do Projeto

"Aventura do Pinguim" é um jogo de plataforma desenvolvido em Python utilizando a biblioteca Pygame. O jogador controla um pinguim que deve navegar por vários níveis, evitando obstáculos e inimigos, enquanto coleta itens de bonificação para aumentar sua pontuação. O objetivo do jogo é completar os níveis e alcançar uma pontuação alta.

## Funcionalidades

- **Menus**: O jogo apresenta um menu inicial onde o jogador pode iniciar o jogo ou sair.
- **Múltiplos Níveis**: O jogo possui 3 níveis diferentes, cada um com um tema e dificuldade progressiva.
- **Inimigos e Obstáculos**: Inimigos voadores e obstáculos são gerados aleatoriamente, aumentando a dificuldade.
- **Itens de Bonificação**: O jogador pode coletar itens que aumentam sua pontuação.
- **Sistema de Vidas**: O jogador tem um número limitado de vidas e pode perder vidas ao colidir com inimigos ou obstáculos.
- **Pontos e Vencer**: O jogador vence ao atingir uma pontuação específica.

## Requisitos de Sistema

- Python 3.x
- Biblioteca PyGame

## Instalação

1. Instale o Python 3.x a partir do [site oficial do Python](https://www.python.org/).
2. Instale a biblioteca PyGame executando o seguinte comando no terminal ou prompt de comando:
 
   pip install pygame
   
## Como Jogar

1. Clone o repositório:
   bash
   git clone https://github.com/carlosathyla/Aventura-do-Pinguim.git
   
   
2. Navegue até o diretório do projeto:
   bash
   cd Aventura_do_Pinguim
   

3. Execute o jogo:
   bash
   python main.py

- *Iniciar Jogo:* Selecione "Iniciar Jogo" no menu principal.
- *Controles:*
  - *Espaço:* Pular (pode pular até 3 vezes consecutivamente)
  - *ESC:* Pausar o jogo
- *Objetivo:* Evite obstáculos e inimigos enquanto coleta bônus de pontuação. Ganhe uma vida extra ao passar de nível (a cada 300 pontos). O jogo é vencido ao atingir 1500 pontos.

## Estrutura do Código

O código é organizado em várias funções personalizadas que encapsulam a lógica do jogo:

- `carregar_imagem(caminho, tamanho)`: Carrega e redimensiona imagens.
- `desenhar_pinguim(x, y)`: Desenha o pinguim na tela.
- `criar_obstaculos(velocidade, nivel)`: Cria obstáculos aleatórios.
- `criar_inimigo(velocidade, nivel)`: Cria inimigos voadores.
- `criar_bonificacao()`: Cria itens de bonificação.
- `mostrar_texto(texto, tamanho, cor, x, y, fundo=None)`: Exibe texto na tela.
- `menu_inicial()`: Exibe o menu inicial do jogo.
- `jogo()`: Lógica principal do jogo.
- `pausar_jogo()`: Pausa o jogo e exibe opções.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Créditos

Jogo desenvolvido por Carlos Athyla.

Ano: 2024
