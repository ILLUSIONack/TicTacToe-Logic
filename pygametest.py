from turtle import *

speed(0)
color('black')
setup(600,600)
pensize(10)

penup()
goto(-300,-100)
pendown()

def board():
    for x in range(2):
        fd(600)
        left(90)
        penup()
        fd(200)
        left(90)
        pendown()
    penup()
    
    goto(-100,-300)
    left(90)
    pendown()
    fd(600)
    right(90)
    penup()
    fd(200)
    right(90)
    pendown()
    fd(600)

def square_red():
    pendown()
    begin_fill()
    color('red')
    for x in range(4):
        fd(50)
        left(90)
    penup()
    end_fill()

def square_blue():
    pendown()
    begin_fill()
    color('blue')
    for x in range(4):
        fd(50)
        left(90)
    penup()
    end_fill()


positions = {
    1: (-215,205),
    2: (-12, 209),
    3: (188, 208),
    4: (-218, 4),
    5: (0,0),
    6: (192,3),
    7: (-220,199),
    8: (-9,201),
    9: (194, -195),
    }

board()
penup()
turn = 0
for turn in range(9):
    if turn == 0:
        user_position = numinput("Your turn", "choose a position 1-9", 1, minval=1, maxval=9)
        goto(positions[user_position])
        square_blue()
    turn+=1

    if turn == 1:
        user_position = numinput("Your turn", "choose a position 1-9", 1, minval=1, maxval=9)
        goto(positions[user_position])
        square_red()
    (turn%2)-1
    print(turn)

        
        

        
    

