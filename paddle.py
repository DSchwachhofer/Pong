from turtle import Turtle


# one paddle for player to play with
# position: x position of paddle on screen
class Paddle:
    def __init__(self, position):
        self.paddle = []
        self.x_position = position
        self.create_paddle()
        self.moving_direction = 0

    def create_paddle(self):
        for i in range(5):
            new_segment = Turtle()
            new_segment.speed("fastest")
            new_segment.color("white")
            new_segment.penup()
            new_segment.shape("square")
            y_position = 50 - i * 20
            new_segment.setposition(self.x_position, y_position)
            self.paddle.append(new_segment)

    def update_position(self):
        # check if paddle is in screen
        if self.paddle[0].ycor() > 430 and self.moving_direction > 0:
            self.moving_direction = 0
        elif self.paddle[4].ycor() < -410 and self.moving_direction < 1:
            self.moving_direction = 0
        for segment in self.paddle:
            pos = segment.ycor()
            new_position = pos + 20 * self.moving_direction
            segment.setposition(self.x_position, new_position)
        # segments keep moving until moving direction has a new value

    # methods to update moving direction
    def move_up(self):
        self.moving_direction = 1

    def move_down(self):
        self.moving_direction = -1

    def stop_moving(self):
        self.moving_direction = 0
