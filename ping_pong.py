'''
Pong Arcade Game
-------------------------------------------------------------
'''

import turtle

def update_score(l_score, r_score, player, score_board):
    """
    Update the score for the left or right player and display it on the screen.
    """
    if player == 'l':
        l_score += 1
    else:
        r_score += 1

    score_board.clear()
    score_board.write('Left Player: {} -- Right Player: {}'.format(
        l_score, r_score), align='center',
        font=('Arial', 24, 'normal'))
    return l_score, r_score, score_board

def setup_game():
    """
    Set up the game screen, paddles, ball, and scoreboard.
    """
    screen = turtle.Screen()
    screen.title('Pong Arcade Game')
    screen.bgcolor('white')
    screen.setup(width=1000, height=600)

    # Left paddle
    l_paddle = turtle.Turtle()
    l_paddle.speed(0)
    l_paddle.shape('square')
    l_paddle.color('red')
    l_paddle.shapesize(stretch_wid=6, stretch_len=2)
    l_paddle.penup()
    l_paddle.goto(-400, 0)

    # Right paddle
    r_paddle = turtle.Turtle()
    r_paddle.speed(0)
    r_paddle.shape('square')
    r_paddle.color('black')
    r_paddle.shapesize(stretch_wid=6, stretch_len=2)
    r_paddle.penup()
    r_paddle.goto(400, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(1)
    ball.shape('circle')
    ball.color('blue')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 4  # Initial speed increased tenfold
    ball.dy = -4  # Initial speed increased tenfold

    # Scoreboard
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.color('blue')
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)
    score_board.write('Left Player: 0 -- Right Player: 0',
                      align='center', font=('Arial', 24, 'normal'))

    return screen, ball, l_paddle, r_paddle, score_board

def pong_game():
    """
    Main function to run the Pong game.
    """
    screen, ball, l_paddle, r_paddle, score_board = setup_game()
    l_score = 0
    r_score = 0

    # Move paddles
    def l_paddle_up():
        if l_paddle.ycor() < 250:
            l_paddle.sety(l_paddle.ycor() + 20)

    def l_paddle_down():
        if l_paddle.ycor() > -240:
            l_paddle.sety(l_paddle.ycor() - 20)

    def r_paddle_up():
        if r_paddle.ycor() < 250:
            r_paddle.sety(r_paddle.ycor() + 20)

    def r_paddle_down():
        if r_paddle.ycor() > -240:
            r_paddle.sety(r_paddle.ycor() - 20)

    screen.listen()
    screen.onkeypress(l_paddle_up, 'w')
    screen.onkeypress(l_paddle_down, 's')
    screen.onkeypress(r_paddle_up, 'Up')
    screen.onkeypress(r_paddle_down, 'Down')

    while True:
        screen.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Ball and wall collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Ball and paddle collision
        if (ball.xcor() > 390 and ball.xcor() < 400 and
                ball.ycor() < r_paddle.ycor() + 50 and ball.ycor() > r_paddle.ycor() - 50):
            ball.setx(390)
            ball.dx *= -1.1  # Increase speed slightly on paddle hit

        if (ball.xcor() < -390 and ball.xcor() > -400 and
                ball.ycor() < l_paddle.ycor() + 50 and ball.ycor() > l_paddle.ycor() - 50):
            ball.setx(-390)
            ball.dx *= -1.1  # Increase speed slightly on paddle hit

        # Ball goes out of bounds
        if ball.xcor() > 490:
            ball.goto(0, 0)
            ball.dx = 4  # Reset speed
            ball.dy = -4  # Reset speed
            l_score, r_score, score_board = update_score(l_score, r_score, 'l', score_board)

        if ball.xcor() < -490:
            ball.goto(0, 0)
            ball.dx = -4  # Reset speed
            ball.dy = 4  # Reset speed
            l_score, r_score, score_board = update_score(l_score, r_score, 'r', score_board)


if __name__ == '__main__':
    pong_game()
