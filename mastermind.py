import turtle
import random

t = turtle.Turtle()

t.speed(0)

# set up the gameboard
# write the rules in the corner:
t.penup()
t.setx(-750)
t.sety(375)
t.write("Objective:")
t.sety(360)
t.write("  Guess the four color secret code in as little tries as you can.")
t.sety(345)
t.write("Rules:")
t.sety(329)
t.write("  Guess the four color secret code.")
t.sety(314)
t.write("  For every guess, the game will tell you how many colors are the right")
t.sety(299)
t.write("  colors (indicated by white circles), and how many colors are the right")
t.sety(284)
t.write("  colors AND in the right position (indicated by a black circle)")

print("The colors you can use are red, blue, green, and yellow")

# function that makes 4 squares in a row
def rectangle_row(x):
    for i in range(4):
        for i in range(4):
            t.fd(x)
            t.lt(90)
        t.fd(x)

# function that will create 10 rows of 4 squares
def ten_rows(s, x, space):
    for i in range(10):
        t.pendown()
        y = t.ycor()
        rectangle_row(s)

        t.penup()
        t.setx(x)
        t.sety(y - space)


# create 10 rows of spaces for the player to guess in
t.setx(-225)
t.sety(375)
t.write("Mastermind")

t.setx(-300)
t.sety(320)
t.pendown()

ten_rows(50, -300, 75)


# create 10 rows where the computer will put correct guesses (the black and whtie circles)
t.setx(0)
t.sety(332.5)

ten_rows(25, 0, 75)



# coding the game
# create a secret code
def code():
    # list of colors you can use
    colors = ["red", "green", "blue", "yellow"]

    secret_code = []
    for i in range(4):
        color = colors[random.randint(0, 3)]
        secret_code.append(color)

    return secret_code

# let the user guess, and fill in a circle to the respective color
def guess():
    guesses = []

    for i in range(4):
        c = input("")
        # append each color to a list
        guesses.append(c)

        t.penup()
        t.fd(50)
        t.pendown()

        t.fillcolor(c)
        t.begin_fill()
        t.circle(20)
        t.end_fill()

    return guesses

# how the function correctness works:
# one variable for each color
# count how many of each color in the secret code
# check how many are the correct color and position,subtract one from the number of things in that color add one to black
# check how many are only the correct color -> make sure the colorvariable is not 0, subtract the color by 1,add one to the write

def correctness(secret_code, guess):
    black = 0
    white = 0

    print(secret_code)

    # create a variable containing the number of each color in the secret code
    red = 0
    blue = 0
    yellow = 0
    green = 0

    # assign each variable to the number of that color is in the secret code
    for i in range(4):
        if secret_code[i] == "red":
            red = red + 1
        elif secret_code[i] == "blue":
            blue = blue + 1
        elif secret_code[i] == "yellow":
            yellow = yellow + 1
        elif secret_code[i] == "green":
            green = green + 1

    for j in range(4):
        if guess[j] == secret_code[j]:
            if guess[j] == "red":
                red = red - 1
            elif guess[j] == "blue":
                blue = blue - 1
            elif guess[j] == "yellow":
                yellow = yellow - 1
            elif guess[j] == "green":
                green = green - 1

            black = black + 1

    for k in range(4):
        if guess[k] == secret_code[k]:
            # do nothing
            continue

        elif guess[k] == "red":
            if red != 0:
                red = red - 1
                white = white + 1
        elif guess[k] == "blue":
            if blue != 0:
                blue = blue - 1
                white = white + 1
        elif guess[k] == "yellow":
            if yellow != 0:
                yellow = yellow - 1
                white = white + 1
        elif guess[k] == "green":
            if green != 0:
                green = green - 1
                white = white + 1

    for i in range(black):
        t.fillcolor("black")
        t.begin_fill()
        t.circle(7.5)
        t.end_fill()

        t.penup()
        t.fd(25)
        t.pendown()
    for i in range(white):
        t.circle(7.5)
        t.penup()
        t.fd(25)
        t.pendown()

# start the game!
def game():
    # create a variable that will keep track of if the game is won or not
    win = False

    # secret code list
    s_code = code()

    i = 0

    x = -325
    y = 325

    gx = 12.5
    gy = 337.5

    # make sure there are no more than 10 guesses
    while win == False and i <=10:
        # guess
        t.penup()
        t.setpos(x, y)
        t.pendown()
        g = guess()
        y = y - 75

        # check it's correct status
        t.penup()
        t.setpos(gx, gy)
        t.pendown()
        correctness(s_code, g)
        gy = gy - 75

        i = i + 1

game()
