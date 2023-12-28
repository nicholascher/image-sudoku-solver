# Sudoku Solver using Image Processing

This Sudoku Solver is a Python-based application that utilizes image processing techniques to solve Sudoku puzzles. It can take an image of a Sudoku puzzle as input, extract the puzzle's digits, solve the puzzle, and output the solved Sudoku board.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [Example](#example)
- [Contributing](#contributing)

## Features

- **Image Input**: Accepts an image file (e.g., PNG, JPEG) containing a Sudoku puzzle.
- **Image Processing**: Uses OpenCV and pytesseract to process the image, detect digits, and extract the Sudoku board.
- **Sudoku Solving**: Applies an algorithm to solve the extracted Sudoku board.
- **Output**: Prints the solved Sudoku board to the console.

## Installation

To use this Sudoku Solver, follow these steps:

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/your_username/sudoku-solver-image.git
   ```

2. Install the required Python libraries:

   ```bash
   pip install numpy
   pip install opencv-python
   pip install pytesseract 
   ```

## Usage

1. Ensure you have an image file containing a Sudoku puzzle.
2. Run the `sudoku_solver.py` script:

   ```bash
   python sudoku_solver.py --image puzzle_image.png
   ```

   Replace `puzzle_image.png` with the path to your Sudoku puzzle image. Note that the image should be in the `Inputs` folder.

## Dependencies

- Python 3.x
- OpenCV
- pytesseract OCR
- NumPy

## How It Works

1. **Image Processing**:
   - Uses OpenCV to read and process the input image.
   - Applies image processing techniques (e.g., thresholding, contour detection) to isolate and extract the Sudoku puzzle grid.

2. **Digit Extraction**:
   - Detects digits within each cell of the Sudoku grid using contour detection and image segmentation.

3. **Sudoku Solving**:
   - Applies a Sudoku solving algorithm to fill in the blank cells of the puzzle.
   - The solver uses logic and backtracking techniques to find the solution.

4. **Output**:
   - Prints the solved Sudoku board to the console.

## Example

```bash
python sudoku_solver.py --image sudoku_puzzle.png
```

Output:

```
Solved Sudoku Puzzle:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## Contributing

Contributions to improve this Sudoku Solver are welcome! Feel free to open issues or submit pull requests.


