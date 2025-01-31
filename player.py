from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.go_to_start()
        self.lives = 3  # Initialize lives
        self.paused = False  # Pause state

    def move(self):
        if not self.paused:
            self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def lose_life(self):
        self.lives -= 1
        if self.lives > 0:
            self.go_to_start()
        return self.lives > 0

    def pause_game(self):
        self.paused = not self.paused  # Toggle pause state

    def restart_game(self):
        self.go_to_start()
        self.lives = 3
        self.paused = False

    def is_paused(self):
        return self.paused