PLAYER1 = 10
PLAYER2 = 11

#STUCKKKKKK
grid = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]


def is_valid_location(grid, position_choose, player):
    print(player)
    if grid[position_choose] != "x":
        grid[position_choose] = player
    else:
        position_choose = int(input("Choose a position again to draw in from 1-9"))
        is_valid_location(grid, position_choose, PLAYER1)



turn = 0
print(grid)

game_over = False

for player_turn in range(9):
    if turn == 0:
        # Player input 1
        position_choose = int(input("Choose a position to draw in from 1-9"))-1
        while True:
            if grid[position_choose] != 10 and 11:
                grid[position_choose] = PLAYER1
                break
            else:
                position_choose = int(input("Choose a position again to draw in from 1-9"))-1

        print(grid)

    if turn == 1:
        # Player input 2
        position_choose = int(input("Choose a position to draw in from 1-9"))-1
        while True:
            if grid[position_choose] != 10 and 11:
                grid[position_choose] = PLAYER2
                break
            else:
                position_choose = int(input("Choose a position again to draw in from 1-9"))-1
        print(grid)

    turn = turn + 1
    turn = turn % 2

print("GAME OVER!")





