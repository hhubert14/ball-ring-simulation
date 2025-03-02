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
        xv=random.uniform(-2, 2),
        yv=random.uniform(-2, 2),
        radius=10,
    ):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.speed = [self.xv, self.yv]
        self.color = (
            random.uniform(0, 255),
            random.uniform(0, 255),
            random.uniform(0, 255),
        )
        self.radius = radius
    
    def update(self):
        # Δy = v_initial × Δt + (1/2) × g × (Δt)²
        gravity_change = abs(self.yv) * DELTA_T + (1 / 2) * 9.8 * DELTA_T ** 2
        self.yv += gravity_change

        self.xv *= AIR_RESISTANCE
        self.yv *= AIR_RESISTANCE


        self.x += self.xv
        self.y += self.yv

    def draw(self):
        pygame.draw.circle(
            screen, 
            self.color, 
            (int(self.x), int(self.y)), 
            self.radius,
        )

    def check_ring_collision(self, ring_center, ring_radius):
        centers_distance = math.sqrt(
            (self.x - ring_center[0]) ** 2 + (self.x - ring_center[1]) ** 2
        )

        # Collision detected
        if centers_distance + self.radius >= ring_radius:
            return True

        
