import sys
import pygame
import constants


class Player:
    def __init__(self):
        self.boatHeadingLeft = pygame.image.load('./assets/images/sprites/boat-left.png').convert_alpha()
        self.boatHeadingRight = pygame.image.load('./assets/images/sprites/boat-right.png').convert_alpha()
        self.image = self.boatHeadingLeft
        self.representation = self.image.get_rect()
        self.representation.x = constants.PLAYER_X_SPAWN_POINT
        self.representation.y = constants.PLAYER_Y_SPAWN_POINT
        self.maxSpeed = constants.PLAYER_MAX_SPEED
        self.velocity = pygame.Vector2(0, 0)
        self.velocityGoal = pygame.Vector2(0, 0)

    def update(self, deltaTime, events):
        self._handle_controls(events)
        self._updateVelocity(deltaTime * constants.PLAYER_DT_MULTIPLIER)
        self._updateImage()
        self.representation = self.representation.move(self.velocity)
        self._keep_inside_bounds()

    def draw(self, surface):
        surface.blit(self.image, self.representation)

    def _handle_controls(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_w:
                    self.velocityGoal.y = -self.maxSpeed
                if event.key == pygame.K_a:
                    self.velocityGoal.x = -self.maxSpeed
                if event.key == pygame.K_s:
                    self.velocityGoal.y = self.maxSpeed
                if event.key == pygame.K_d:
                    self.velocityGoal.x = self.maxSpeed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.velocityGoal.y = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.velocityGoal.x = 0
    
    def _keep_inside_bounds(self):
        if self.representation.x >= (constants.WINDOW_WIDTH - self.representation.width):
            self.representation.x = constants.WINDOW_WIDTH - self.representation.width

        if self.representation.x <= 0:
            self.representation.x = 0

        if self.representation.y <= 0:
            self.representation.y = 0

        if self.representation.y >= (constants.WINDOW_HEIGHT - self.representation.width):
            self.representation.y = constants.WINDOW_HEIGHT - self.representation.width
        pass
    
    def _updateVelocity(self, step):
        self.velocity.x = self._approach(self.velocity.x, self.velocityGoal.x, step)
        self.velocity.y = self._approach(self.velocity.y, self.velocityGoal.y, step)

    def _approach(self, current, goal, step):
        difference = goal - current

        if difference > step:
            current += step
        elif difference < -step:
            current -= step
        else:
            current = goal
        
        return current

    def _updateImage(self):
        if self.velocityGoal.x > 0:
            self.image = self.boatHeadingRight
        else:
            self.image = self.boatHeadingLeft