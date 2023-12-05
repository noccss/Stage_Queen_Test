import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from n_queens_solver import NQueensSolver
import math

SIZE_CHESSHOUSE = 50

class ChessBoardGUI:
    def __init__(self, board_size):
        # Initial pygame config
        pygame.init()
        self.board_size = board_size
        # Call class NQueensSolver and attribute to self.solver
        self.solver = NQueensSolver(board_size)
        self.solutions = list(self.solver.n_queen())
        self.current_solution_index = 0
        self.board = self.solutions[self.current_solution_index]
        self.screen = pygame.display.set_mode((board_size * SIZE_CHESSHOUSE, board_size * SIZE_CHESSHOUSE))
        self.queen_sprite = pygame.image.load("./asset/queen.png")
        pygame.display.set_caption("Stage N Quenn")
        pygame.display.set_icon(self.queen_sprite)
        self.queen_sprite = pygame.transform.scale(self.queen_sprite, (SIZE_CHESSHOUSE, SIZE_CHESSHOUSE))

    def draw_board(self):
        # Draws the chessboard according to the size specified for the board
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (col * SIZE_CHESSHOUSE, row * SIZE_CHESSHOUSE, SIZE_CHESSHOUSE, SIZE_CHESSHOUSE))

    def draw_queens(self):
        # Draws the queens according to the specified quantity
        for col, row in enumerate(self.board):
            self.screen.blit(self.queen_sprite, (col * SIZE_CHESSHOUSE, (row - 1) * SIZE_CHESSHOUSE))

    def next_solution(self):
        # Switches to the next solution.
        self.current_solution_index = (self.current_solution_index + 1) % len(self.solutions)
        self.board = self.solutions[self.current_solution_index]

    def display_solution_info(self):
        # Display on terminal the current solution list, and print how many solutions has.
        print(f"{self.board}")
        queen_count = len(set(self.board))
        if queen_count == 1:
            print("Explanation: Only one queen can be placed in the single cell available.")
        else:
            total_solutions = len(list(self.solver.n_queen()))
            print(f"Explanation: These are the {total_solutions} possible solutions.")

    def run(self):
        # Run the pygame loop to display the chessboard
        clock = pygame.time.Clock()
        running = True
        current_solution_text_displayed = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                # After pressing the keyboard spacebar, it switches to the next solution.
                elif event.type == KEYDOWN and event.key == K_SPACE:
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
        """
        Before starting the execution in pygame, a question will be asked about how many queens you want to insert, and this will determine the 
        size of the matrix as well. 
            If it's less than 1, a print will be made indicating that the list is empty. 
            If it's equal to 2 or 3, a print will be made stating that the chosen number has no solution. 
            If it's greater than or equal to 11, there is a chance that the machine may not support it, so an approximate calculation of 
        factorization is performed without checking the possibilities of the queen.
        """
        while True:
            try:
                n = int(input("Enter the N of the chessboard and the number of queens: "))
                if n < 1:
                    print("Empty List []")
                    print("Please, enter number positive more than 1.")
                elif n == 2 or n == 3:
                    print("There are no solutions for a chessboard of n 2 or 3. Please enter another number.")
                else:
                    # To perform calculations for large factorials, the Stirling formula was used. This allows us to approximate the value of solutions without consuming excessive machine memory.
                    # n!≈ sqrt2πn (n/e)^n
                    if n >= 11:
                        factorial_approximation = math.sqrt(2 * math.pi * n) * ((n / math.e) ** n)
                        print(f"For a chessboard of n {n}, the approximate number of possible solutions" 
                                f"is {factorial_approximation:.2e} (in scientific notation).")
                    else:
                        return n
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
            except OverflowError:
                print("Result is too large. Please enter another number")

def main():
    board_size = ChessBoardInput.get_user_input()
    gui = ChessBoardGUI(board_size)
    gui.run()

if __name__ == "__main__":
    main()
