import pygame

class Ball:
    def __init__(self, xv=0.1, yv=0.1):
        self.xv = xv
        self.yv = yv
        self.speed = [self.xv, self.yv]
        
