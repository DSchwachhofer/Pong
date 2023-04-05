from turtle import Turtle


# NET IN THE MIDDLE OF SCREEN
class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.turtlesize(0.3, 0.9)
        self.goto(0, 425)
        self.setheading(270)
        self.draw_net()

    def draw_net(self):
        while self.ycor() > -410:
            self.stamp()
            self.forward(35)
