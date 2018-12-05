from turtle import *

# Turtle Properties
speed(0)
color('black')
setup(600, 600)
pensize(10)

# Grid positions x and y
positions = {
    1: (-215, 205),
    2: (-12, 209),
    3: (188, 208),
    4: (-218, 4),
    5: (0, 0),
    6: (192, 3),
    7: (-220, -199),
    8: (-9, -201),
    9: (194, -195),
}

# Empty positions
grid = []


def is_valid_location(grid, user_input):
    if user_input not in grid:
        grid.append(user_input)
        print(grid)
        return user_input
    else:
        while True:
            user_input = int(numinput("Your turn", "Pick again, choose a position 1-9", 1, minval=1, maxval=9))
            return is_valid_location(grid, user_input)


def draw_board():
    penup()
    goto(-300, -100)
    pendown()
    for x in range(2):
        fd(600)
        left(90)
        penup()
        fd(200)
        left(90)
        pendown()
    penup()

    goto(-100, -300)
    left(90)
    pendown()
    for i in range(2):
        fd(600)
        right(90)
        penup()
        fd(200)
        right(90)
        pendown()
    penup()


def player_red():
    pendown()
    begin_fill()
    color('red')
    for x in range(4):
        fd(50)
        left(90)
    penup()
    end_fill()


def player_blue():
    pendown()
    begin_fill()
    color('blue')
    for x in range(4):
        fd(50)
        left(90)
    penup()
    end_fill()


def draw_token_on_board(func, player_turn):
    if player_turn == 0:
        goto(positions[func])
        player_blue()
    elif player_turn == 1:
        goto(positions[func])
        player_red()


def game_loop():
    for turn in range(1,10):
        turn = turn % 2
        if turn == 0:
            user_position = int(numinput("Your turn", "choose a position 1-9", 1, minval=1, maxval=9))
            draw_token_on_board(is_valid_location(grid, user_position), turn)

        elif turn == 1:
            user_position = int(numinput("Your turn", "choose a position 1-9", 1, minval=1, maxval=9))
            draw_token_on_board(is_valid_location(grid, user_position), turn)


draw_board()
game_loop()




