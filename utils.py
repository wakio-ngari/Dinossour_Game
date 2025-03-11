import pygame
from constants import GRAY, BLACK, WHITE, FONT_SIZE

def get_player_name(screen):
    input_box = pygame.Rect(300,150,200, 50)
    color_inactive = BLACK
    color_active = WHITE
    color= color_inactive
    active = False
    text= ""
    font = pygame.font.SysFont(None,FONT_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)
        txt_surface = font.render(text, True, color)
        width =max(200, txt_surface.get_width() + 10)
        input_box.w=width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        prompt = font.render("Player's name:", True, WHITE)
        screen.blit(prompt, (300, 100))

        pygame.display.update()