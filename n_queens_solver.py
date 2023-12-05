from itertools import permutations

class NQueensSolver:
    def __init__(self, board_size):
        self.board_size = board_size

    def is_valid_position(self, permutation):
        # Checking if the permutation is correct by verifying that no queen is attacking another.
        for row in range(len(permutation)):
            for column in range(row + 1, len(permutation)):
                if abs(row - column) == abs(permutation[row] - permutation[column]):
                    return False
        return True

    def take_all_solutions(self, permutation):
        # Return all solutions list formatted by [4, 3, 2, 1] for example
        list_output = [0] * len(permutation)
        for i in range(len(permutation)):
            list_output[permutation[i] - 1] = i + 1
        return list_output

    def n_queen(self):
        # Return permutations list with N Queens Solution
        for permutation in permutations(range(1, self.board_size + 1)):
            if self.is_valid_position(permutation):
                yield self.take_all_solutions(permutation)
