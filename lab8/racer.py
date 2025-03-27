import pygame
import sys
import random
import time

W = 300
H = 800


car = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/unnamed.png")
car = pygame.transform.scale(car, (100, 100))

enemy = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/938z8l9w2ho51.png.webp")
sprite_img = pygame.transform.scale(enemy, (100, 100))
sprite_size = sprite_img.get_rect().size

screen = pygame.display.set_mode((W, H))


sprites = []

cordx = 0
cordy = H - 100

pygame.init()

font = pygame.font.Font(None, 36)  

running = True

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))



    text = font.render(f"x {cordx}", True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(10, 10))

    screen.blit(text, text_rect)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and cordx <= 200:
        cordx += 1
    if keys[pygame.K_LEFT] and cordx >= 0:
        cordx -= 1


    if random.random() < 0.001:
        x = random.randint(0, 2)  # Случайное место сверху
        y = -sprite_size[1]  # Старт выше экрана
        speed = 1  # скорость падения
        sprites.append([x*100, y, speed])

    # Обновляем позиции спрайтов
    for sprite in sprites:
        sprite[1] += sprite[2]  # Двигаем вниз

    # Удаляем спрайты, если они выходят за нижний край
    sprites = [s for s in sprites if s[1] < H]

    # Рисуем спрайты
    for sprite in sprites:
        screen.blit(sprite_img, (sprite[0], sprite[1]))

    for sprite in sprites:
        if sprite[0] <= cordx <= sprite[0]+100 and sprite[1] <= cordy <= sprite[1]+100 or sprite[0] <= cordx+100 <= sprite[0]+100 and sprite[1] <= cordy+100 <= sprite[1]+100:
            print("Столкновение!")
            running = False
            sys.exit()


    screen.blit(car, (cordx, cordy))


    pygame.display.update()


