from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.level = 1
        self.high_score = self.load_high_score()  # Load high score
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard(3)  # Initialize with 3 lives

    def update_scoreboard(self, lives):
        self.clear()
        self.write(f"Level: {self.level}  Lives: {lives}  High Score: {self.high_score}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        if self.level > self.high_score:
            self.high_score = self.level
            self.save_high_score()  # Save new high score
        self.update_scoreboard(3)  # Reset lives display on level up

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 1  # Default high score if file doesn't exist