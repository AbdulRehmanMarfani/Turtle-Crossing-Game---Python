import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import winsound  # For Windows sound effects

# Sound effects (Windows)
def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

# Function to display text on the screen
def display_text(text, y_offset=0, font_size=24, color="white"):
    text_turtle = Turtle()
    text_turtle.color(color)
    text_turtle.penup()
    text_turtle.hideturtle()
    text_turtle.goto(0, y_offset)
    text_turtle.write(text, align="center", font=("Courier", font_size, "normal"))
    return text_turtle

# Function to create a button
def create_button(text, y_offset, callback):
    button = Turtle()
    button.color("white")
    button.penup()
    button.hideturtle()
    button.goto(0, y_offset)
    button.write(text, align="center", font=("Courier", 24, "normal"))
    screen.onclick(lambda x, y: callback() if -50 < y - y_offset < 50 else None)

# Initialize screen
screen = Screen()
screen.setup(width=750, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Function to start the game
def start_game():
    global game_is_on, turtle, cars_manager, scoreboard
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    # Initialize game components
    turtle = Player()
    cars_manager = CarManager()
    scoreboard = Scoreboard()

    # Keyboard controls
    screen.listen()
    screen.onkey(turtle.move, "Up")
    screen.onkey(turtle.pause_game, "p")  # Pause the game
    screen.onkey(turtle.restart_game, "r")  # Restart the game

    game_is_on = True

# Function to show the start screen
def show_start_screen():
    screen.clear()
    screen.bgcolor("black")
    display_text("Turtle Crossing Game", y_offset=50, font_size=40)
    display_text("Avoid the cars and reach the top!", y_offset=0)
    display_text("Press 'P' to Pause the Game", y_offset=-50)
    display_text("Press 'R' to Restart the Game", y_offset=-100)
    create_button("Start Game", y_offset=-200, callback=start_game)

# Function to show the end screen
def show_end_screen():
    screen.clear()
    screen.bgcolor("black")
    display_text("Game Over", y_offset=50, font_size=30, color="red")
    display_text(f"Final Score: {scoreboard.level}", y_offset=-50)
    display_text(f"High Score: {scoreboard.high_score}", y_offset=-100)
    create_button("Restart Game", y_offset=-200, callback=start_game)

# Show the start screen initially
show_start_screen()

# Main game loop
game_is_on = False
paused = False

while True:
    if game_is_on and not paused:
        time.sleep(0.1)
        screen.update()

        # Generate and move cars
        cars_manager.generate_car(scoreboard.level)
        cars_manager.move_cars()

        # Check for collision with cars
        for car in cars_manager.all_cars:
            if car.distance(turtle) < 20:
                play_sound("collision.wav")  # Play collision sound
                if not turtle.lose_life():
                    game_is_on = False
                    scoreboard.game_over()
                    show_end_screen()
                else:
                    scoreboard.update_scoreboard(turtle.lives)  # Update lives display
                break  # Exit the loop after handling collision

        # Check if turtle reached the finish line
        if turtle.is_at_finish_line():
            play_sound("level_up.wav")  # Play level-up sound
            turtle.go_to_start()
            cars_manager.level_up()
            scoreboard.level_up()

    # Handle pause state
    if game_is_on and turtle.is_paused():
        paused = True
    else:
        paused = False

    # Allow the screen to process events even when paused
    screen.update()

screen.exitonclick()






