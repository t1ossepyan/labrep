import pygame
import datetime
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((736, 736))
face = pygame.image.load('/Users/tevososepyan/Documents/PythonRep/lab7/pictures/clock.png.jpg')
mi = pygame.image.load('/Users/tevososepyan/Documents/PythonRep/lab7/pictures/minute.png').convert_alpha()
min = pygame.transform.scale(mi, (72,356))
se = pygame.image.load('/Users/tevososepyan/Documents/PythonRep/lab7/pictures/minarrow.png').convert_alpha()
sec = pygame.transform.scale(se, (325, 960))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    center = (368, 368)
    now = datetime.datetime.now()

    second_angle = -now.second * 6 
    minute_angle = -(now.minute * 6 + now.second * 0.1) 


    rotated_minute = pygame.transform.rotate(min, minute_angle)
    rotated_second = pygame.transform.rotate(sec, second_angle)

    minute_rect = rotated_minute.get_rect(center=center)
    second_rect = rotated_second.get_rect(center=center)

    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip()
    clock.tick(60)
    angle = int(now.minute) * 6 
