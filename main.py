import pygame
from constants import *
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Ring Simulation")

BG_COLOR = (0, 0, 0)  # Black background
WHITE = (255, 255, 255)  # White border

# Ring properties
ring_center = (400, 300)  # Center position
ring_radius = 250  # Radius
ring_width = 3  # Border thickness

balls = [Ball(400, 300)]


run = True
clock = pygame.time.Clock()
while run:
    # Boilerplate
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(BG_COLOR)

    # Custom simulation logic
    pygame.draw.circle(screen, WHITE, ring_center, ring_radius, ring_width)

    for ball in balls:
        ball.draw()
        ball.update()
        if ball.check_ring_collision(ring_center, ring_radius):
            balls.append(ball)

pygame.quit()