import numpy as np

gridSize = 9

board = np.array([
        [7, 0, 2, 0, 5, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [1, 0, 0, 0, 0, 9, 5, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 4, 3, 0, 0, 0, 7, 5, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 9, 7, 0, 0, 0, 0, 5],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 4, 0, 2, 0, 3]])

def solve(board): 

  if solveBoard(board): 
    printBoard(board)
  else:
     print("This board cannot be solved! :(")


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * (len(board) * 2 + 5))  # Add horizontal line every 3 rows
        
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Add vertical line every 3 columns
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")



def isNumberInRow(board, number, row):
  for i in range(0, gridSize):
    if board[row][i] == number:
      return True

  return False
    
def isNumberInCol(board, number, col):
  for i in range(0, gridSize):
    if board[i][col] == number:
      return True
      
  return False
    
def isNumberInBox(board, number, row, col):
  localRow = row - row % 3
  localCol = col - col % 3

  for i in range(localRow, localRow + 3):
    for j in range(localCol, localCol + 3):
      if board[i][j] == number:
        return True
      
  return False

def isValid(board, number, row, col):
  return (not isNumberInRow(board, number, row)) and (not isNumberInCol(board, number, col)) and (not isNumberInBox(board, number, row, col))


def solveBoard(board):
  for row in range(0, gridSize): 
    for col in range(0, gridSize):
      if board[row][col] == 0:
        for numToTry in range(1, gridSize + 1):
          if isValid(board, numToTry, row, col):
            board[row][col] = numToTry

            if solveBoard(board):
              return True
            else:
              board[row][col] = 0

        return False
  
  return True
      