import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            random_angle = random.uniform(20, 50)
            dir_1 = self.velocity.rotate(random_angle)
            dir_2 = self.velocity.rotate(-1 * random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for i in range(0, 2):
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                match i:
                    case 0:
                        new_asteroid.velocity = dir_1 * 1.2
                    case 1:
                        new_asteroid.velocity = dir_2 * 1.2

            self.kill()
