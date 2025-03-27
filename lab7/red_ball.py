import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font(None, 36)  

WHITE = (255, 255, 255)
RED = (255, 0, 0)

RADIUS = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
SPEED = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if ball_y - RADIUS - SPEED >= 0:
            ball_y -= SPEED
    if keys[pygame.K_DOWN]:
        if ball_y + RADIUS + SPEED <= HEIGHT:
            ball_y += SPEED
    if keys[pygame.K_LEFT]:
        if ball_x - RADIUS - SPEED >= 0:
            ball_x -= SPEED
    if keys[pygame.K_RIGHT]:
        if ball_x + RADIUS + SPEED <= WIDTH:
            ball_x += SPEED

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), RADIUS)
    pygame.display.flip()

    clock.tick(60)
