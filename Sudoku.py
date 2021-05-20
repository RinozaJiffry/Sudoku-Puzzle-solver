## We are using back tracking algorithm here

## Backtracking is an algorithmic-technique for solving problems recursively by
# trying to build a solution incrementally, one piece at a time, removing those solutions
# that fail to satisfy the constraints of the problem at any point of time (by time, here,
# is referred to the time elapsed till reaching any level of the search tree).

## Steps of Sudoku solving (backtracking algorithm)
    # 1. Pick an empty box
    # 2. Try all value by putting them in
    # 3. Find the value which works on that box
    # 4. Then move to next box Repeat the steps again
    # 5.Backtrack

question = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

## Back track algorithm
def solving(qs):
    ## Finding the empty Box
    findEmpty = finding_emptyBox(qs)
    if not findEmpty:
        return True
    else:
        row, column = findEmpty

    for i in range(1,10):
        if correctAnswer(qs, i, (row, column)):
            qs[row][column] = i

            if solving(qs):
                return True

            qs[row][column] = 0

    return False

## Cheking the question is valid or not
def correctAnswer(qs, number, position):
    # Now we are Checking the row
    for i in range(len(qs[0])):
        if qs[position[0]][i] == number and position[1] != i:
            return False

    ## Next we are checking the columns
    for i in range(len(qs)):
        if qs[i][position[1]] == number and position[0] != i:
            return False

    ## Finding which box we are in
    boxX = position[1] // 3
    boxY = position[0] // 3

    ## We are going through the box to avoid same elements in the box
    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if qs[i][j] == number and (i, j) != position:
                return False

    return True

# Printing the sudoku question
def print_question(qs):
    ## After every 3 rows Printing the vertical line
    ## i = rows
    for i in range(len(qs)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        ## After every 3 columns Printing the horizontal line
        ## j = columns
        for j in range(len(qs[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(qs[i][j])
            else:
                print(str(qs[i][j]) + " ", end="")


def finding_emptyBox(qs):
    for i in range(len(qs)):
        for j in range(len(qs[0])):
            if qs[i][j] == 0:
                return (i, j)  # row, col

    return None

print_question(question)
solving(question)
print(" ")
print("************************************")
print("***********Solved Sudoku************")
print("************************************")
print(" ")
print_question(question)