import pygame
import sys
import math

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
LARGURA_TELA, ALTURA_TELA = 800, 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("bounce")

# Definir as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Configurações da bola
raio_bola = 20
x_bola, y_bola = LARGURA_TELA // 2, ALTURA_TELA // 2
velocidade_x_bola, velocidade_y_bola = 5, 5
fator_aumento_velocidade = 5  # Fator de aumento da velocidade a cada toque

# Configurações do jogador
largura_jogador, altura_jogador = 700, 30
x_jogador, y_jogador = (LARGURA_TELA - largura_jogador) // 2, ALTURA_TELA - altura_jogador - 10
velocidade_jogador = 50

# Configurações do adversário
largura_adversario, altura_adversario = 700, 30
x_adversario, y_adversario = (LARGURA_TELA - largura_adversario) // 2, 10
velocidade_adversario = 50

# Placar
placar_jogador = 0
placar_adversario = 0
fonte = pygame.font.Font(None, 36)

# Configurações do relógio
clock = pygame.time.Clock()
FPS = 60


# Função para desenhar o placar na tela
def desenhar_placar():
    texto_jogador = fonte.render(f"Adversário: {placar_adversario}", True, BRANCO)
    texto_adversario = fonte.render(f"Jogador: {placar_jogador}", True, BRANCO)
    tela.blit(texto_jogador, (10, 10))
    tela.blit(texto_adversario, (LARGURA_TELA - texto_adversario.get_width() - 10, 10))


# Função para calcular o ângulo de deflexão da bola
def defletir_bola(x_contato, x_raquete, largura_raquete):
    centro_raquete = x_raquete + largura_raquete / 2
    distancia_centro = x_contato - centro_raquete
    max_deflexao = math.radians(45)
    fator_deflexao = distancia_centro / (largura_raquete / 2)
    angulo = fator_deflexao * max_deflexao
    return angulo


# Função para verificar colisão usando interpolação de movimento
def verificar_colisao_bola(raquete_x, raquete_y, largura_raquete, altura_raquete):
    global x_bola, y_bola, velocidade_x_bola, velocidade_y_bola

    # Simular a trajetória da bola entre dois frames
    next_x_bola = x_bola + velocidade_x_bola
    next_y_bola = y_bola + velocidade_y_bola

    # Verificar colisão horizontal e vertical
    if ((raquete_x < x_bola < raquete_x + largura_raquete or raquete_x < next_x_bola < raquete_x + largura_raquete) and
            (raquete_y < y_bola < raquete_y + altura_raquete or raquete_y < next_y_bola < raquete_y + altura_raquete)):
        return True
    return False


# Loop principal do jogo
while True:
    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar a posição da bola
    x_bola += velocidade_x_bola
    y_bola += velocidade_y_bola

    # Verificar colisões com as bordas da tela
    if x_bola - raio_bola < 0 or x_bola + raio_bola > LARGURA_TELA:
        velocidade_x_bola = -velocidade_x_bola

    if y_bola - raio_bola < 0:
        placar_jogador += 1
        x_bola, y_bola = LARGURA_TELA // 2, ALTURA_TELA // 2
        velocidade_x_bola, velocidade_y_bola = 5, 5  # Resetar velocidades

    if y_bola + raio_bola > ALTURA_TELA:
        placar_adversario += 1
        x_bola, y_bola = LARGURA_TELA // 2, ALTURA_TELA // 2
        velocidade_x_bola, velocidade_y_bola = 5, 5  # Resetar velocidades

    # Verificar colisão da bola com o jogador
    if verificar_colisao_bola(x_jogador, y_jogador, largura_jogador, altura_jogador):
        angulo = defletir_bola(x_bola, x_jogador, largura_jogador)
        velocidade_x_bola = 5 * math.sin(angulo)
        velocidade_y_bola = -5 * math.cos(angulo)

        # Aumentar a velocidade a cada toque
        velocidade_x_bola *= fator_aumento_velocidade
        velocidade_y_bola *= fator_aumento_velocidade

    # Verificar colisão da bola com o adversário
    if verificar_colisao_bola(x_adversario, y_adversario, largura_adversario, altura_adversario):
        angulo = defletir_bola(x_bola, x_adversario, largura_adversario)
        velocidade_x_bola = 5 * math.sin(angulo)
        velocidade_y_bola = 5 * math.cos(angulo)

        # Aumentar a velocidade a cada toque
        velocidade_x_bola *= fator_aumento_velocidade
        velocidade_y_bola *= fator_aumento_velocidade

    # Mover o adversário para seguir a bola
    if x_bola < x_adversario + largura_adversario / 2:
        x_adversario -= velocidade_adversario
    if x_bola > x_adversario + largura_adversario / 2:
        x_adversario += velocidade_adversario

    # Mover o jogador (também automaticamente) para seguir a bola
    if x_bola < x_jogador + largura_jogador / 2:
        x_jogador -= velocidade_jogador
    if x_bola > x_jogador + largura_jogador / 2:
        x_jogador += velocidade_jogador

    # Manter o jogador e o adversário dentro da tela
    x_jogador = max(0, min(LARGURA_TELA - largura_jogador, x_jogador))
    x_adversario = max(0, min(LARGURA_TELA - largura_adversario, x_adversario))

    # Preencher a tela com a cor preta
    tela.fill(PRETO)

    # Desenhar a bola
    pygame.draw.circle(tela, BRANCO, (x_bola, y_bola), raio_bola)

    # Desenhar o jogador
    pygame.draw.rect(tela, BRANCO, (x_jogador, y_jogador, largura_jogador, altura_jogador))

    # Desenhar o adversário
    pygame.draw.rect(tela, VERDE, (x_adversario, y_adversario, largura_adversario, altura_adversario))

    # Desenhar o placar
    desenhar_placar()

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização
    clock.tick(FPS)
