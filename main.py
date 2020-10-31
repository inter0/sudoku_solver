def solve(sudoku):
    #because I only insert valid numbers I can return if the sudoku is finished
    if finished(sudoku):
        return True
    
    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            #go through the sudoku and search for empty fields, means find fields that yield 0
            if sudoku[row][col] == 0:
                for i in range(1, 10):
                    #only insert valid numbers
                    if valid(sudoku, i, row, col):
                        sudoku[row][col] = i
                    else:
                        continue
                    #recursivly call the solve method to solve the sudoku with one valid number inserted in an empyt field
                    #if solve returned True, it means that the sudoku is finished and only valid numbers were inserted, so return True
                    if solve(sudoku):
                        return True

                #if there are no (more) valid numbers for this field reset the field and return False
                sudoku[row][col] = 0
                return False
    #dunno return, useless I guess
    return True


#check if the sudoku is valid 
def valid(sudoku, num, x, y):
    #checking row and col
    for i in range(len(sudoku)):
        if sudoku[x][i] == num and i != y:
            return False
        if sudoku[i][y] == num and i != x:
            return False

    #checking the fields
    minCol = (y // 3) * 3
    maxCol = minCol + 3
    minRow = (x // 3) * 3
    maxRow = minRow + 3

    for row in range(minRow, maxRow):
        for col in range(minCol, maxCol):
            if sudoku[row][col] == num and row != x and col != y:
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

    sudoku2 =   [[7, 8, 5, 4, 3, 0, 1, 2, 0],
                [6, 0, 0, 0, 7, 5, 0, 0, 9],
                [0, 0, 0, 6, 0, 1, 0, 7, 8],
                [0, 0, 7, 0, 4, 0, 2, 6, 0],
                [0, 0, 1, 0, 5, 0, 9, 3, 0],
                [9, 0, 4, 0, 6, 0, 0, 0, 5],
                [0, 7, 0, 3, 0, 0, 0, 1, 2],
                [1, 2, 0, 0, 0, 7, 4, 0, 0],
                [0, 4, 9, 2, 0, 6, 0, 0, 7]]

    sudoku = sudoku1

    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            if sudoku[row][col] != 0:
                if not valid(sudoku, sudoku[row][col], row, col):
                    print("Given Sudoku is not in a valid state!\nExiting Program")
                    exit()
    
    print("Given Sudoku")
    print("-"*27)
    for row in sudoku:
        print(row)
    print("-"*27)

    solve(sudoku)

    print("\nSolution")
    print("-"*27)
    for row in sudoku:
        print(row)
    print("-"*27)