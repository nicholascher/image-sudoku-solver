import cv2
import numpy as np

import pytesseract
from PIL import Image

import solver

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def fix_square(countours):

  # Returns the four corners of the square and returns it as a 4 x 2 arr in the order
  # Top left, Top right, Btm right, Btm left 

  # Input countour arr is 4 x 1 x 2, this sets it to a 4 x 2 array for convienience
  countours = countours.reshape(4, 2)
  newSquare = np.zeros((4,2),dtype = np.float32)
  
  # Sums the arr. Max is btm right, min is top left coord
  add = countours.sum(1)

  newSquare[0] = countours[np.argmin(add)]
  newSquare[2] = countours[np.argmax(add)]

  # Take the diff btwn x an y coord, Min diff is top right, Max diff is btm left
  diff = np.diff(countours, axis = 1)

  newSquare[1] = countours[np.argmin(diff)]
  newSquare[3] = countours[np.argmax(diff)]

  return newSquare



def pre_process(img_name):

  base_folder = 'inputs/'

  img_path = base_folder + img_name
  img = cv2.imread(img_path)
  
  # Making the image greyscale so its more readable by the OCR

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (5, 5), 0)
  thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
	
  return (gray, thresh)

def find_puzzle(img_name):
  
  gray, thresh = pre_process(img_name)
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  biggest = None 
  max_area = 0

  # Finding the largest square in the image. The size of the largest square should be at least
  # half the area of the img 

  for i in contours: 
    area = cv2.contourArea(i)
    if area > gray.size / 2: 
      peri = cv2.arcLength(i, True)
      approx = cv2.approxPolyDP(i, 0.02*peri, True)
      if area > max_area and len(approx == 4):
        biggest = approx
        max_area = area

  if biggest is not None:
    biggest = fix_square(biggest)

    # My target is a 450 x 450 img
    target_img = np.array([ [0,0],[449,0],[449,449],[0,449] ], np.float32)

    retval = cv2.getPerspectiveTransform(biggest, target_img)
    warped_img = cv2.warpPerspective(gray, retval, (450,450))

    return warped_img
  
  

def split_cells(img_name):

  board = np.zeros((9, 9), np.uint8)

  warped_img = find_puzzle(img_name)

  smooth = cv2.GaussianBlur(warped_img,(3,3),3)
  thresh = cv2.adaptiveThreshold(smooth,255,0,1,5,2)

  # thresh = cv2.adaptiveThreshold(smooth, 252, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 61)
  kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
  erode = cv2.erode(thresh,kernel,iterations =1)
  dilate =cv2.dilate(erode,kernel,iterations =1)

  for i in range(0, 9):
    for j in range(0, 9):

      roi = dilate[i * 50 + 8: i * 50 + 45, j * 50 + 12: j * 50 + 40]

      # cv2.imshow("test", roi)
      # cv2.waitKey(0)
      # cv2.destroyAllWindows

      
      number = pytesseract.image_to_string(roi, config="--psm 10")

      number = ''.join(filter(str.isdigit, number))

      if not number:
          number = '0'

      

      board[i][j] = int(number)
      
  return board


