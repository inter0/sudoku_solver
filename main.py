counter = 0

def solve(sudoku):
    global counter
    counter += 1
    print(counter)

    if finished(sudoku):
        return True
    
    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            if sudoku[row][col] == 0:
                for i in range(1, 10):
                    if valid(sudoku, i, row, col):
                        sudoku[row][col] = i

                    if solve(sudoku):
                        return True

                    sudoku[row][col] = 0

    return False


#check if the sudoku is valid 
def valid(sudoku, num, x, y):
    boolArr = [False]*9
    
    #checking row
    for i in range(9):
            number = sudoku[x][i] - 1
            if number >= 0:
                boolArr[number] = True

    if boolArr[num - 1]:
        return False                
                
    boolArr = [False]*9

    #checking column
    for i in range(9):
            number = sudoku[i][y] - 1
            if number >= 0:
                boolArr[number] = True

    if boolArr[num - 1]:
        return False 

    boolArr = [False]*9

    #checking the fields
    minCol = (y % 3) * 3
    maxCol = minCol + 3
    minRow = (x % 3) * 3
    maxRow = minRow + 3

    for row in range(minRow, maxRow):
        for col in range(minCol, maxCol):
            number = sudoku[row][col] - 1
            if number >= 0:
                boolArr[number] = True
        
    if boolArr[num - 1]:
        return False

    return True

def finished(sudoku):
    for row in sudoku:
        for col in row:
            if col == 0:
                return False
    
    return True


if __name__ == "__main__":
    sudoku1 =   [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    sudoku2 = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    for row in sudoku2:
        print(row)

    solve(sudoku2)

    print("")
    for row in sudoku2:
        print(row)