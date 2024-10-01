import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definindo as constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 30
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_SPEED = 7
ENEMY_SPEED = 3

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configurando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Função para desenhar o jogador
# Função para desenhar o jogador como um triângulo
def draw_player(x, y):
    pygame.draw.polygon(screen, WHITE, [
        (x + PLAYER_WIDTH // 2, y),  # Ponto superior do triângulo
        (x, y + PLAYER_HEIGHT),       # Ponto inferior esquerdo
        (x + PLAYER_WIDTH, y + PLAYER_HEIGHT)  # Ponto inferior direito
    ])


# Função para desenhar os inimigos
def draw_enemy(x, y):
    pygame.draw.polygon(screen, RED, [
        (x, y + ENEMY_HEIGHT),
        (x + ENEMY_WIDTH // 2, y),
        (x + ENEMY_WIDTH, y + ENEMY_HEIGHT)
    ])

# Função para desenhar a bala
def draw_bullet(x, y):
    pygame.draw.rect(screen, GREEN, [x, y, BULLET_WIDTH, BULLET_HEIGHT])

# Tela de "Continue"
def show_continue_screen(score):
    font = pygame.font.SysFont(None, 55)
    text = font.render(f"Score: {score} - Pressione 'C' para continuar", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    waiting = False

# Gera novos inimigos
def create_enemies(num_enemies):
    enemies = []
    for _ in range(num_enemies):
        enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        enemy_y = random.randint(50, 150)
        enemies.append([enemy_x, enemy_y])
    return enemies

# Loop principal do jogo
def game_loop():
    global ENEMY_DIRECTION  # Declare ENEMY_DIRECTION como global
    ENEMY_DIRECTION = 1    # 1 = direita, -1 = esquerda

    running = True

    while running:
        player_x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
        enemies = create_enemies(5)
        player_bullets = []
        enemy_bullets = []
        clock = pygame.time.Clock()
        score = 0
        player_hits = 0  # Contador de acertos no jogador
        game_active = True  # Flag para o estado do jogo

        while game_active:
            screen.fill(BLACK)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_active = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= 5
            if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_WIDTH:
                player_x += 5
            if keys[pygame.K_SPACE]:
                player_bullets.append([player_x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, player_y])

            # Atualizando inimigos e suas balas
            for enemy in enemies[:]:
                enemy[0] += ENEMY_SPEED * ENEMY_DIRECTION
                if enemy[0] < 0 or enemy[0] > SCREEN_WIDTH - ENEMY_WIDTH:
                    ENEMY_DIRECTION *= -1
                    for e in enemies:
                        e[1] += 10  # Mover todos os inimigos para baixo
                    break

                # Lógica para inimigos atirarem
                if random.random() < 0.02:  # Chance de um inimigo atirar
                    enemy_bullets.append([enemy[0] + ENEMY_WIDTH // 2 - BULLET_WIDTH // 2, enemy[1] + ENEMY_HEIGHT])

            # Atualizando balas do jogador
            for bullet in player_bullets[:]:
                bullet[1] -= BULLET_SPEED
                if bullet[1] < 0:
                    player_bullets.remove(bullet)

            # Atualizando balas dos inimigos
            for bullet in enemy_bullets[:]:
                bullet[1] += BULLET_SPEED
                if bullet[1] > SCREEN_HEIGHT:
                    enemy_bullets.remove(bullet)

            # Verificando colisões
            for bullet in player_bullets[:]:
                for enemy in enemies[:]:
                    if (bullet[0] + BULLET_WIDTH > enemy[0] and
                        bullet[0] < enemy[0] + ENEMY_WIDTH and
                        bullet[1] + BULLET_HEIGHT > enemy[1] and
                        bullet[1] < enemy[1] + ENEMY_HEIGHT):
                        player_bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 1
                        break

            # Verificando colisões do jogador com as balas inimigas
            for bullet in enemy_bullets[:]:
                if (bullet[0] + BULLET_WIDTH > player_x and
                    bullet[0] < player_x + PLAYER_WIDTH and
                    bullet[1] + BULLET_HEIGHT > player_y and
                    bullet[1] < player_y + PLAYER_HEIGHT):
                    player_hits += 1
                    enemy_bullets.remove(bullet)
                    if player_hits >= 3:
                        show_continue_screen(score)
                        game_active = False  # O jogador é atingido 3 vezes

            # Verificando se todos os inimigos foram derrotados
            if not enemies:
                enemies = create_enemies(5)  # Criar novos inimigos se todos foram derrotados

            # Desenhando o jogador, inimigos e balas
            draw_player(player_x, player_y)
            for enemy in enemies:
                draw_enemy(enemy[0], enemy[1])
            for bullet in player_bullets:
                draw_bullet(bullet[0], bullet[1])
            for bullet in enemy_bullets:
                draw_bullet(bullet[0], bullet[1])

            # Mostrando o placar e número de acertos
            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f"Score: {score}", True, WHITE)
            hits_text = font.render(f"Hits: {player_hits}/3", True, WHITE)
            screen.blit(score_text, (10, 10))
            screen.blit(hits_text, (10, 40))

            # Atualizando a tela
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()

# Executa o jogo
game_loop()
