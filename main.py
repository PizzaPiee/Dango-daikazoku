import pygame, os, sys, random

pygame.init()
pygame.display.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 600
ICON = pygame.image.load(os.path.join('assets', 'icon.png'))
pygame.display.set_caption("Dango daikazoku")
pygame.display.set_icon(ICON)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60
VEL = 3

BACKGROUND = pygame.image.load(os.path.join('assets', 'background.png'))

LANES = [1, WIDTH//4*1+2, WIDTH//4*2+2, WIDTH//4*3+2]
DANGO_DAIKAZOKU = ['e5', 'd5', 'g5', 'g5', 'a5', 'a5', 'b5', 'g5']
TILES = []
top = 0
for note in DANGO_DAIKAZOKU:
    i = random.randint(0, 3)
    tile = pygame.Rect(LANES[i], top, 100-2, 200)
    top -= 205
    TILES.append(tile)

def draw_window():
    WIN.fill((255, 255, 255))
    WIN.blit(BACKGROUND, (0, 0))

    left = WIDTH//4
    while left<=WIDTH:
        border = pygame.Rect(left, 0, 2, HEIGHT)
        pygame.draw.rect(WIN, (255, 255, 255), border)
        left += WIDTH//4

    for tile in TILES:
        pygame.draw.rect(WIN, (0, 0, 0), tile)

    pygame.display.flip()

def tiles_handle_movement():
    for tile in TILES:
        tile.y += VEL

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tiles_handle_movement()
        clock.tick(FPS)
        draw_window()

def start_menu():
    pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join('sounds', 'Shining_in_the_Sky.mp3')), loops=-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.stop()
                    main()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        WIN.blit(BACKGROUND, (0, 0))
        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    start_menu()