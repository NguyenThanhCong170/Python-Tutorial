grid = [[" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "]]
        
def main():
    # while True:
    print()
    print('WELCOME to the GAME')
    play()
    # if game_over:
    #     break

def play():
    i = 0
    while True:
        draw()
        if i%2 == 0:
            
            mark = 'X'
            print()
            print("Player X's Turn")
            row = int(input('Please enter your row: '))
            if row < 1 or row > 12:
                print('ERROR: OUT OF ROW, PLEASE ENTER ROW BETWEEN 1 AND 12')
                continue
            checkrow = CheckRow(row)
            if checkrow == 'error':
                continue
            column = int(input('Please enter your column: '))
            if column < 1 or column > 12:
                print('ERROR: OUT OF COLUMN, PLEASE ENTER COLUMN BETWEEN 1 AND 12')
                continue
            checkcolumn = CheckColumn(column)
            if checkcolumn == 'error':
                continue
            if grid[row-1][column-1] != " ":
                print('ERROR: ALREADY CHOOSEN, PLEASE ENTER YOUR POSITION AGAIN')
                continue
            else:
                grid[row-1][column-1] = mark
            
            i+=1
        elif i%2 == 1:
            mark = 'O'
            print()
            print("Player O's Turn")
            row = int(input('Please enter your row: '))
            if row < 1 or row > 12:
                print('ERROR: OUT OF ROW, PLEASE ENTER ROW BETWEEN 1 AND 12')
                continue
            checkrow = CheckRow(row)
            if checkrow == 'error':
                continue
            column = int(input('Please enter your column: '))
            if column < 1 or column > 12:
                print('ERROR: OUT OF COLUMN, PLEASE ENTER COLUMN BETWEEN 1 AND 12')
                continue
            checkcolumn = CheckColumn(column)
            if checkcolumn == 'error':
                continue
            if grid[row-1][column-1] != " ":
                print('ERROR: ALREADY CHOOSEN, PLEASE ENTER YOUR POSITION AGAIN')
                continue
            else:
                grid[row-1][column-1] = mark
            i+=1
        game_over = CheckWinner(mark)
        if i == 12*12-1:
            print('DRAW !!!')
            break
        if i > 30:
            wanna_draw = input('DRAW ? (type draw to draw, else type anything): ')
            if wanna_draw == 'draw':
                print('DRAW !!!')
                break
        if game_over == 'over':
            draw()
            break
            

def draw():
    print()
    print('     1   2   3   4   5   6   7   8   9   10  11  12')
    print('   +---+---+---+---+---+---+---+---+---+---+---+---+')
    z=1
    for x in grid:
        if z<10:
            print(z,end='  ')
            print('|',end='')
            for y in x:
                print(' ' + y + ' |',end="")
            print()
            print('   +---+---+---+---+---+---+---+---+---+---+---+---+')
            z+=1
        else: 
            print(z,end=' ')
            print('|',end='')
            for y in x:
                print(' ' + y + ' |',end="")
            print()
            print('   +---+---+---+---+---+---+---+---+---+---+---+---+')
            z+=1
def CheckRow(row):
    for x in grid:
        if x[0] != " " and x[1] != " " and x[2] != " " and x[3] != " " and x[4] != " " and x[5] != " " and x[6] != " " and x[7] != " " and x[8] != " " and x[9] != " " and x[10] != " " and x[11] != " " and row-1 == x:
            print('ERROR: FULL OF ROW, PLEASE CHOOSE ANOTHER ROW')  
            return 'error'


def CheckColumn(column):
    for y in range(12):
        if grid[0][y] != " " and grid[1][y] != " " and grid[2][y] != " " and grid[3][y] != " " and grid[4][y] != " " and grid[5][y] != " " and grid[6][y] != " " and grid[7][y] != " " and grid[8][y] != " " and grid[9][y] != " " and grid[10][y] != " " and grid[11][y] != " " and column == y:
            print('ERROR: FULL OF COLUMN, PLEASE CHOOSE ANOTHER COLUMN')  
            return 'error'


def CheckError():
    return 0

def CheckWinner(mark):
    # Win by rows
    for row in grid:
        for index in range(8):
            if row[index] == row[index+1] and row[index] == row[index+2] and row[index] == row[index+3] and row[index] == row[index+4] and row[index] == mark:
                print()
                print(f'PLAYER {mark} IS THE WINNER')
                print()
                print('GAME OVER')
                return 'over'
    # Win by columns
    for index in range(12):
        for row in range(8):
            if grid[row][index] == grid[row+1][index] and grid[row][index] == grid[row+2][index] and grid[row][index] == grid[row+3][index] and grid[row][index] == grid[row+4][index] and grid[row][index] == mark:
                print()
                print(f'PLAYER {mark} IS THE WINNER')
                print()
                print('GAME OVER')
                return 'over'
    # Win by right diagonal line
    for x in range(8):
        for y in range(8):
            if grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x+2][y+2] and grid[x][y] == grid[x+3][y+3] and grid[x][y] == grid[x+4][y+4] and grid[x][y] == mark:
                print()
                print(f'PLAYER {mark} IS THE WINNER')
                print()
                print('GAME OVER')
                return 'over'
    # Win by left diagonal line
    for x in range(8):
        for y in range(4,12):
            if grid[x][y] == grid[x+1][y-1] and grid[x][y] == grid[x+2][y-2] and grid[x][y] == grid[x+3][y-3] and grid[x][y] == grid[x+4][y-4] and grid[x][y] == mark:
                print()
                print(f'PLAYER {mark} IS THE WINNER')
                print()
                print('GAME OVER')
                return 'over'
    return 'play'

if __name__ == '__main__':
    main()


