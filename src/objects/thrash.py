import random
import pygame
import constants

class Thrash():
    def __init__(self):
        self.image = pygame.image.load('./assets/images/sprites/thrash.png').convert_alpha()
        self.representation = self.image.get_rect()
        self.representation.x = random.randint(0, constants.WINDOW_WIDTH - self.representation.width)
        self.area = pygame.display.get_surface().get_rect()
        
        self.velocity = pygame.Vector2(0, 0)
        self.velocityGoal = pygame.Vector2(0, constants.THRASH_MAX_SPEED)

    def update(self, deltaTime):
        self._updateVelocity(deltaTime * constants.THRASH_DT_MULTIPLIER)
        self.representation = self.representation.move(self.velocity)

    def draw(self, surface):
        surface.blit(self.image, self.representation)
    
    def _updateVelocity(self, step):
        self.velocity.x = self.approach(self.velocity.x, self.velocityGoal.x, step)
        self.velocity.y = self.approach(self.velocity.y, self.velocityGoal.y, step)

    def approach(self, current, goal, step):
        difference = goal - current

        if difference > step:
            current += step
        elif difference < -step:
            current -= step
        else:
            return current
        
        return current