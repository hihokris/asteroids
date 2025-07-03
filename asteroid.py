from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white",self.position, self.radius ,width = 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_diff = random.uniform(20,50)
        vel1, vel2 = self.velocity.rotate(angle_diff), self.velocity.rotate(-angle_diff)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_rad)
        new_asteroid1.velocity = vel1 * 1.2
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_rad)
        new_asteroid2.velocity = vel2 * 1.2