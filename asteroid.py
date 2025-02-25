from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        # rotated1 = pygame.Vector2(0, 1).rotate(random_angle)
        # rotated2 = pygame.Vector2(0, 1).rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
        return new_asteroid1, new_asteroid2