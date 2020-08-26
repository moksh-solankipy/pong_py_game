import turtle

win = turtle.Screen()
win.title("Pong Game By @Moksh &copy")

win.bgcolor("black")
win.setup(width=900, height=700)
win.tracer(0)

# score
score_a = 0
score_b = 0


# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(-1)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=0.5, stretch_wid=6)
paddle_a.penup()
paddle_a.color("blue")
paddle_a.goto(-350, 0)

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(-1)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=0.5, stretch_wid=6)
paddle_b.penup()
paddle_b.color("blue")
paddle_b.goto(350, 0)

# pen
pen = turtle.Turtle()
pen.speed(-1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)


# ball
ball = turtle.Turtle()
ball.speed(-1)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.08
ball.dy = -0.07


# function for paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)


# function for paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")


win.onkeypress(paddle_b_up, "i")
win.onkeypress(paddle_b_down, "k")


# Main
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1

    if ball.xcor() > 440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center" , font="Arial")

    if ball.xcor() < -440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font="Arial")

    # Paddle and Ball Collisions
    #

    # paddle_b Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    # paddle_a Collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
