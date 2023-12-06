import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from n_queens_solver import NQueensSolver

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
