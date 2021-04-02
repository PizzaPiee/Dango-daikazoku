import pygame
import os

pygame.init()
pygame.display.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 600
ICON = pygame.image.load(os.path.join('assets', 'icon.png'))
pygame.display.set_caption("Dango daikazoku")
pygame.display.set_icon(ICON)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


FPS = 60

BACKGROUND = pygame.image.load(os.path.join('assets', 'background.png'))

def draw_window():
    left = WIDTH//4
    while left<=WIDTH:
        border = pygame.Rect(left, 0, 2, HEIGHT)
        pygame.draw.rect(WIN, (255, 255, 255), border)
        left += WIDTH//4

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_window()
    pygame.quit()

def start_menu():
    clock = pygame.time.Clock()
    pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join('sounds', 'Shining_in_the_Sky.mp3')), loops=-1)
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(BACKGROUND, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.stop()
                    main()
                    pygame.display.quit()
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

if __name__ == "__main__":
    start_menu()