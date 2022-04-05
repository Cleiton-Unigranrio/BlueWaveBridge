import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
background_color = pygame.Color(0, 0, 0)

player = pygame.Rect(0, 0, 50, 50)
playerVelocity = pygame.Vector2(0)
playerDirection = pygame.Vector2(0, 0)
playerColor = pygame.Color(255, 0, 0)

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60) / 1000
    print(playerVelocity)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerVelocity += pygame.Vector2((0, -1)) * dt
            elif event.key == pygame.K_s:
                playerVelocity += pygame.Vector2((0, 1)) * dt
            if event.key == pygame.K_a:
                playerVelocity += pygame.Vector2((-1, 0)) * dt
            if event.key == pygame.K_d:
                playerVelocity += pygame.Vector2((1, 0)) * dt

    if playerVelocity.length() > 0:
        playerDirection = playerVelocity.normalize()
        print(playerDirection)
        player = player.move(playerVelocity * playerDirection)
        
    screen.fill(background_color)
    pygame.draw.rect(screen, playerColor, player)
    pygame.display.update()