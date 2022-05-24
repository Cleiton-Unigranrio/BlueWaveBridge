import pygame
import constants

from objects.thrash import Thrash

class ThrashSpawner:
    def __init__(self):
        self._spawnTrashTimer = pygame.time.set_timer(
            constants.SPAWN_THRASH_EVENT,
            constants.THRASH_SPAWN_MS_DELAY,
        )
        self.thrashes = []
    
    def spawn(self):
        self.thrashes.append(Thrash())
    
    def update(self, dt, events):
        for event in events:
            if event.type == constants.SPAWN_THRASH_EVENT:
                self.thrashes.append(Thrash())

        for thrash in self.thrashes:
            if thrash.representation.y > constants.WINDOW_HEIGHT:
                self.thrashes.remove(thrash)
                pygame.event.post(pygame.event.Event(constants.GAME_OVER_EVENT))
            else:
                thrash.update(dt)

    def draw(self, surface):
        for thrash in self.thrashes:
            thrash.draw(surface)