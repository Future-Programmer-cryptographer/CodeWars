from copy import deepcopy

def getSquare(row,column):
    return 3*(row//3)+(column//3)

board = [
    [None,7,None,None,None,5,4,None,None],
    [None,5,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,6],
    [4,None,None,None,None,7,None,3,None],
    [None,6,None,3,None,None,None,1,None],
    [9,None,None,1,None,2,7,4,None],
    [None,None,2,None,8,6,None,None,None],
    [None,4,None,7,3,None,None,6,None],
    [3,None,6,9,2,None,None,None,1]
]

valuesInRows = [set() for _ in range(9)]
valuesInColumns = [set() for _ in range(9)]
valuesInSquares = [set() for _ in range(9)]

# setup candidates
possibleValues = {1,2,3,4,5,6,7,8,9}
for rowNum,row in enumerate(board):
    for columnNum,element in enumerate(row):
        if element == None:
            board[rowNum][columnNum] = possibleValues.copy()

while True:

    previousBoard = deepcopy(board)

    for rowNum,row in enumerate(board):
        for columnNum,element in enumerate(row):
            if isinstance(element, int):
                valuesInRows[rowNum].add(element)
                valuesInColumns[columnNum].add(element)
                valuesInSquares[getSquare(rowNum,columnNum)].add(element)

    for rowNum,row in enumerate(board):
        for columnNum,element in enumerate(row):
            if isinstance(element, set):
                board[rowNum][columnNum] = element.difference(valuesInRows[rowNum])
                board[rowNum][columnNum] = board[rowNum][columnNum].difference(valuesInColumns[columnNum])
                board[rowNum][columnNum] = board[rowNum][columnNum].difference(valuesInSquares[getSquare(rowNum,columnNum)])

                if len(board[rowNum][columnNum]) == 1:
                    board[rowNum][columnNum] = list(board[rowNum][columnNum])[0]

    if board == previousBoard:
        break

print(board)