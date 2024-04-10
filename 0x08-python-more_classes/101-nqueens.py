#!/usr/bin/python3
import sys
"""Define N queens."""


def in_board(n):
    """Initialise a n * n board"""

    board = []
    [board.append([]) for i in range (n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)

def board_inside(board):
    """return copy of deep chessboard"""
    if isinstance(board, list):
        return list(map(board_inside, board))
    return (board)

def getting_solution(board):
    """Return list of lists representation"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                solution.append([r, c])
                break
    return (solution)
def xingout(board, row, col):
    """Gives out spots on a chess board."""

    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        voard[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col -1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
def recursive_solve(board, row, queens, solutions):
    if queens == (len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xingout(tmp_board, row, c)
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

    board = in_board(int(sys.argv[1]))
    solutions = recursive_slve(board, 0, 0, [])
    for solving in solutions:
        print(sol)
