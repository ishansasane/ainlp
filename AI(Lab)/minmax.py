# Tic Tac Toe - Predict 7th move from a board with 6 moves using Minimax
from typing import List, Tuple, Optional

Board = List[List[str]]

def print_board(board: Board) -> None:
    for r in range(3):
        print(" | ".join(board[r]))
        if r < 2:
            print("-" * 5)
    print()

def empty_cells(board: Board) -> List[Tuple[int, int]]:
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def winner(board: Board) -> Optional[str]:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_terminal(board: Board) -> bool:
    return winner(board) is not None or not empty_cells(board)

def score(board: Board, depth: int, ai: str, human: str) -> int:
    win = winner(board)
    if win == ai:
        return 10 - depth
    elif win == human:
        return depth - 10
    return 0

def minimax(board: Board, depth: int, is_max: bool,
            ai: str, human: str, alpha: int, beta: int) -> Tuple[int, Optional[Tuple[int, int]]]:
    if is_terminal(board):
        return score(board, depth, ai, human), None

    best_move = None
    if is_max:
        max_eval = -1000
        for r, c in empty_cells(board):
            board[r][c] = ai
            eval_score, _ = minimax(board, depth + 1, False, ai, human, alpha, beta)
            board[r][c] = " "
            if eval_score > max_eval:
                max_eval, best_move = eval_score, (r, c)
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = 1000
        for r, c in empty_cells(board):
            board[r][c] = human
            eval_score, _ = minimax(board, depth + 1, True, ai, human, alpha, beta)
            board[r][c] = " "
            if eval_score < min_eval:
                min_eval, best_move = eval_score, (r, c)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def best_move(board: Board, ai: str, human: str) -> Tuple[int, int]:
    _, move = minimax(board, 0, True, ai, human, -1000, 1000)
    return move

def predict_7th_move(initial_board: Board, current_player: str):
    human, ai = ("X", "O") if current_player == "X" else ("O", "X")

    print("Initial Board:")
    print_board(initial_board)

    r, c = best_move(initial_board, current_player, ai if current_player == human else human)
    initial_board[r][c] = current_player

    print(f"Predicted 7th Move: {current_player} -> ({r+1},{c+1})")
    print("\nFinal Board:")
    print_board(initial_board)

if __name__ == "__main__":
    
    board = [
        ["X", "O", "X"],
        [" ", "O", " "],
        [" ", "X", " "]
    ]
    predict_7th_move(board, "X")
