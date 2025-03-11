import pygame
from constants import SCREEN_WIDTH

class Background:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x1 = 0
        self.x2 = SCREEN_WIDTH  # Start the second image at the end of the first
        self.speed = 3

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        # If the first image is completely off the screen, reset it to the right of the second image
        if self.x1 <= -SCREEN_WIDTH:
            self.x1 = self.x2 + SCREEN_WIDTH

        # If the second image is completely off the screen, reset it to the right of the first image
        if self.x2 <= -SCREEN_WIDTH:
            self.x2 = self.x1 + SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))