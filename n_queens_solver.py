from itertools import permutations
from chess_board import ChessBoard

class NQueensSolver:
    def __init__(self, board_size):
        self.board_size = board_size
        self.chess_board = ChessBoard(board_size)

    def is_safe(self, permutation):
        for row in range(len(permutation)):
            for column in range(row + 1, len(permutation)):
                if abs(row - column) == abs(permutation[row] - permutation[column]):
                    return False
        return True

    def print_solution(self, permutation):
        list_output = [0] * len(permutation)
        for i in range(len(permutation)):
            list_output[permutation[i] - 1] = i + 1
        return list_output

    def n_queen(self):
        for permutation in permutations(range(1, self.board_size + 1)):
            if self.is_safe(permutation):
                yield self.print_solution(permutation)
