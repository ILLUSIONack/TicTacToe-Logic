PLAYER1 = 10
PLAYER2 = 11

#STUCKKKKKK
grid = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]


def is_valid_location(grid, position_choose, player):
    while True:
        if grid[position_choose] != 10 and 11:
            grid[position_choose] = player
            return player
        else:
            position_choose = int(input("Choose a position again to draw in from 1-9")) - 1
            is_valid_location(grid, position_choose, player)

def check_if_winner(grid, player):
    if grid[0] & grid[1] & grid[2] == player:
        return True
    if grid[3] & grid[4] & grid[5] == player:
        return True
    if grid[6] & grid[7] & grid[8] == player:
        return True
    return False
turn = 0
print(grid)

game_over = False

while not game_over:
    if turn == 0:
        # Player input 1
        position_choose = int(input("Choose a position to draw in from 1-9"))-1
        is_valid_location(grid, position_choose, PLAYER1)
        if check_if_winner(grid, PLAYER1):
            print("PLAYER 1 WINS")
            game_over = True
        print(grid)

    if turn == 1:
        # Player input 2
        position_choose = int(input("Choose a position to draw in from 1-9"))-1
        is_valid_location(grid, position_choose, PLAYER2)
        if check_if_winner(grid, PLAYER1):
            print("PLAYER 2 WINS")
            game_over = True
        print(grid)

    turn = turn + 1
    turn = turn % 2

print("GAME OVER!")





