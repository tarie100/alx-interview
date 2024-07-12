#!/usr/bin/python3
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            # number of queens we are solving for
            board_size = int(sys.argv[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if board_size < 4:
            print("N must be at least 4")
            exit(1)

        # will hold current testing data
        currentSolution = [0 for x in range(board_size)]

        # found solutions
        solutions = []

        def isSafe(testRow, testCol):
            # no need to check for row 0
            if testRow == 0:
                return True

            for row in range(0, testRow):

                # check vertical
                if testCol == currentSolution[row]:
                    return False

                # diagonal
                if abs(testRow - row) == abs(testCol - currentSolution[row]):
                    return False

            # no attack found
            return True

        def placeQueen(row):
            global currentSolution, solutions, board_size
            for col in range(board_size):
                if not isSafe(row, col):
                    continue
                else:
                    currentSolution[row] = col
                    if row == (board_size - 1):
                        #  last row
                        solution = []
                        for i in range(len(currentSolution)):
                            solution.append([i, currentSolution[i]])
                        solutions.append(solution)
                    else:
                        placeQueen(row + 1)

        placeQueen(0)
        for solution in solutions:
            print(solution)
    else:
        print("Usage: nqueens N")
        exit(1)