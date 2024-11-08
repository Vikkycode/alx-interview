#!/usr/bin/python3
"""N queens puzzle."""
import sys


def print_board(board):
    """Prints the board."""
    for row in board:
        print(" ".join(["Q" if col else "." for col in row]))
    print()


def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at board[row][col]."""
    # Check row
    for i in range(N):
        if board[row][i]:
            return False

    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """Solves the N Queens problem using backtracking."""
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack


def solve_nqueens(N):
    """Solves the N Queens problem and prints all solutions."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
