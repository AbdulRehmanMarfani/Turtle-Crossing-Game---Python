# Turtle Crossing Game

## Overview

The Turtle Crossing Game is a simple yet engaging game where the player controls a turtle that must cross a busy road filled with moving cars. The objective is to reach the top of the screen without colliding with any cars. As the game progresses, the cars move faster, and the player must navigate through increasingly difficult levels. The game keeps track of the player's score and high score, and it includes features like pausing and restarting the game.

## Features

- **Player Control**: The player controls a turtle that can move forward using the "Up" arrow key.
- **Car Movement**: Cars move horizontally across the screen at increasing speeds as the player progresses through levels.
- **Collision Detection**: The game detects collisions between the turtle and cars, reducing the player's lives upon collision.
- **Level Progression**: Each time the turtle successfully reaches the top, the player advances to the next level, and the cars move faster.
- **Scoreboard**: The game displays the current level, remaining lives, and the high score.
- **Pause and Restart**: The game can be paused and restarted using the "P" and "R" keys, respectively.
- **Sound Effects**: The game includes sound effects for collisions and leveling up (Windows only).

## Files

- **`car_manager.py`**: Manages the creation and movement of cars.
- **`high_score.txt`**: Stores the highest score achieved by the player.
- **`main.py`**: The main script that initializes the game, handles the game loop, and manages the game state.
- **`player.py`**: Defines the player-controlled turtle and its behaviors.
- **`scoreboard.py`**: Manages the scoreboard, including the current level, lives, and high score.

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. The start screen will appear, providing instructions and a "Start Game" button.
2. **Control the Turtle**: Use the "Up" arrow key to move the turtle forward.
3. **Avoid Cars**: Navigate the turtle across the road without colliding with any cars. Each collision reduces the turtle's lives by one.
4. **Reach the Top**: Successfully reach the top of the screen to advance to the next level. The cars will move faster with each level.
5. **Pause and Restart**: Press "P" to pause the game and "R" to restart the game at any time.
6. **Game Over**: The game ends when the turtle loses all its lives. The final score and high score will be displayed on the end screen.

## Requirements

- **Python 3.x**: The game is written in Python and requires Python 3.x to run.
- **Turtle Module**: The game uses the `turtle` module, which is included with Python's standard library.
- **Winsound Module**: The game uses the `winsound` module for sound effects, which is available only on Windows.

## Installation

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Run the Game**: Navigate to the project directory and run the `main.py` script using Python:
   ```bash
   python main.py
   ```

## Customization

- **Car Colors**: The colors of the cars can be customized by modifying the `COLORS` list in `car_manager.py`.
- **Car Speed**: The initial speed of the cars and the speed increment per level can be adjusted by changing the `STARTING_MOVE_DISTANCE` and `MOVE_INCREMENT` variables in `car_manager.py`.
- **Player Lives**: The number of lives the player starts with can be changed by modifying the `lives` attribute in the `Player` class in `player.py`.

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as you see fit.

## Acknowledgments

- The game was inspired by classic arcade games and is intended as a fun project for learning Python and game development basics.
- Special thanks to the `turtle` module for providing an easy-to-use graphics library for Python.

Enjoy the game, and happy coding!
