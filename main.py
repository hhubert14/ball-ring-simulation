import pygame
from constants import *
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Ring Simulation")

BG_COLOR = (0, 0, 0)  # Black background
WHITE = (255, 255, 255)  # White border
RED = (255, 0, 0)

# Ring properties
ring_center = (400, 300)  # Center position
ring_radius = 250  # Radius
ring_width = 3  # Border thickness

# ball_obj = pygame.draw.circle(
#     surface=screen, color=RED, center=[100, 100], radius=40)

# # speed = [X direction speed (+ right, - left), Y direction speed (+ down, - up)]
# speed = [1, -2]

ball = Ball(400, 300)

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(BG_COLOR)

    pygame.draw.circle(screen, WHITE, ring_center, ring_radius, ring_width)

    ball.draw()
    ball.update()
    ball.check_ring_collision(ring_center, ring_radius)




    # ball_obj = ball_obj.move(speed)

    # # if ball goes out of screen then change direction of movement
    # if ball_obj.left <= 0 or ball_obj.right >= SCREEN_WIDTH:
    #     speed[0] = -speed[0]
    # if ball_obj.top <= 0 or ball_obj.bottom >= SCREEN_HEIGHT:
    #     speed[1] = -speed[1]

    # # draw ball at new centers that are obtained after moving ball_obj
    # pygame.draw.circle(surface=screen, color=RED,
    #     center=ball_obj.center, radius=40)

    pygame.display.update()
pygame.quit()