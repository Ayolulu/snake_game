from turtle import Turtle
with open("data.txt") as file:
    data_high_score = file.read()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.highscore = data_high_score
        self.number_of_bites = 0
        self.penup()
        self.goto(0,270)

    def keep_score(self):
        self.write(f"Score:{self.number_of_bites } High Score: {self.highscore} ",align="center",font=('Courier', 18, 'normal'))
    def add_score(self):
        self.number_of_bites = self.number_of_bites + 1
    def reset_game(self):
        if self.number_of_bites > int(self.highscore):
            self.highscore = self.number_of_bites
            with open("data.txt",mode="w") as file:
                file.write(f"{self.number_of_bites}")
        self.number_of_bites = 0
        self.clear()
        self.keep_score()
    # def game_is_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align="center", font=('Courier', 24, 'normal'))



