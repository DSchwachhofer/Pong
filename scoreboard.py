from turtle import Turtle


# score board class, handles one player score
class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.hideturtle()
        self.score = 0
        self.y_position = 300
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        # set position in regard of score is used for left or right player
        if self.position == "left":
            x_position = -50
            alignment = "right"
        else:
            x_position = 50
            alignment = "left"

        self.setposition(x_position, self.y_position)
        self.write(self.score, align=alignment, font=("Menlo", 100, "normal"))
        self.score += 1  # update score
