from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            contants = int(data.read())
        self.high_score = contants
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.increase_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over...", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.increase_score()
