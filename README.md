#  DINOSSAUR GAME

This is a python based game thats built through use of pygame framework.
The player controls the dinosaur that runs endlessly,avoding obstacles wihich in our case are cacti to achieve the highest score possible.
The game features multiple difficulty levels,a highscore system and a user friendly interface.


## Table of Contents

### 1.Features
### 2.How to play
### 3.Installation
### 4.File structure
### 5.Code Overview
### 6.Crud operations
### 7.Future improvements
### 8.Credits

## Features
.Endless Gameplay: the dinosour runs endlessly depending on how many obstacles you avoid.

.Difficulty levels: one can choose between easy and hard modes.

.Dynamic Background: there is a scrolling background of dessert that creates the illusion of movement.

.Collision Detection: When dino collides with cacti,game ends.

Friendly Menus:  user friendly menus to allow user easily navigate the game.

## How to Play

### 1.start game
- Run python main.py to launch game.
- press 'start game' button to begin.
### 2.Enter Your Name
- Enter your name using the keyboard.
### 3.Choose difficulty
- choose either hard or easy level
### 4.Gameplay
- use the spacebar to make dino jump over cacti.
- your score is saved and you can choose to restart or return to main menu to check scores or change level.
### 5.View Score
one can view scores by the highscores menu where only the top four scores are displayed.


## Installation
###  Required
- Python 3
- Pygame library
### Steps
1.Clone the Repository:
- git clone https://github.com/your-username/dino-game.git
- cd dino-game

2. Install Pygame:
- pip install pygame

3. Run the Game:
- python main.py

## File Structure
- The game has the following files:

- data.json: stores players data (names and scores)
- constants.py: contains screen dimensions,colours and font size.
- background.py:Manages the scrolling background.
- cactus.py: Manages cactus obsatacles.
- utils.py: Contains utility functions like get_player_name.
- main.py: The main game loop and entry point.
- menus.py: Handles all menus and screens(start menu,difficult menu,highscores screen,game over screen).
- dinosour.py:Controls dinos movement and animation.
-crud.py: Implements crud operations for saving and loading players data.

## CRUD Operations
The game implements CRUD(create,read,update,delete)operations for managing player data;

### 1.Create
- When a player enters their name ,a new entry is created

### 2.Read
- we are able to view or retrieve players data through the load-data function. 
- and are able to view player and scores in the highscore screen.

### 3.Update
- The update_highscore function updates a players highscore when they achieve a new score.
- player can choose a level between hard and easy.

### 4.Delete
- A players data and score can be erased completely from the data.json through delete_player function.

## Future Improvements
- Adding more obstacles like rocks,birds ro make game more exciting and tough as one advances .

- sound effects for running,jumping,collison and on passing a highscore.

- Allow two players to compete simultaneously.

## Credits
### Developer.
- JOYCE NGARI.

### License
- MIT License

### library used
 - Pygame







