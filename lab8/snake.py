import pygame
import random
import time 

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

score = 0

font = pygame.font.Font(None, 36)

SPEED = 10

snake = [(100, 100),(120, 100), (140,100)] 
direction = (CELL_SIZE, 0)
snake_body_texture = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/New Project-4.png")
snake_body_texture = pygame.transform.scale(snake_body_texture, (CELL_SIZE, CELL_SIZE))

snake_body_texture_vertical = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/New Project-7.png")
snake_body_texture_vertical = pygame.transform.scale(snake_body_texture_vertical, (CELL_SIZE, CELL_SIZE))

snake_body_texture_head = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/New Project-6.png")
snake_body_texture_head = pygame.transform.scale(snake_body_texture_head, (CELL_SIZE, CELL_SIZE))

apple = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE, 
         random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

texture = pygame.image.load("/Users/tevososepyan/Documents/PythonRep/lab8/sprites/edfwe.jpg")
texture = pygame.transform.scale(texture, (CELL_SIZE, CELL_SIZE))
running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    def retry():
        text = font.render(f"ВЫ ПРОИГРАЛИ :(", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        
        
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
        score += 1
        apple = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE, 
                 random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    else:
        snake.pop() 

#Score
    text = font.render(f"Счет = {score} direction{direction}", True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(10, 10))
    screen.blit(text, text_rect)
    screen.blit(texture, (apple[0], apple[1]))


#Head position
    if direction[0] == 0 and direction[1] == CELL_SIZE:
        down = pygame.transform.rotate(snake_body_texture_head, 180)
        screen.blit(down, (snake[0][0], snake[0][1]))
    if direction[0] == 0 and direction[1] == -CELL_SIZE:
        screen.blit(snake_body_texture_head, (snake[0][0], snake[0][1]))
    if direction[0] == CELL_SIZE and direction[1] == 0:
        right = pygame.transform.rotate(snake_body_texture_head, -90)
        screen.blit(right, (snake[0][0], snake[0][1]))
    if direction[0] == -CELL_SIZE and direction[1] == 0:
        left = pygame.transform.rotate(snake_body_texture_head, 90)
        screen.blit(left, (snake[0][0], snake[0][1]))
    
#Body texture displaying
    for segment in snake[1:]:
        if direction[1] == 0:
            screen.blit(snake_body_texture, (segment[0], segment[1]))
        if direction[0] == 0:
            screen.blit(snake_body_texture_vertical, (segment[0], segment[1]))
        
    pygame.display.flip()

    clock.tick(SPEED) 

pygame.quit()
