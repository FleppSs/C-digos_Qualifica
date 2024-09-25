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
AZUL = (0, 0, 255)

# Configurações da bola
raio_bola = 20
x_bola, y_bola = LARGURA_TELA // 2, ALTURA_TELA // 2
velocidade_x_bola, velocidade_y_bola = 5, 5

# Configurações do jogador
largura_jogador, altura_jogador = 100, 20
x_jogador, y_jogador = (LARGURA_TELA - largura_jogador) // 2, ALTURA_TELA - altura_jogador - 10
velocidade_jogador = 10

# Configurações do adversário
largura_adversario, altura_adversario = 100, 20
x_adversario, y_adversario = (LARGURA_TELA - largura_adversario) // 2, 10
velocidade_adversario = 2.8

# Placar
placar_jogador = 0
placar_adversario = 0
fonte = pygame.font.Font(None, 36)

# Configurações do relógio
clock = pygame.time.Clock()
FPS = 60


# Função para desenhar o placar na tela
def desenhar_placar():
    texto_jogador = fonte.render(f"Adversário: {placar_jogador}", True, BRANCO)
    texto_adversario = fonte.render(f"Jogador: {placar_adversario}", True, BRANCO)
    tela.blit(texto_jogador, (10, 10))
    tela.blit(texto_adversario, (LARGURA_TELA - texto_adversario.get_width() - 10, 10))


# Função para calcular o ângulo de deflexão da bola
def defletir_bola(x_contato, x_raquete, largura_raquete):
    centro_raquete = x_raquete + largura_raquete / 2
    distancia_centro = x_contato - centro_raquete
    # A deflexão máxima é de 45 graus (±π/4 radianos)
    max_deflexao = math.radians(45)
    fator_deflexao = distancia_centro / (largura_raquete / 2)
    angulo = fator_deflexao * max_deflexao
    return angulo


# Loop principal do jogo
while True:
    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obter o estado das teclas
    teclas = pygame.key.get_pressed()

    # Mover o jogador com as setas do teclado
    if teclas[pygame.K_LEFT]:
        x_jogador -= velocidade_jogador
    if teclas[pygame.K_RIGHT]:
        x_jogador += velocidade_jogador

    # Manter o jogador dentro da tela
    if x_jogador < 0:
        x_jogador = 0
    if x_jogador + largura_jogador > LARGURA_TELA:
        x_jogador = LARGURA_TELA - largura_jogador

    # Atualizar a posição da bola
    x_bola += velocidade_x_bola
    y_bola += velocidade_y_bola

    # Verificar colisões com as bordas da tela
    if x_bola - raio_bola < 0 or x_bola + raio_bola > LARGURA_TELA:
        velocidade_x_bola = -velocidade_x_bola

    if y_bola - raio_bola < 0:
        # Bola atingiu a parte superior (adversário ganha um ponto)
        placar_adversario += 1
        # Resetar a posição da bola
        x_bola, y_bola = LARGURA_TELA // 2, ALTURA_TELA // 2
        velocidade_x_bola, velocidade_y_bola = 5, 5

    if y_bola + raio_bola > ALTURA_TELA:
        # Bola caiu na parte inferior (jogador ganha um ponto)
        placar_jogador += 1
        # Resetar a posição da bola
        x_bola, y_bola = LARGURA_TELA // 2, ALTURA_TELA // 2
        velocidade_x_bola, velocidade_y_bola = 5, 5

    # Verificar colisão da bola com o jogador
    if (x_bola + raio_bola > x_jogador and x_bola - raio_bola < x_jogador + largura_jogador and
            y_bola + raio_bola > y_jogador and y_bola - raio_bola < y_jogador + altura_jogador):
        angulo = defletir_bola(x_bola, x_jogador, largura_jogador)
        velocidade_x_bola = 5 * math.sin(angulo)  # Ajusta a velocidade X com base no ângulo
        velocidade_y_bola = -5 * math.cos(angulo)  # Ajusta a velocidade Y com base no ângulo

        # Garantir que a bola não "teleporte" e só mude a direção
        if velocidade_x_bola == 0:
            velocidade_x_bola = 5 if x_bola > x_jogador + largura_jogador / 2 else -5

        if velocidade_y_bola == 0:
            velocidade_y_bola = -5

    # Verificar colisão da bola com o adversário
    if (x_bola + raio_bola > x_adversario and x_bola - raio_bola < x_adversario + largura_adversario and
            y_bola - raio_bola < y_adversario + altura_adversario and y_bola + raio_bola > y_adversario):
        angulo = defletir_bola(x_bola, x_adversario, largura_adversario)
        velocidade_x_bola = 5 * math.sin(angulo)  # Ajusta a velocidade X com base no ângulo
        velocidade_y_bola = 5 * math.cos(angulo)  # Ajusta a velocidade Y com base no ângulo

        # Garantir que a bola não "teleporte" e só mude a direção
        if velocidade_x_bola == 0:
            velocidade_x_bola = 5 if x_bola > x_adversario + largura_adversario / 2 else -5

        if velocidade_y_bola == 0:
            velocidade_y_bola = 5

    # Mover o adversário para seguir a bola
    if x_bola < x_adversario + largura_adversario / 2:
        x_adversario -= velocidade_adversario
    if x_bola > x_adversario + largura_adversario / 2:
        x_adversario += velocidade_adversario

    # Manter o adversário dentro da tela
    if x_adversario < 0:
        x_adversario = 0
    if x_adversario + largura_adversario > LARGURA_TELA:
        x_adversario = LARGURA_TELA - largura_adversario

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
