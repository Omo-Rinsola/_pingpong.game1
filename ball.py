from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # same x different y
        # y_axis = random.randint(-250, 251)
        # x_axis = [-350, 350]
        # x_ = random.choice(x_axis)
        # self.goto(x_, y_axis)
        # put tracer on for bouncing effect

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # only need y to reduce to bounce back
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # increase ball speed when ball hits paddle
        self.move_speed *= 0.9

    #    when ball goes out : reset starts bouncing from the other player's side
    def reset(self):
        self.goto(0, 0)
        # when a player loses it will reset to the original speed
        self.move_speed = 0.1
        self.bounce_x()


