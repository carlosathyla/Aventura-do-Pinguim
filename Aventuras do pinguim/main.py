import pygame
import random
import time

# Inicializando o PyGame
pygame.init()
largura_tela, altura_tela = 1280, 720
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Aventura do Pinguim")

# Cores
BRANCO, PRETO, AZUL, VERDE, VERMELHO, AMARELO, LARANJA, CINZA = (255, 255, 255), (0, 0, 0), (0, 150, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 165, 0), (128, 128, 128)

# Definir o FPS (frames por segundo)
clock = pygame.time.Clock()
FPS = 60

# Função para carregar imagens
def carregar_imagem(caminho, tamanho):
    try:
        return pygame.transform.scale(pygame.image.load(caminho), tamanho)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        pygame.quit()
        exit()

# Carregar imagens
pinguim = carregar_imagem("C:/Projects/pingo.png", (100, 100))
fundo_nivel_1 = carregar_imagem("C:/Projects/fundoArtico.png", (largura_tela, altura_tela))
fundo_nivel_2 = carregar_imagem("C:/Projects/fundofloresta.png", (largura_tela, altura_tela))
fundo_nivel_3 = carregar_imagem("C:/Projects/fundoDeserto.png", (largura_tela, altura_tela))
fundo_menu = carregar_imagem("C:/Projects/fundoInicio.png", (largura_tela, altura_tela))
fundo_fim_jogo = carregar_imagem("C:/Projects/fundoFimJogo.png", (largura_tela, altura_tela))
fundo_vitoria = carregar_imagem("C:/Projects/fundoVitoria.png", (largura_tela, altura_tela))

largura_pinguim, altura_pinguim = 100, 100

# Função para desenhar o pinguim
def desenhar_pinguim(x, y):
    tela.blit(pinguim, (x, y))

# Função para criar obstáculos aleatórios
def criar_obstaculos(velocidade, nivel):
    largura, altura = random.randint(100, 200), random.randint(50, 100)
    return [largura_tela, altura_tela - altura - 20, largura, altura, velocidade, [PRETO, VERDE, VERMELHO, AMARELO][nivel]]

# Função para criar inimigos voadores (pássaros)
def criar_inimigo(velocidade, nivel):
    return [largura_tela, random.randint(50, 500), 50, 30, velocidade, [VERMELHO, LARANJA, CINZA, AMARELO][nivel]]

# Função para criar itens de bonificação de pontos
def criar_bonificacao():
    return [largura_tela, random.randint(100, altura_tela - 100), 30, 30, 'bonus']

# Função para exibir texto na tela
def mostrar_texto(texto, tamanho, cor, x, y, fundo=None):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor, fundo)
    tela.blit(texto_surface, (x, y))

# Função para exibir o menu inicial
def menu_inicial():
    opcoes = ["Iniciar Jogo", "Sair"]
    indice_selecionado = 0
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    indice_selecionado = (indice_selecionado - 1) % len(opcoes)
                elif evento.key == pygame.K_DOWN:
                    indice_selecionado = (indice_selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN:
                    if indice_selecionado == 0:
                        registrar_nome()
                    elif indice_selecionado == 1:
                        pygame.quit()
                        return

        tela.blit(fundo_menu, (0, 0))
        mostrar_texto("Aventura do Pinguim", 74, BRANCO, largura_tela // 2 - 200, altura_tela // 4, PRETO)
        for i, opcao in enumerate(opcoes):
            fundo = CINZA if i == indice_selecionado else None
            mostrar_texto(opcao, 50, BRANCO, largura_tela // 2 - 75, altura_tela // 2 + i * 60, fundo)
        
        pygame.display.update()
        clock.tick(FPS)

# Função para registrar o nome do jogador
def registrar_nome():
    nome_jogador = ""
    while True:
        tela.fill(AZUL)
        mostrar_texto("Digite seu nome:", 50, BRANCO, largura_tela // 2 - 150, altura_tela // 4, PRETO)
        mostrar_texto(nome_jogador, 50, BRANCO, largura_tela // 2 - 150, altura_tela // 2, PRETO)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome_jogador:
                    jogo(nome_jogador)
                    return
                elif evento.key == pygame.K_BACKSPACE:
                    nome_jogador = nome_jogador[:-1]
                else:
                    nome_jogador += evento.unicode

# Função principal do jogo
def jogo(nome_jogador):
    niveis = [
        {"tema": AZUL, "velocidade": 5, "nome": "Nível 1 - Ártico", "fundo": fundo_nivel_1},
        {"tema": VERDE, "velocidade": 7, "nome": "Nível 2 - Floresta", "fundo": fundo_nivel_2},
        {"tema": VERMELHO, "velocidade": 9, "nome": "Nível 3 - Deserto", "fundo": fundo_nivel_3}
    ]
    nivel_atual, velocidade_y, gravidade, vidas, pulos_restantes, invulneravel = 0, 0, 0.5, 3, 3, False
    tempo_invulneravel, pontos, tempo_inicio = 0, 0, time.time()
    x_pinguim, y_pinguim = 100, altura_tela - altura_pinguim - 20
    obstaculos = [criar_obstaculos(niveis[nivel_atual]["velocidade"], nivel_atual)]
    inimigos = [criar_inimigo(3, nivel_atual)]
    bonificacoes = [criar_bonificacao()]
    jogando, fim_de_jogo = True, False
    
    while jogando:
        tempo_jogado = int(time.time() - tempo_inicio)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            if evento.type == pygame.KEYDOWN and not fim_de_jogo:
                if evento.key == pygame.K_SPACE and pulos_restantes > 0:
                    velocidade_y = -15
                    pulos_restantes -= 1
                if evento.key == pygame.K_ESCAPE:
                    pausar_jogo()

        if not fim_de_jogo:
            velocidade_y += gravidade
            y_pinguim += velocidade_y
            if y_pinguim > altura_tela - altura_pinguim - 20:
                y_pinguim = altura_tela - altura_pinguim - 20
                pulos_restantes = 3
            tela.blit(niveis[nivel_atual]["fundo"], (0, 0))
            if not invulneravel or int(time.time() * 10) % 2 == 0:
                desenhar_pinguim(x_pinguim, y_pinguim)
            for obstaculo in obstaculos:
                obstaculo[0] -= obstaculo[4]
                pygame.draw.rect(tela, obstaculo[5], obstaculo[:4])

                # Verificação de colisão
                if not invulneravel and (
                    x_pinguim < obstaculo[0] + obstaculo[2] and
                    x_pinguim + largura_pinguim > obstaculo[0] and
                    y_pinguim < obstaculo[1] + obstaculo[3] and
                    y_pinguim + altura_pinguim > obstaculo[1]
                ):
                    vidas -= 1
                    if vidas <= 0:
                        fim_de_jogo = True
                    invulneravel = True
                    tempo_invulneravel = time.time()
                if obstaculo[0] < -obstaculo[2]:
                    obstaculos.remove(obstaculo)
                    obstaculos.append(criar_obstaculos(niveis[nivel_atual]["velocidade"], nivel_atual))
                    pontos += 10
            for inimigo in inimigos:
                inimigo[0] -= inimigo[4]
                pygame.draw.rect(tela, inimigo[5], inimigo[:4])
                if not invulneravel and (
                    x_pinguim < inimigo[0] + inimigo[2] and
                    x_pinguim + largura_pinguim > inimigo[0] and
                    y_pinguim < inimigo[1] + inimigo[3] and
                    y_pinguim + altura_pinguim > inimigo[1]
                ):
                    vidas -= 1
                    if vidas <= 0:
                        fim_de_jogo = True
                    invulneravel = True
                    tempo_invulneravel = time.time()
                if inimigo[0] < -inimigo[2]:
                    inimigos.remove(inimigo)
                    inimigos.append(criar_inimigo(3, nivel_atual))
            for bonificacao in bonificacoes:
                bonificacao[0] -= 5
                if int(time.time() * 10) % 2 == 0:
                    pygame.draw.ellipse(tela, AMARELO, bonificacao[:4])
                if (x_pinguim < bonificacao[0] + bonificacao[2] and
                    x_pinguim + largura_pinguim > bonificacao[0] and
                    y_pinguim < bonificacao[1] + bonificacao[3] and
                    y_pinguim + altura_pinguim > bonificacao[1]
                ):
                    pontos += 50
                    bonificacoes.remove(bonificacao)
                    bonificacoes.append(criar_bonificacao())
                if bonificacao[0] < -bonificacao[2]:
                    bonificacoes.remove(bonificacao)
                    bonificacoes.append(criar_bonificacao())
            if invulneravel and (time.time() - tempo_invulneravel > 3):
                invulneravel = False
            if pontos >= 1200:
                fim_de_jogo = True
                tela.blit(fundo_vitoria, (0, 0))
                mostrar_texto("Parabéns! Você venceu!", 74, VERMELHO, largura_tela // 2 - 250, altura_tela // 4, PRETO)
                mostrar_texto(f"Pontos: {pontos}", 50, PRETO, largura_tela // 2 - 100, altura_tela // 2, PRETO)
                pygame.display.update()
                time.sleep(5)
                return
            if nivel_atual == 0 and pontos >= 300:
                nivel_atual += 1
                vidas += 1  # Concede uma vida extra ao passar de nível
            elif nivel_atual == 1 and pontos >= 800:
                nivel_atual += 1
                vidas += 1
        else:
            # Menu de Fim de Jogo
            opcoes_fim = ["Jogar Novamente", "Voltar ao Menu"]
            indice_selecionado = 0
            while True:
                tela.blit(fundo_fim_jogo, (0, 0))  # Fundo do fim de jogo
                if int(time.time() * 5) % 2 == 0:
                    mostrar_texto("FIM DE JOGO", 144, VERMELHO, largura_tela // 2 - 300, altura_tela // 4, PRETO)
                    
                for i, opcao in enumerate(opcoes_fim):
                    fundo = CINZA if i == indice_selecionado else None
                    mostrar_texto(opcao, 50, BRANCO, largura_tela // 2 - 150, altura_tela // 2 + i * 60, fundo)
                
                pygame.display.update()
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        return
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_UP:
                            indice_selecionado = (indice_selecionado - 1) % len(opcoes_fim)
                        elif evento.key == pygame.K_DOWN:
                            indice_selecionado = (indice_selecionado + 1) % len(opcoes_fim)
                        elif evento.key == pygame.K_RETURN:
                            if indice_selecionado == 0:
                                jogo(nome_jogador)
                                return
                            elif indice_selecionado == 1:
                                menu_inicial()
                                return

        pygame.draw.rect(tela, PRETO, (5, 5, 250, 180), border_radius=5)
        mostrar_texto(f"Pontuação: {pontos}", 36, BRANCO, 10, 10, PRETO)
        mostrar_texto(f"Tempo: {tempo_jogado}s", 36, BRANCO, 10, 50, PRETO)
        mostrar_texto(niveis[nivel_atual]["nome"], 36, BRANCO, 10, 90, PRETO)
        mostrar_texto(f"Vidas: {vidas}", 36, BRANCO, 10, 130, PRETO)
        pygame.display.update()
        clock.tick(FPS)

    menu_inicial()

# Função para pausar o jogo
def pausar_jogo():
    pausado = True
    opcoes_pausa = ["Continuar", "Voltar ao Menu"]
    indice_selecionado = 0
    while pausado:
        tela.fill(PRETO)
        mostrar_texto("PAUSADO", 74, BRANCO, largura_tela // 2 - 150, altura_tela // 4, PRETO)
        for i, opcao in enumerate(opcoes_pausa):
            fundo = CINZA if i == indice_selecionado else None
            mostrar_texto(opcao, 50, BRANCO, largura_tela // 2 - 150, altura_tela // 2 + i * 60, fundo)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    indice_selecionado = (indice_selecionado - 1) % len(opcoes_pausa)
                elif evento.key == pygame.K_DOWN:
                    indice_selecionado = (indice_selecionado + 1) % len(opcoes_pausa)
                elif evento.key == pygame.K_RETURN:
                    if indice_selecionado == 0:
                        pausado = False
                    elif indice_selecionado == 1:
                        menu_inicial()

menu_inicial()
pygame.quit()