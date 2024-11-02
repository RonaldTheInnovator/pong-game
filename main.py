from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebaord import Scoreboard
import time


# STEP 1 | CREATE THE SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000,height=600)
screen.title(f"Pong Game | Developed by Ronald Netya on 11/1/24")
screen.tracer(0)

r_paddle = Paddle((480,0))
l_paddle = Paddle((-480,0))

pong_ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()
# STEP 4 | DETECT COLLISION WITH WALL AND BOUNCE
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
#         NEEDS TO BOUNCE
          pong_ball.bounce_y()

# STEP 5 | DETECT COLLISION WITH THE PADDLE
    if pong_ball.distance(r_paddle) < 30 and pong_ball.xcor() > 340 or pong_ball.distance(l_paddle) < 30 and pong_ball.xcor() < -340:
        pong_ball.bounce_x()

# STEP 5 | DETECT WHEN PADDLE MISSES
#     Detect R paddle misses
    if pong_ball.xcor() > 500:
        pong_ball.reset_position()
        scoreboard.l_point()
    #Detect L Paddle misses
    if pong_ball.xcor() < -500:
        pong_ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()