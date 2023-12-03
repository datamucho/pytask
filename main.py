import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Game")

white = (255, 255, 255)
blue = (0, 0, 255)

player_size = 50
player_x, player_y = width // 2, height // 2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += 5
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y < height - player_size:
        player_y += 5

    screen.fill(white)

    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
