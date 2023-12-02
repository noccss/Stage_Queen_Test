class ChessBoard:
    def __init__(self, size):
        self.size = size

    def is_valid_position(self, permutation):
        for row in range(len(permutation)):
            for column in range(row + 1, len(permutation)):
                if abs(row - column) == abs(permutation[row] - permutation[column]):
                    return False
        return True

    def print_solution(self, permutation):
        list_output = [0] * len(permutation)
        for i in range(len(permutation)):
            list_output[permutation[i] - 1] = i + 1

        print(list_output, end=' ')
