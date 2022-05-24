import pygame

import constants
from objects.player import Player
from objects.thrash import Thrash
from systems.thrash_spawner import ThrashSpawner
from ui.text import Text

pygame.init()
screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
background_image = pygame.image.load('assets/images/background/bg.png').convert()

while True:
    game_over = False
    player = Player()
    font = pygame.font.Font('assets/fonts/gamefont.ttf', 24)
    scoreText = Text('', font)
    thrashSpawner = ThrashSpawner()
    score = 0

    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 100

        events = pygame.event.get()

        player.update(dt, events)
        thrashSpawner.update(dt, events)
        scoreText.update(f'Score: {score}')

        screen.blit(background_image, (0, 0))
        
        player.draw(screen)
        thrashSpawner.draw(screen)
        scoreText.draw(screen, (10, 10))

        if game_over:
            pygame.time.wait(2000)
            break

        for event in pygame.event.get():
            if event.type == constants.GAME_OVER_EVENT:
                game_over = True

        for thrash in thrashSpawner.thrashes:
            if thrash.representation.colliderect(player.representation):
                thrashSpawner.thrashes.remove(thrash)
                score += 1

        pygame.display.flip()
