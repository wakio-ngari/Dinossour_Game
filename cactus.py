import pygame

import random

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Cactus:

    def __init__(self , frames, difficulty ):
        self.frames= frames
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect= self.image.get_rect()
        self.difficulty= difficulty
        
        # Adjust spacing based on difficulty and level (easy or hard)
        if difficulty=="easy":
            self.rect.x= SCREEN_WIDTH + random.randint(400,600)
        else:
            self.rect.x= SCREEN_WIDTH + random.randint(200,400)
            
        self.rect.y=SCREEN_HEIGHT - self.rect.height - 50
        self.animation_speed = 0.1

        # Adjust speed based on difficulty
        if difficulty == "easy":
            self.speed= 5
        elif difficulty == "hard":
            self.speed= 10

    def update(self):
        # controls cacti Animation
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image =self.frames[int(self.current_frame )]

        # controls cacti Movements
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            if self.difficulty == "easy":
                self.rect.x = SCREEN_WIDTH + random.randint(400, 600)
            else:
                self.rect.x = SCREEN_WIDTH + random.randint(200, 400)
            self.rect.y = SCREEN_HEIGHT - self.rect.height - 50

    def draw(self,screen):
        screen.blit(self.image,self.rect)
