import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GREEN, FONT_SIZE
from crud import load_data, delete_player_data

def start_menu(screen,font, menu_background_image):
    while True :
       
        screen.blit(menu_background_image, (0,0))
        title = font.render("Dinosaur Game", True, GREEN)
        screen.blit(title, (300, 50))

        start_button =pygame.Rect(300, 150, 200, 50 )
        pygame.draw.rect(screen, WHITE, start_button )
        start_text= font.render("Start Game",True, BLACK)
        screen.blit(start_text, (330, 160))

        # the highscore button 
        high_scores_button =pygame.Rect(300,220, 200, 50)
        pygame.draw.rect(screen, WHITE,high_scores_button )
        high_scores_text = font.render("High Scores", True, BLACK)
        screen.blit(high_scores_text, (320, 230) )

    
        pygame.display.update()

        # Handling of game  events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                if high_scores_button.collidepoint(event.pos):
                    return "high_scores"

def difficulty_menu(screen, font, menu_background_image):
    while True:
        screen.blit(menu_background_image, (0, 0))

        title = font.render("Select Difficulty", True, GREEN)
        screen.blit(title, (300, 50))

        #easy level button
        easy_button = pygame.Rect(300, 150, 200, 50)
        pygame.draw.rect(screen, WHITE, easy_button)
        easy_text = font.render("Easy", True, BLACK)
        screen.blit(easy_text, (350, 160))

        # Hard level button
        hard_button= pygame.Rect(300, 220, 200, 50)
        pygame.draw.rect(screen, WHITE, hard_button)
        hard_text =font.render("Hard", True, BLACK)
        screen.blit(hard_text, (350, 230))

    
        pygame.display.update()#update screen


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return "easy"
                if hard_button.collidepoint(event.pos):
                    return "hard"

def high_scores_screen(screen, font):
    data=load_data()  # Loads a  player information

    while True:

        screen.fill(BLACK)

        # Draw the title
        title = font.render("High Scores", True, WHITE)
        screen.blit(title,(300, 50))

        # Create a list of all players and their highest scores across all difficulties
        all_players_scores=[]
        for player, scores_by_difficulty in data["players"].items():
           
            all_scores=[]
            
            if "easy" in scores_by_difficulty:
                all_scores.extend(scores_by_difficulty["easy"])
           
            if "hard" in scores_by_difficulty:
                all_scores.extend(scores_by_difficulty["hard"])
            # checks the players  scores, find the highest one
            if all_scores:
                highest_score= max(all_scores)
                all_players_scores.append((player,highest_score))

        # Sort all players by their highest score in descending order
        all_players_scores.sort(key=lambda x: x[1], reverse=True)

        # Display the top 4 players and their highest scores
        y_offset =100
        delete_buttons= []  
        for player, highest_score in all_players_scores[:4]:
            player_text= font.render(f"{player}: {highest_score}", True, GREEN)
            screen.blit(player_text, (300, y_offset))

            delete_button  = pygame.Rect(500, y_offset, 100, 30)
            pygame.draw.rect(screen,GREEN, delete_button)
            delete_text= font.render("Delete", True, BLACK)
            screen.blit(delete_text, (510, y_offset + 5))
            delete_buttons.append((delete_button, player))  # Store button and player name

            y_offset += 40

    
        back_button = pygame.Rect(300, y_offset + 20, 200, 50)
        pygame.draw.rect(screen, WHITE, back_button)
        back_text = font.render("Back", True, BLACK)
        screen.blit(back_text, (360, y_offset + 30))

        
        pygame.display.update()

   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return
                # Check if a delete button was clicked
                for button, player_name in delete_buttons:
                    if button.collidepoint(event.pos):
                        delete_player_data(player_name) 
                        data = load_data()  # Reload data after deletion

def game_over_screen(screen, font, score, player_name, menu_background_image):
    while True:
        # Draws the menu background,scores,restart button,main menu button
        screen.blit(menu_background_image, (0, 0))

        game_over_text= font.render("Game Over",True,BLACK)
        screen.blit(game_over_text, (320,50))
        score_text =font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (340, 100))

        restart_button= pygame.Rect(300,150,200, 50)
        pygame.draw.rect(screen,WHITE, restart_button)
        restart_text=font.render("Restart", True, BLACK)
        screen.blit(restart_text,(340, 160))

        menu_button = pygame.Rect(300,220, 200, 50)
        pygame.draw.rect(screen, WHITE,menu_button)
        menu_text= font.render("Main Menu",True, BLACK)
        screen.blit(menu_text, (330,230))

        # Update the display
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"
                if menu_button.collidepoint(event.pos):
                    return "menu"