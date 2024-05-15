#!/usr/bin/python3
"""
 solves the N queens problem
"""


import sys


def printSolution(board):
    """
    prints the current arrangement of queens 
    on the chessboard. 
    It iterates through the board (a 2D list) and 
    prints each cell’s value (0 or 1)
    """
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col):
    """
    checks if it’s safe to place a queen at position (row, col) 
    on the board. 
    It verifies that no other queens threaten the current positio
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
        for x, y in zip(range(row, -1, -1), range(i, -1, -1)):
            if board[x][y] == 1:
                return False
        for x, y in zip(range(row, N), range(i, -1, -1)):
            if board[x][y] == 1:
                return False
    return True

def solveNQUtil(board, col):
    """
    If col exceeds the board size, 
    it means we’ve found a solution, 
    so it returns True.Otherwise, 
    it tries to place a queen in each row of the current column
    """
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solveNQ():
    """
    initializes the board and starts solving 
    the N-Queens problem. If no solution exists, 
    it prints an error message and exits
    """
    board = [[0] * N for _ in range(N)]
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        sys.exit(1)
    printSolution(board)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solveNQ()
    except ValueError:
        print("N must be a number")
        sys.exit(1)

