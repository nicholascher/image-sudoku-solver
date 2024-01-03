import numpy as np

gridSize = 9

board = [
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

unsolvable_board = [
    [0, 0, 9, 0, 2, 8, 7, 0, 0],
    [8, 0, 6, 0, 0, 4, 0, 0, 5],
    [0, 0, 3, 0, 0, 0, 0, 0, 4],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 7, 1, 3, 4, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [3, 0, 0, 0, 0, 0, 5, 0, 0],
    [9, 0, 0, 4, 0, 0, 8, 0, 7],
    [0, 0, 1, 2, 5, 0, 3, 0, 0]
]



def solve(board): 

  if solveBoard(board): 
    print("Solved Board: \n")
    printBoard(board)
  else:
     print("This board cannot be solved! :(")

    
def printBoard(board):
  for i in range(len(board)):
      if i % 3 == 0 and i != 0:
          print("-" * (len(board) * 2 + 5))
      
      for j in range(len(board[i])):
          if j % 3 == 0 and j != 0:
              print("|", end=" ")
              
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

def findEmpty(board): 
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
          return (i, j)

  return None


def solveBoard(board):
  emptySquare = findEmpty(board)
  if not emptySquare:
      return True
  else:
      row, col = emptySquare

  for i in range(1,10):
      if isValid(board, i, row, col):
          board[row][col] = i

          if solveBoard(board):
              return True

          board[row][col] = 0

  return False

      