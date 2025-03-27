import pygame
import sys
import random

W = 800
H = 500


car = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/unnamed.png")
car_rect = car.get_rect(center=(W // 2, H // 2))

enemy = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/938z8l9w2ho51.png.webp")
enemy_rect = enemy.get_rect().size

screen = pygame.display.set_mode((W, H))


sprites = []

cordx = W // 2
cordy = H // 2

pygame.init()

screen = pygame.display.set_mode((800, 500))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))

    if random.random() < 0.02:
        x = random.randint(0, W - enemy_rect[0])  # Случайное место сверху
        y = -enemy_rect[1]  # Старт выше экрана
        speed = 5  # Случайная скорость падения
        sprites.append([x, y, speed])

    for sprite in sprites:
        sprite[1] += sprite[2]  # Двигаем вниз

    # Удаляем спрайты, если они выходят за нижний край
    sprites = [s for s in sprites if s[1] < H]

    # Рисуем спрайты
    for sprite in sprites:
        screen.blit(enemy, (sprite[0], sprite[1]))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if cordx < W | cordx > 0:
            cordx +=5
        else:
            cordx = W // 2
    if keys[pygame.K_LEFT]:
        if cordx <= W | cordx >= 0:
            cordx -= 5
        else:
            cordx = W // 2

    car_rect.clamp_ip(screen.get_rect())
    
    screen.blit(car, (cordx, cordy))

    
    pygame.display.flip()


