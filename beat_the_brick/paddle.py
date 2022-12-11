from turtle import Turtle

# distance to be moved on key press
DIST_MOVE = 70


# paddle dimensions and requirements
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('steel blue')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)

    # moves left by the distance of movement
    def move_left(self):
        self.backward(DIST_MOVE)

    # moves right by the distance of movement
    def move_right(self):
        self.forward(DIST_MOVE)