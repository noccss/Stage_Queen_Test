from itertools import permutations

def chess_house_safe(permutation):
    for row in range(len(permutation)):
        for column in range(row + 1, len(permutation)):
            if abs(row - column) == abs(permutation[row] - permutation[column]):
                return False
    return True

def print_solution(permutation):
    list_output = [0] * len(permutation)
    for i in range(len(permutation)):
        list_output[permutation[i] - 1] = i + 1

    print(list_output, end=' ')

def nQueen(n):
    for permutation in permutations(range(1, n + 1)):
        if chess_house_safe(permutation):
            print_solution(permutation)

nQueen(4)
