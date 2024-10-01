import pygame
import random
import sys

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
LARGURA_TELA, ALTURA_TELA = 800, 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Adicionar Bolas")

# Definir as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Configurações da bola
raio_bola = 20
velocidade_bola_min = 3
velocidade_bola_max = 9

# Configurações do botão
largura_botao, altura_botao = 200, 50
x_botao, y_botao = (LARGURA_TELA - largura_botao) // 2, ALTURA_TELA - altura_botao - 20
cor_botao = AZUL
fonte = pygame.font.Font(None, 36)

# Lista de bolas
bolas = []

# Relógio para controlar FPS
clock = pygame.time.Clock()

# Função para criar uma bola nova com velocidade aleatória e direção aleatória
def criar_bola():
    x_bola = random.randint(raio_bola, LARGURA_TELA - raio_bola)
    y_bola = random.randint(raio_bola, ALTURA_TELA - raio_bola)
    velocidade_x_bola = random.choice([-1, 1]) * random.uniform(velocidade_bola_min, velocidade_bola_max)
    velocidade_y_bola = random.choice([-1, 1]) * random.uniform(velocidade_bola_min, velocidade_bola_max)
    return {"x": x_bola, "y": y_bola, "velocidade_x": velocidade_x_bola, "velocidade_y": velocidade_y_bola}

# Função para desenhar o botão
def desenhar_botao():
    pygame.draw.rect(tela, cor_botao, (x_botao, y_botao, largura_botao, altura_botao))
    texto_botao = fonte.render("Adicionar Bola", True, BRANCO)
    tela.blit(texto_botao, (x_botao + (largura_botao - texto_botao.get_width()) // 2,
                            y_botao + (altura_botao - texto_botao.get_height()) // 2))

# Função para mover as bolas e fazê-las quicar nas bordas
def mover_bolas():
    for bola in bolas:
        bola["x"] += bola["velocidade_x"]
        bola["y"] += bola["velocidade_y"]

        # Verificar colisões com as bordas da tela
        if bola["x"] - raio_bola < 0 or bola["x"] + raio_bola > LARGURA_TELA:
            bola["velocidade_x"] *= -1
        if bola["y"] - raio_bola < 0 or bola["y"] + raio_bola > ALTURA_TELA:
            bola["velocidade_y"] *= -1

# Função para desenhar as bolas
def desenhar_bolas():
    for bola in bolas:
        pygame.draw.circle(tela, BRANCO, (int(bola["x"]), int(bola["y"])), raio_bola)

# Loop principal do jogo
while True:
    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = evento.pos
            # Verificar se o botão foi clicado
            if x_botao <= mouse_x <= x_botao + largura_botao and y_botao <= mouse_y <= y_botao + altura_botao:
                bolas.append(criar_bola())  # Adicionar uma nova bola

    # Mover e atualizar as bolas
    mover_bolas()

    # Preencher a tela com a cor preta
    tela.fill(PRETO)

    # Desenhar as bolas
    desenhar_bolas()

    # Desenhar o botão
    desenhar_botao()

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização
    clock.tick(60)
