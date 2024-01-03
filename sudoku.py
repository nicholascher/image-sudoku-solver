import imgprocessing
import solver


def editBoard(board, x, y, newValue):

  board[x][y] = newValue

  return board

def isValidInput(x, y, value):

  if x > 9 or x < 0 or y > 9 or y < 0 or value > 9 or value < 0: 
    print("Invalid inputs! ")
    return False
  else:
    return True 

def checkBoard(board):

  solver.printBoard(board)  
  response = input("Is this board correct? (Y/N): ")

  if response == "Y":
    solver.solve(board)

  elif response == "N":

    isValid = False

    while not isValid:
       
      x, y, value = input("Enter the x, y coordinates followed by the correct value (separated by space): ").split()

      x = int(x)
      y = int(y)
      value = int(value)

      isValid = isValidInput(x, y, value)
       

    newBoard = editBoard(board, x, y, value)
    checkBoard(newBoard)

  else: 
    print("Please enter a valid input! \n")
    checkBoard(board)


def main():
    img_name = input("Enter the name of the Sudoku puzzle image file: ")

    board = imgprocessing.split_cells(img_name)

    checkBoard(board)

if __name__ == "__main__":
    main()
