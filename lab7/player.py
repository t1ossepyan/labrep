import pygame
import sys
import os

pygame.init()

pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

playlist = [
    "/Users/tevososepyan/Documents/PythonRep/lab7/songs/Chronos.mp3",
    "/Users/tevososepyan/Documents/PythonRep/lab7/songs/house_lo.mp3",
    "/Users/tevososepyan/Documents/PythonRep/lab7/songs/Overdrive-Matrika.mp3"
]

current_song_index = 0
is_paused = False

def load_and_play(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[index]}")

load_and_play(current_song_index)

font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    if not is_paused:
                        pygame.mixer.music.pause()
                        is_paused = True
                        print("Paused")
                    else:
                        pygame.mixer.music.unpause()
                        is_paused = False
                        print("Resumed")
                else:
                    load_and_play(current_song_index)
                    is_paused = False

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_paused = False
                print("Stopped")

            if event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(playlist)
                load_and_play(current_song_index)
                is_paused = False

            if event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(playlist)
                load_and_play(current_song_index)
                is_paused = False

    song_name = os.path.basename(playlist[current_song_index])
    text_surface = font.render(f"Now Playing: {song_name}", True, BLACK)
    screen.blit(text_surface, (50, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(30)
