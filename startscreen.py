from turtle import Turtle


class Start_Screen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, -150)
        self.logo = r"""

.______     ______   .__   __.   _______ 
|   _  \   /  __  \  |  \ |  |  /  _____|
|  |_)  | |  |  |  | |   \|  | |  |  __  
|   ___/  |  |  |  | |  . `  | |  | |_ | 
|  |      |  `--'  | |  |\   | |  |__| | 
| _|       \______/  |__| \__|  \______| 
                                         
                   
"""
        self.write(self.logo, align="center", font=("Menlo", 25, "normal"))
