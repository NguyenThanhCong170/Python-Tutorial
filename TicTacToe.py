grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

def main():
    start_game()
    taketurn()
    print('Game over')
def start_game():
    print('Welcome to TICTACTOE')
    DrawMark(grid,' ')
def taketurn():
    turn = 1
    gameover = False
    while not gameover:
        mark = ' '
        if turn %2 == 1:
            mark = 'X'
            print(mark + "'s turn")
        else:
            mark = 'O'
            print(mark + "'s turn")
        row = int(input('Enter your row (1,3): '))
        if row <1 or row > 3:
            print('Invalid Number ! Please Enter an number between 1-3')
            continue
        column = int(input('Enter your column (1,3): '))
        if column <1 or column > 3:
            print('Invalid Number ! Please Enter an number between 1-3')
        if grid[row-1][column-1] != " ":
            print('Please enter another position because this has already taken !')
            continue
        grid[row-1][column -1] = mark
        DrawMark(grid,mark)
        
        a = CheckWinner(mark)
        if a == 1:
            gameover = True
        if turn == 9:
            print("It's a tie")
            gameover =True
        turn+=1
def DrawMark(grid,mark):
    print()
    print('+---+---+---+')
    for a in grid:
        print('|',end="")
        for b in a:
            print(" " + b + " |",end="")
        print()
        print('+---+---+---+')

def CheckWinner(mark):
    for x in range(3):
        if grid[x][0] == grid[x][1] and grid[x][1] == grid[x][2] == mark:
            print(mark + "player Win")
            return 1
        elif grid[x][0] == grid[x][1] and grid[x][1] == grid[x][2]== mark:
            print(mark + "player Win")
            return 1
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]== mark:
        print(mark + "player Win")
        return 1
    elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]== mark:
        print(mark + "player Win")
        return 1
    return 0
        

if __name__ == "__main__":
    main()
