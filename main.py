from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_score = Scoreboard((-50, 270))
r_score = Scoreboard((50, 270))


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "u")
screen.onkey(l_paddle.down, "d")



#  so that when you run paddle will already at the edge , instead of running it and looking at it going to the edge
is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # collision with up and down wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision  with r_paddle and l
    # not t using the turtle.distance(), measures the distance from the middle of on item to the other
    if ball.xcor() == 320 and ball.distance(r_paddle) <= 50 or ball.xcor() == -320 and ball.distance(l_paddle) <= 50:
        ball.bounce_x()

    # if ball goes past the r_paddle
    if ball.xcor() > 380:
        print("wall")
        l_score.add_score()
        ball.reset()
    # left paddle misses
    if ball.xcor() < -380:
        print("wall")
        r_score.add_score()
        ball.reset()







screen.exitonclick()
