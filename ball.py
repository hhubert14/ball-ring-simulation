import pygame
import random
from constants import *
import math

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Ball:
    def __init__(
        self,
        x,
        y,
        x_vel=None,
        y_vel=None,
        radius=None,
    ):
        self.x = x
        self.y = y
        self.x_vel = random.uniform(-2, 2) if x_vel is None else x_vel
        self.y_vel = random.uniform(-2, 2) if y_vel is None else y_vel
        self.speed = [self.x_vel, self.y_vel]
        self.color = (
            random.uniform(0, 255),
            random.uniform(0, 255),
            random.uniform(0, 255),
        )
        self.radius = random.uniform(20, 40) if radius is None else radius
    
    def update(self):
        self.y_vel += GRAVITY


        self.x_vel *= VELOCITY_MULTIPLIER
        self.y_vel *= VELOCITY_MULTIPLIER


        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self):
        pygame.draw.circle(
            screen, 
            self.color, 
            (int(self.x), int(self.y)), 
            self.radius,
        )

    def check_ring_collision(self, ring_center, ring_radius):
        # Calculate distance between ball center and ring center
        dx = self.x - ring_center[0]
        dy = self.y - ring_center[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Collision detected
        if distance + self.radius >= ring_radius:
            if distance > 0:
                nx = dx / distance
                ny = dy / distance
            else:
                nx = 0
                ny = 0

            dot_product = self.x_vel * nx + self.y_vel * ny

            self.x_vel = self.x_vel - 2 * dot_product * nx
            self.y_vel = self.y_vel - 2 * dot_product * ny

            # Move ball back inside the ring to prevent sticking
            overlap = (distance + self.radius) - ring_radius
            self.x -= overlap * nx
            self.y -= overlap * ny

            return True

        return False