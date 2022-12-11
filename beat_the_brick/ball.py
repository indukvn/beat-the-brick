from turtle import Turtle

# distance to be moved by the ball
DIST_MOVE = 10


# ball dimensions and requirements
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move_dist = DIST_MOVE
        self.y_move_dist = DIST_MOVE
        self.reset()

    # movement of ball
    def move(self):
        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(x=new_x, y=new_y)

    # bounce action of ball
    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_dist *= -1

        if y_bounce:
            self.y_move_dist *= -1

    # reset of ball position
    def reset(self):
        self.goto(x=0, y=-240)
        self.y_move_dist = 10