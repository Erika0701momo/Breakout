from turtle import Screen
import time
from paddle import Paddle
from block import BlockManager
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
blockmanager = BlockManager()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

blockmanager.create_blocks()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if len(blockmanager.blocks) == 0:
        scoreboard.game_clear()
        game_is_on = False

    if ball.distance(paddle) < 50 and ball.ycor() < -170:
        ball.bounce_y()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for block in blockmanager.blocks:
        if block.distance(ball) < 20 and block not in blockmanager.removed_blocks:
            ball.bounce_y()
            block.hideturtle()
            scoreboard.get_score()
            blockmanager.removed_blocks.append(block)

screen.exitonclick()