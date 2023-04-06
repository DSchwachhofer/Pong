from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from startscreen import Start_Screen
import time

# Game Speed
SPEED = 0.01

# Setup Screen
screen = Screen()
screen.tracer(0)  # keep screen from self updating
screen.bgcolor("black")
screen.setup(width=1600, height=900)
screen.title("Pong")

# show start screen for 3 seconds
start_screen = Start_Screen()
screen.update()
# time.sleep(3)
start_screen.clear()

# set up game
net = Net()  # draw net in the middle
paddle_left = Paddle(-770)
paddle_right = Paddle(760)
ball = Ball()
score_left = Scoreboard("left")
score_right = Scoreboard("right")

screen.update()

# setup key listeners
screen.listen()
screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")
screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")

screen.onkeyrelease(paddle_right.stop_moving, "Up")
screen.onkeyrelease(paddle_right.stop_moving, "Down")
screen.onkeyrelease(paddle_left.stop_moving, "w")
screen.onkeyrelease(paddle_left.stop_moving, "s")

game_is_on = True


# set up function to stop game
def end_game():
    global game_is_on
    print("GOODBYE")
    game_is_on = False


screen.onkey(end_game, "Escape")
while game_is_on:
    paddle_left.update_position()
    paddle_right.update_position()
    ball.move_ball()
    screen.update()
    game_speed = SPEED
    time.sleep(game_speed)

    # detect collision with up and down wall
    if ball.ycor() > 440:
        ball.bounce_from_wall()
    elif ball.ycor() < -430:
        ball.bounce_from_wall()

    # detect collision with paddle
    if ball.xcor() > 740:
        difference = paddle_right.ycor() - ball.ycor()
        if -50 < difference < 50:
            ball.bounce_from_paddle(difference, "right")
    if ball.xcor() < -750:
        difference = paddle_left.ycor() - ball.ycor()
        if -50 < difference < 50:
            ball.bounce_from_paddle(difference, "left")
    # detect ball collision with side walls
    if ball.xcor() > 780:
        # update score
        score_left.update_score()
        ball.color("red")
        screen.update()
        time.sleep(2)
        ball.start_left_or_right = 0
        ball.reset_ball()
    if ball.xcor() < -785:
        # update score
        score_right.update_score()
        ball.color("red")
        screen.update()
        time.sleep(2)
        ball.start_left_or_right = 1
        ball.reset_ball()

screen.exitonclick()
