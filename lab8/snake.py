import pygame
import random
import time 
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 25
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

score = 0
font = pygame.font.Font(None, 36)

SPEED = 10

snake = [(100, 100),(120, 100), (140,100)] 
direction = (CELL_SIZE, 0)

textures = {
    "head": pygame.image.load("lab8/sprites/head.png"),
    "tail": pygame.image.load("lab8/sprites/tail.png"),
    "horizontal": pygame.image.load("lab8/sprites/New Project-4.png"),
    "vertical": pygame.image.load("lab8/sprites/New Project-7.png"),
    "corner": pygame.image.load("lab8/sprites/New Project-3.png"),
    "apple": pygame.image.load("lab8/sprites/apple.png"),
    "temp_apple": pygame.image.load("lab8/sprites/temp_apple.png"),
    "timer1": pygame.image.load("lab8/sprites/timer1.png"),
    "timer2": pygame.image.load("lab8/sprites/timer2.png")
}

for key in textures:
    textures[key] = pygame.transform.scale(textures[key], (CELL_SIZE, CELL_SIZE))

apple = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE, 
    random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    
bg = pygame.image.load("lab8/sprites/bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))


def retry(): 
    screen.blit(bg, (0,0))
    text1 = font.render("Game Over", True, (225,0,0))
    text2 = font.render(f"Ваш счет: {score}", True, (0,0,0))
    text3 = font.render(f"Нажмите ESC, чтобы выйти", True, (0,0,0))

    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 3))
    screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2))
    screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2 + 60))
    
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    return True
                if event.key == pygame.K_ESCAPE:  
                    pygame.quit()
                    sys.exit()

timer_tick = True
temp_apple = None
temp_apple_timer = 0

running = True

while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Keys pressing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)

    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)

    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)

    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)


    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

#Game over
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]):
        retry()

#Apple collecting 
    if new_head == apple:
        SPEED += 1
        score += 1
        apple = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                 random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    elif temp_apple and new_head == temp_apple:
        score += 10
        SPEED += 1
        temp_apple = None 
    else:
        snake.pop()

    if temp_apple is None and random.randint(1, 100) > 98:
        temp_apple = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                      random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
        temp_apple_timer = time.time()

    if temp_apple and time.time() - temp_apple_timer > 3:
        temp_apple = None

    screen.blit(textures["apple"], apple)
    if temp_apple:
        if timer_tick:
            screen.blit(textures["timer1"], (temp_apple[0], temp_apple[1]-CELL_SIZE))
            timer_tick = False
        else:
            screen.blit(textures["timer2"], (temp_apple[0], temp_apple[1]-CELL_SIZE))
            timer_tick = True
        screen.blit(textures["temp_apple"], temp_apple)

#Score
    text = font.render(f"Счет = {score}", True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(10, 10))
    screen.blit(text, text_rect)



    for i, segment in enumerate(snake):
        if i == 0:
            head_rotate = textures["head"]
            if direction[0] == 0 and direction[1] == CELL_SIZE:
                head_rotate = pygame.transform.rotate(head_rotate, 180)
            if direction[0] == CELL_SIZE and direction[1] == 0:
                head_rotate = pygame.transform.rotate(head_rotate, -90)
            if direction[0] == -CELL_SIZE and direction[1] == 0:
                head_rotate = pygame.transform.rotate(head_rotate, 90)
            screen.blit(head_rotate, segment)

        elif i == len(snake) - 1: 
            prev_seg = snake[i - 1]
            tail_img = textures["tail"]
            if prev_seg[0] < segment[0]:
                tail_img = pygame.transform.rotate(tail_img, 90)
            elif prev_seg[0] > segment[0]:
                tail_img = pygame.transform.rotate(tail_img, -90)
            elif prev_seg[1] < segment[1]: 
                tail_img = pygame.transform.rotate(tail_img, 0)
            elif prev_seg[1] > segment[1]:
                tail_img = pygame.transform.rotate(tail_img, 180)
            screen.blit(tail_img, segment)

        else:
            prev_seg = snake[i - 1]
            next_seg = snake[i + 1]

            if prev_seg[0] == next_seg[0]: 
                screen.blit(textures["vertical"], segment)
            elif prev_seg[1] == next_seg[1]:
                screen.blit(textures["horizontal"], segment)
            else:  
                body_corner = textures["corner"]
                if (prev_seg[0] < segment[0] and next_seg[1] < segment[1]) or \
                   (next_seg[0] < segment[0] and prev_seg[1] < segment[1]):  
                    body_corner = pygame.transform.rotate(body_corner, 180)
                elif (prev_seg[0] > segment[0] and next_seg[1] > segment[1]) or \
                     (next_seg[0] > segment[0] and prev_seg[1] > segment[1]):  
                    body_corner = pygame.transform.rotate(body_corner, 0)
                elif (prev_seg[0] > segment[0] and next_seg[1] < segment[1]) or \
                     (next_seg[0] > segment[0] and prev_seg[1] < segment[1]):   
                    body_corner = pygame.transform.rotate(body_corner, 90)
                elif (prev_seg[0] < segment[0] and next_seg[1] > segment[1]) or \
                     (next_seg[0] < segment[0] and prev_seg[1] > segment[1]):   
                    body_corner = pygame.transform.rotate(body_corner, -90)
                
                screen.blit(body_corner, segment)
                
    pygame.display.flip()

    clock.tick(SPEED) 

pygame.quit()
