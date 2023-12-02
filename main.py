import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from n_queens_solver import NQueensSolver
import math

CELL_SIZE = 50

class ChessBoardGUI:
    def __init__(self, board_size):
        self.board_size = board_size
        self.solver = NQueensSolver(board_size)
        self.solutions = list(self.solver.n_queen())
        self.current_solution_index = 0
        self.board = self.solutions[self.current_solution_index]
        self.screen = pygame.display.set_mode((board_size * CELL_SIZE, board_size * CELL_SIZE))
        self.queen_sprite = pygame.image.load("./asset/queen.png")
        pygame.display.set_icon(self.queen_sprite)
        self.queen_sprite = pygame.transform.scale(self.queen_sprite, (CELL_SIZE, CELL_SIZE))

    def draw_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_queens(self):
        for col, row in enumerate(self.board):
            self.screen.blit(self.queen_sprite, (col * CELL_SIZE, (row - 1) * CELL_SIZE))

    def next_solution(self):
        self.current_solution_index = (self.current_solution_index + 1) % len(self.solutions)
        self.board = self.solutions[self.current_solution_index]

    def display_solution_info(self):
        print(f"{self.board}")

        queen_count = len(set(self.board))
        if queen_count == 1:
            print("Explanation: Only one queen can be placed in the single cell available.")
        else:
            total_solutions = len(list(self.solver.n_queen()))
            print(f"Explanation: These are the {total_solutions} possible solutions.")

    def run(self):
        clock = pygame.time.Clock()
        running = True
        current_solution_text_displayed = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.next_solution()
                        current_solution_text_displayed = False

            self.draw_board()
            self.draw_queens()
            pygame.display.flip()

            if not current_solution_text_displayed:
                self.display_solution_info()
                current_solution_text_displayed = True

            clock.tick(5)

        pygame.quit()

class ChessBoardInput:
    @staticmethod
    def get_user_input():
        while True:
            try:
                size = int(input("Enter the size of the chessboard and the number of queens: "))
                if size < 1:
                    print("Please enter a positive integer.")
                elif size == 2 or size == 3:
                    print("There are no solutions for a chessboard of size 2 or 3. Please enter another number.")
                else:
                    if size >= 11:
                        factorial_approximation = math.sqrt(2 * math.pi * size) * ((size / math.e) ** size)
                        print(f"Note: For a chessboard of size {size}, the approximate number of possible solutions "
                              f"is {factorial_approximation:.2e} (in scientific notation).")
                    else:
                        return size
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

def main():
    board_size = ChessBoardInput.get_user_input()

    gui = ChessBoardGUI(board_size)
    gui.run()

if __name__ == "__main__":
    main()
