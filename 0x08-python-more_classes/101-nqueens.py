#!/usr/bin/python3
"""Define N queens."""

import sys


def in_board(n):
    """Initialise a n * n board."""

    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)

def board_inside(board):
    """return copy of deep chessboard."""
    if isinstance(board, list):
        return list(map(board_inside, board))
    return (board)

def getting_solution(board):
    """Return list of lists representation."""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                solution.append([i, j])
                break
    return (solution)

def xingout(board, row, col):
    """Gives out spots on a chess board."""

    for j in range(col + 1, len(board)):
        board[row][j] = "X"
    for j in range(col - 1, -1, -1):
        board[row][j] = "X"
    for i in range(row + 1, len(board)):
        board[i][col] = "X"
    for i in range(row - 1, -1, -1):
        board[i][col] = "X"
    j = col + 1
    for i in range(row + 1, len(board)):
        if j >= len(board):
            break
        board[i][j] = "X"
        j += 1
    j = col - 1
    for i in range(row - 1, -1, -1):
        if j < 0:
            break
        board[i][j]
        j -= 1
    j = col + 1
    for i in range(row - 1, -1, -1):
        if j >= len(board):
            break
        board[i][j] = "X"
        j += 1
    j = col - 1
    for i in range(row + 1, len(board)):
        if j < 0:
            break
        board[i][j] = "X"
        j -= 1
def recursive_solve(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(getting_solution(board))
        return (solutions)

    for j in range(len(board)):
        if board[row][j] == " ":
            tmp_board = board_inside(board)
            tmp_board[row][j] = "Q"
            xingout(tmp_board, row, j)
            solutions = recursive_solve(tmp_board, row + 1, 
                    queens + 1, solutions)
            return (solutions)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = in_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for game in solutions:
        print(game)
