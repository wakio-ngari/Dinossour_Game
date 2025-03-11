import pygame
from constants import SCREEN_HEIGHT

class Dinosaur:
    def __init__(self, frames):

        self.frames= frames
        self.current_frame= 0
        self.image =self.frames[self.current_frame]
        self.rect= self.image.get_rect()
        self.rect.x =50
        self.rect.y= SCREEN_HEIGHT - self.rect.height - 50
        self.jump= False
        self.jump_speed= 10
        self.animation_speed =0.2

    def update(self):
        # handles our dinosaurs Animation
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[int(self.current_frame)]

        # handles our dino Jump
        if self.jump:
            self.rect.y -= self.jump_speed
            self.jump_speed -= 0.4
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height - 50:
                self.rect.y = SCREEN_HEIGHT - self.rect.height - 50
                self.jump = False
                self.jump_speed= 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)