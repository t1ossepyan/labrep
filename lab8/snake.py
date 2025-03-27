import pygame
import random


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

snake = [(100, 100), (80, 100), (60, 100)] 
direction = (CELL_SIZE, 0)
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

    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]):
        retry()

    if new_head == apple:
        score += 1
        SPEED += 1
        apple = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE, 
                 random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    else:
        snake.pop() 

    text = font.render(f"Счет = {score}", True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(10, 10))

    screen.blit(text, text_rect)

    screen.blit(texture, (apple[0], apple[1]))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(SPEED) 

pygame.quit()
