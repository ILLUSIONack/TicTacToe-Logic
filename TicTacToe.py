PLAYER1 = 1
PLAYER2 = 2

#STUCKKKKKK
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def is_valid_location(grid, position_choose):
    for y in range(3):
        for x in range(3):
            if grid[y][x] == position_choose:
                return position_choose

    return True


print(grid)
turn = 0
game_over = False

while not game_over:
    if turn == 0:
        # Player input 1
        position_choose = int(input("Choose a position to draw in from 1-9"))
        is_valid_location(grid, position_choose)
        position_grid = is_valid_location(grid, position_choose)
        if position_grid:
            position_choose = int(input("Choose a position to draw in from 1-9"))
            is_valid_location(grid, position_choose)

        if position_grid == 1:
            grid[0][0] = 10
        elif position_grid == 2:
            grid[0][1] = 10
        elif position_grid == 3:
            grid[0][2] = 10
        elif position_grid == 4:
            grid[1][0] = 10
        elif position_grid == 5:
            grid[1][1] = 10
        elif position_grid == 6:
            grid[1][2] = 10
        elif position_grid == 7:
            grid[2][0] = 10
        elif position_grid == 8:
            grid[2][1] = 10
        elif position_grid == 9:
            grid[2][2] = 10
    print(grid)

    if turn == 1:
        # Player input 2
        position_choose = int(input("Choose a position to draw in from 1-9"))
        is_valid_location(grid, position_choose)
        position_grid = is_valid_location(grid, position_choose)
        if position_grid:
            position_choose = int(input("Choose a position to draw in from 1-9"))
            is_valid_location(grid, position_choose)

        if position_grid == 1:
            grid[0][0] = 11
        elif position_grid == 2:
            grid[0][1] = 11
        elif position_grid == 3:
            grid[0][2] = 11
        elif position_grid == 4:
            grid[1][0] = 11
        elif position_grid == 5:
            grid[1][1] = 11
        elif position_grid == 6:
            grid[1][2] = 11
        elif position_grid == 7:
            grid[2][0] = 11
        elif position_grid == 8:
            grid[2][1] = 11
        elif position_grid == 9:
            grid[2][2] = 11
        print(grid)
    turn = turn + 1
    turn = turn % 2

print(grid)





