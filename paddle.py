from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positon):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(positon)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
