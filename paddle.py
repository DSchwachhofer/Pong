from turtle import Turtle


# one paddle for player to play with
# position: x position of paddle on screen
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.x_position = position
        self.create_paddle()
        self.moving_direction = 0
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.setposition(self.x_position, 0)

    def update_position(self):
        pass
        # check if paddle is in screen
        if self.ycor() > 380 and self.moving_direction > 0:
            self.moving_direction = 0
        elif self.ycor() < -380 and self.moving_direction < 1:
            self.moving_direction = 0
        pos = self.ycor()
        new_position = pos + 20 * self.moving_direction
        self.setposition(self.x_position, new_position)
        # segments keep moving until moving direction has a new value

    # methods to update moving direction
    def move_up(self):
        self.moving_direction = 1

    def move_down(self):
        self.moving_direction = -1

    def stop_moving(self):
        self.moving_direction = 0
