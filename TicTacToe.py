PLAYER1 = 1
PLAYER2 = 2

#STUCKKKKKK
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def is_valid_location(grid,position_choose):
    print(position_choose)
    for y in range(3):
        for x in range(3):
            if grid[y][x] == position_choose:
                print(grid[0][0])
                return position_choose

            else:
                position_choose2 = int(input("Choose a different position to draw in from 1-9"))
                print(position_choose2)
                return is_valid_location(grid, position_choose2)

print(grid)
print(grid[0][0])
turn = 0
game_over = False

while not game_over:
    if turn == 0:
        # Player input 1
        position_choose = int(input("Choose a position to draw in from 1-9"))
        is_valid_location(grid, position_choose)
        position_grid = is_valid_location(grid, position_choose)

        if position_grid == 1:
            grid[0][0] = "x"
        elif position_grid == 2:
            grid[0][1] = "x"
        elif position_grid == 3:
            grid[0][2] = "x"
        elif position_grid == 4:
            grid[1][0] = "x"
        elif position_grid == 5:
            grid[1][1] = "x"
        elif position_grid == 6:
            grid[1][2] = "x"
        elif position_grid == 7:
            grid[2][0] = "x"
        elif position_grid == 8:
            grid[2][1] = "x"
        elif position_grid == 9:
            grid[2][2] = "x"
        print(grid)

    if turn == 1:
        # Player input 2
        print("hello")
        position_choose = int(input("Choose a position to draw in from 1-9"))
        is_valid_location(grid, position_choose)
        position_grid = is_valid_location(grid, position_choose)
        print(position_grid)

        if position_grid == 1:
            grid[0][0] = "o"
        elif position_grid == 2:
            grid[0][1] = "o"
        elif position_grid == 3:
            grid[0][2] = "o"
        elif position_grid == 4:
            grid[1][0] = "o"
        elif position_grid == 5:
            grid[1][1] = "o"
        elif position_grid == 6:
            grid[1][2] = "o"
        elif position_grid == 7:
            grid[2][0] = "o"
        elif position_grid == 8:
            grid[2][1] = "o"
        elif position_grid == 9:
            grid[2][2] = "o"
        print(grid)
    turn = turn + 1
    turn = turn % 2

print(grid)





