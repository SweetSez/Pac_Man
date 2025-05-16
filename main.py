import pygame
import sys
import random
import math

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мини-Пакмэн")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Игрок
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Еда (шарики)
food_radius = 10
foods = []
for _ in range(20):
    fx = random.randint(food_radius, WIDTH - food_radius)
    fy = random.randint(food_radius, HEIGHT - food_radius)
    foods.append([fx, fy])

# Главный цикл
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Проверка столкновения с едой
    player_center = (player_x + player_size // 2, player_y + player_size // 2)
    new_foods = []
    for fx, fy in foods:
        distance = math.hypot(player_center[0] - fx, player_center[1] - fy)
        if distance > food_radius + player_size // 2:
            new_foods.append([fx, fy])
    foods = new_foods

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    for fx, fy in foods:
        pygame.draw.circle(screen, RED, (fx, fy), food_radius)
    pygame.display.flip()

# Завершение
pygame.quit()
sys.exit()