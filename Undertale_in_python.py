import pygame
import random

# Inicializar o pygame
pygame.init()

# Configurações da tela
largura, altura = 640, 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Undertale - Python Edition")

# Configurações do quadrado vermelho
quadrado_tam = 20
quadrado_x = largura // 2 - quadrado_tam // 2
quadrado_y = altura // 2 - quadrado_tam // 2
velocidade = 5

# Configurações dos ícones brancos
icone_tam = 30
icones = []
icone_velocidade = 6

# Configurações da vida
vida_maxima = 100
vida_atual = vida_maxima
barra_vida_largura = 200
barra_vida_altura = 20

# Adicionar bordas brancas
bordas_largura = 10

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Controle de FPS
clock = pygame.time.Clock()


# Função para criar novos ícones
def criar_icone():
    direcao = random.choice(['esquerda', 'direita', 'cima', 'baixo'])
    if direcao == 'esquerda':
        x = largura
        y = random.randint(0, altura - icone_tam)
    elif direcao == 'direita':
        x = -icone_tam
        y = random.randint(0, altura - icone_tam)
    elif direcao == 'cima':
        x = random.randint(0, largura - icone_tam)
        y = altura
    elif direcao == 'baixo':
        x = random.randint(0, largura - icone_tam)
        y = -icone_tam
    icones.append([x, y, direcao])


# Função para movimentar ícones
def mover_icones():
    global vida_atual
    for icone in icones:
        if icone[2] == 'esquerda':
            icone[0] -= icone_velocidade
        elif icone[2] == 'direita':
            icone[0] += icone_velocidade
        elif icone[2] == 'cima':
            icone[1] -= icone_velocidade
        elif icone[2] == 'baixo':
            icone[1] += icone_velocidade

        # Verificar colisão com o quadrado vermelho
        if (icone[0] < quadrado_x + quadrado_tam and
                icone[0] + icone_tam > quadrado_x and
                icone[1] < quadrado_y + quadrado_tam and
                icone[1] + icone_tam > quadrado_y):
            # Reduzir vida e remover o ícone
            vida_atual -= 10
            icones.remove(icone)
            if vida_atual <= 0:
                return True  # Indicar que o jogo deve reiniciar

    return False


# Função para desenhar a barra de vida
def desenhar_barra_vida():
    vida_percentual = vida_atual / vida_maxima
    pygame.draw.rect(tela, vermelho,
                     (largura // 2 - barra_vida_largura // 2, 10, barra_vida_largura, barra_vida_altura))
    pygame.draw.rect(tela, verde, (
    largura // 2 - barra_vida_largura // 2, 10, barra_vida_largura * vida_percentual, barra_vida_altura))


# Função para desenhar a tela de game over
def tela_game_over():
    fonte_grande = pygame.font.Font(None, 74)
    fonte_pequena = pygame.font.Font(None, 36)
    texto_game_over = fonte_grande.render("GAME OVER", True, branco)
    texto_determinacao = fonte_pequena.render("Não desista! Tenha DETERMINAÇÃO!", True, branco)

    texto_rect_game_over = texto_game_over.get_rect(center=(largura // 2, altura // 2 - 20))
    texto_rect_determinacao = texto_determinacao.get_rect(center=(largura // 2, altura // 2 + 40))

    tela.fill(preto)
    tela.blit(texto_game_over, texto_rect_game_over)
    tela.blit(texto_determinacao, texto_rect_determinacao)
    pygame.display.flip()
    pygame.time.wait(2000)  # Esperar 2 segundos para o jogador ver a tela de game over


# Função para reiniciar o jogo
def reiniciar_jogo():
    global quadrado_x, quadrado_y, vida_atual, icones
    quadrado_x = largura // 2 - quadrado_tam // 2
    quadrado_y = altura // 2 - quadrado_tam // 2
    vida_atual = vida_maxima
    icones = []


# Loop principal do jogo
jogando = True
while True:
    # Eventos de saída
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Movimentação do quadrado vermelho
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and quadrado_x > bordas_largura:
        quadrado_x -= velocidade
    if teclas[pygame.K_RIGHT] and quadrado_x < largura - quadrado_tam - bordas_largura:
        quadrado_x += velocidade
    if teclas[pygame.K_UP] and quadrado_y > bordas_largura:
        quadrado_y -= velocidade
    if teclas[pygame.K_DOWN] and quadrado_y < altura - quadrado_tam - bordas_largura:
        quadrado_y += velocidade

    # Criar novos ícones
    if random.randint(0, 50) < 2:
        criar_icone()

    # Movimentar ícones e verificar colisões
    jogo_reiniciar = mover_icones()

    # Desenhar o fundo e as bordas
    tela.fill(preto)
    pygame.draw.rect(tela, branco, (0, 0, largura, bordas_largura))  # Topo
    pygame.draw.rect(tela, branco, (0, altura - bordas_largura, largura, bordas_largura))  # Fundo
    pygame.draw.rect(tela, branco, (0, 0, bordas_largura, altura))  # Esquerda
    pygame.draw.rect(tela, branco, (largura - bordas_largura, 0, bordas_largura, altura))  # Direita

    # Desenhar o quadrado vermelho
    pygame.draw.rect(tela, vermelho, (quadrado_x, quadrado_y, quadrado_tam, quadrado_tam))

    # Desenhar os ícones brancos
    for icone in icones:
        pygame.draw.rect(tela, branco, (icone[0], icone[1], icone_tam, icone_tam))

    # Desenhar a barra de vida
    desenhar_barra_vida()

    # Atualizar a tela
    pygame.display.flip()

    # Verificar se o jogo deve reiniciar
    if jogo_reiniciar:
        tela_game_over()
        pygame.time.wait(1000)  # Esperar 1 segundo antes de reiniciar
        reiniciar_jogo()

    # Controle de FPS
    clock.tick(60)
