import pygame
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FONT_SIZE
from dinosaur import Dinosaur
from cactus import Cactus
from background import Background
from menus import start_menu, difficulty_menu, high_scores_screen, game_over_screen
from crud import load_data, update_high_score
from utils import get_player_name

# Initializes Pygame,sets up game window and title of our game
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Dinosaur Game")

#loads all the game assets ,images,catus and resizes them ,background image and resizes it
#to fit the screen then returns all the loaded asets.
def load_assets():
  
    assets={}
    assets["dino_frames"]= [
        pygame.transform.scale(pygame.image.load(f"assets/dino_{i}.png").convert_alpha(), (50, 50))
        for i in range(1, 4)
    ]
    assets["cactus_frames"]=[
        pygame.transform.scale(pygame.image.load(f"assets/cactus_{i}.png").convert_alpha(), (30, 50))
        for i in range(1, 3)
    ]
    assets["background_image"]= pygame.transform.scale(
        pygame.image.load("assets/background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    assets["menu_background_image"] =pygame.transform.scale(
        pygame.image.load("assets/menu_background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    return assets
#run the main loop where game is happening
def run_game(assets, font, player_name, difficulty):
    
    dino= Dinosaur(assets["dino_frames"])
    cacti=[Cactus(assets["cactus_frames"], difficulty) for _ in range(2 if difficulty == "easy" else 5)]
    background= Background(assets["background_image"])
    clock =pygame.time.Clock ()
    score= 0

    while True:#checks for events like quitting the game or preessing keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not dino.jump:
                dino.jump = True#makes dino jump when we press spacebar

        # Update game objects
        background.update()
        dino.update()
        for cactus in cacti:
            cactus.update()
            if dino.rect.colliderect(cactus.rect):
                update_high_score(load_data(), player_name, score, difficulty)
                action = game_over_screen(screen, font, score, player_name, assets["menu_background_image"])
                return action 

        # Draw everything
        screen.fill(WHITE)
        background.draw(screen)
        for cactus in cacti:
            cactus.draw(screen)
        dino.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(30)  # Cap the frame rate at 30 FPS
        score += 1

def main():
    """Main function to handle the game flow."""
    assets = load_assets()
    font = pygame.font.SysFont(None, FONT_SIZE)

    while True:
        action =start_menu(screen, font, assets["menu_background_image"])
        if action == "start":
            player_name= get_player_name(screen)
            if player_name:
                difficulty =difficulty_menu(screen, font, assets["menu_background_image"])
                if difficulty:
                    while True:
                        result =run_game(assets, font, player_name, difficulty)
                        if result != "restart":
                            break  # Returns us to the main menu
        elif action == "high_scores":
            high_scores_screen(screen, font)
        elif action is None:
            break  # Exits the  dino game

    pygame.quit()

if __name__ == "__main__":
    main()