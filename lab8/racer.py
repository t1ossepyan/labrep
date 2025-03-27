import pygame
import sys
import random


W = 300
H = 800


car = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/unnamed.png")
car = pygame.transform.scale(car, (100, 100))

score = 0

enemy = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/938z8l9w2ho51.png.webp")
sprite_img = pygame.transform.scale(enemy, (100, 100))
sprite_size = sprite_img.get_rect().size

screen = pygame.display.set_mode((W, H))

bg = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/New Project-2.png")

coin = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/2140382.png")
coin = pygame.transform.scale(coin, (100, 100))
coin_size = coin.get_rect().size

coins=[]
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

    screen.blit(bg, (0, 0))

    text = font.render(f"Монет собрано: {score}", True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(10, 10))

    screen.blit(text, text_rect)

    
    keys = pygame.key.get_pressed()

    

    if keys[pygame.K_RIGHT] and cordx <= 200:
        if keys[pygame.K_LSHIFT]:
            cordx += 0.5
        else:
            cordx += 1
    if keys[pygame.K_LEFT] and cordx >= 0:
        if keys[pygame.K_LSHIFT]:
            cordx -= 0.5
        else:
            cordx -= 1


    if random.random() < 0.001:
        x = random.randint(0, 2) 
        y = -sprite_size[1] 
        speed = 1  
        sprites.append([x*100, y, speed])

    for sprite in sprites:
        sprite[1] += sprite[2] 

    sprites = [s for s in sprites if s[1] < H]

    for sprite in sprites:
        screen.blit(sprite_img, (sprite[0], sprite[1]))

    for sprite in sprites:
        if sprite[0] <= cordx <= sprite[0]+100 and sprite[1] <= cordy <= sprite[1]+100 or sprite[0] <= cordx+100 <= sprite[0]+100 and sprite[1] <= cordy+100 <= sprite[1]+100:
            running = False
            sys.exit()

    if random.random() < 0.0001:
        x = random.randint(0, 2) 
        y = -coin_size[1] 
        speed = 1 
        coins.append([x*100, y, speed])

    for i in coins:
        i[1] += i[2] 

    coins = [s for s in coins if s[1] < H]

    for i in coins:
        screen.blit(coin, (i[0], i[1]))

    for i in coins:
        if i[0] <= cordx <= i[0]+100 and i[1] <= cordy <= i[1]+100 or i[0] <= cordx+100 <= i[0]+100 and i[1] <= cordy+100 <= i[1]+100:
            score += 1
            coins.pop()



    screen.blit(car, (cordx, cordy))


    pygame.display.update()


