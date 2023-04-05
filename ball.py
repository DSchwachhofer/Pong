from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        # get random starting direction
        self.start_left_or_right = random.randint(0, 1)
        self.reset_ball()
        self.hits = 1

    # reset ball to middle of screen
    # set random direction for ball to move
    def reset_ball(self):
        self.color("white")
        self.hits = 1
        self.setposition(0, 0)
        if self.start_left_or_right == 0:
            self.setheading(random.randint(155, 205))
        else:
            self.setheading(random.randint(-25, 25))

    # move ball, hte more registered hits, the faster the ball will get
    def move_ball(self):
        self.forward(10 + self.hits)

    # calculate new angle if ball hits paddle
    # difference: way between first paddle segment and ball
    def bounce_from_paddle(self, difference, paddle_position):
        middle = difference - 45  # get middle of pannel
        if paddle_position == "right":
            new_heading = middle + 180
        else:
            new_heading = middle * -1
        self.hits += 1
        print(self.hits)
        self.setheading(new_heading)
        self.move_ball()

    # calculate new angle if ball hits wall
    def bounce_from_wall(self):
        current_heading = self.heading() - 90
        new_heading = 90 + 90 - current_heading
        self.setheading(new_heading + 90)
