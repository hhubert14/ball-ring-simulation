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
        x_vel=random.uniform(-2, 2),
        y_vel=random.uniform(-2, 2),
        radius=10,
    ):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.speed = [self.x_vel, self.y_vel]
        self.color = (
            random.uniform(0, 255),
            random.uniform(0, 255),
            random.uniform(0, 255),
        )
        self.radius = radius
    
    def update(self):
        # Δy = v_initial × Δt + (1/2) × g × (Δt)²
        gravity_change = abs(self.y_vel) * DELTA_T + (1 / 2) * 9.8 * DELTA_T ** 2
        self.y_vel += gravity_change

        self.x_vel *= AIR_RESISTANCE
        self.y_vel *= AIR_RESISTANCE


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