from turtle import Turtle
ALIGNMENT ="center"
FONT=("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        # self.high_score=0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        # self.increase_score()
        self.display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
                file.close()
        self.score=0
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=1
        self.display()

