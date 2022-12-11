import turtle as trtl
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from ui import UI
import time

# screen to be visible
screen = trtl.Screen()
# dimensions of screen
screen.setup(width=1200, height=600)
# background color of screen
screen.bgcolor('black')
# title of the program
screen.title('Beat the Brick')
screen.tracer(0)

ui = UI()
ui.header()

# assigning the lives of ball
score = Scoreboard(lives=3)
# object of Paddle class
paddle = Paddle()
# object of Ball class
ball = Ball()
# object of Bricks class
bricks = Bricks()

game_paused = False
playing_game = True


# to pause the game
def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


# listening to the key press of user
screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
screen.onkey(key='space', fun=pause_game)


# collision with walls
def check_collision_with_walls():
    global ball, score, playing_game, ui
    # collision with left/right walls
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    # collision with upper wall
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return
    # collision with bottom wall
    # lost the game, game is reset
    if ball.ycor() < -280:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            playing_game = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return


# collision with paddle
def check_collision_with_paddle():
    global ball, paddle

    # x-axis coordinates of ball and paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        # paddle on right of screen
        if paddle_x > 0:
            if ball_x > paddle_x:
                # ball hits left of paddle and moves left
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        # paddle on left of screen
        elif paddle_x < 0:
            if ball_x < paddle_x:
                # ball hits left of paddle and moves left
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        # paddle in middle horizontally
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


# collision with bricks
def check_collision_with_bricks():
    global ball, bricks, score

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)

            # collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


while playing_game:
    if not game_paused:

        # update the screen after every press
        screen.update()
        time.sleep(0.01)
        ball.move()

        check_collision_with_walls()
        check_collision_with_paddle()
        check_collision_with_bricks()

        # user win
        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break
    else:
        ui.paused_status()


trtl.mainloop()