from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(position)
        self.write(f"{self.score} ", move=False, align='center', font=('Arial', 20, 'normal'))

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score} ", move=False, align='center', font=('Arial', 20, 'normal'))



