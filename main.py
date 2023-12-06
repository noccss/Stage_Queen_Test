import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_RETURN, K_BACKSPACE
import math
from chessboard_gui import ChessBoardGUI

class ChessBoardInput:
    @staticmethod
    def validate_input(user_input):
        """
            Before starting the execution in pygame, a question will be asked about how many queens you want to insert, and this will determine the 
            size of the matrix as well. 
                If it's less than 1, a print will be made indicating that the list is empty. 
                If it's equal to 2 or 3, a print will be made stating that the chosen number has no solution. 
                If it's greater than or equal to 11, there is a chance that the machine may not support it, so an approximate calculation of 
            factorization is performed without checking the possibilities of the queen.
        """
        try:
            n = int(user_input)
            error_message = ""
            if n < 1:
                error_message = "Empty List []\nPlease, enter number positive more than 1."
            elif n == 2 or n == 3:
                error_message = "There are no solutions for a chessboard of n\n 2 or 3. Please enter another number."
            else:
                # To perform calculations for large factorials, the Stirling formula was used. This allows us to approximate the value of solutions without consuming excessive machine memory.
                # n!≈ sqrt2πn (n/e)^n
                if n >= 11:
                    factorial_approximation = math.sqrt(2 * math.pi * n) * ((n / math.e) ** n)
                    error_message = (f"The approximate number possible solutions \nof {n} is {factorial_approximation:.2e} (in scientific notation).")
            if error_message != "":
                print(error_message)
                return None, error_message
            return n, None
        except ValueError:
            return None, "Invalid input. Please enter a positive integer."
        except OverflowError:
            return None, "Result is too large. Please enter another \nnumber"

    @staticmethod
    def show_text(screen, text, position, font_size):
        # Pygame configuration to show text in GUI
        text_splited = text.split('\n')
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text_splited[0], True, (0, 0, 0))
        if '\n' in text:
            # If text has \n so break the lines with the news values
            new_position = (10, 140)
            new_text_surface = font.render(text_splited[1], True, (0, 0, 0))
            screen.blit(new_text_surface, new_position)
        screen.blit(text_surface, position)
            
    @staticmethod
    def get_input():
        # Configure pygame window to get the input value
        pygame.init()
        screen = pygame.display.set_mode((450, 200))
        pygame.display.set_icon(pygame.image.load("./asset/queen.png"))
        pygame.display.set_caption("Stage N Quenn")
        input_text = ""
        error_message = ""
        input_active = True
        clock = pygame.time.Clock()

        # Verify if user input is valid to start N Queen solution
        while input_active:
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (0, 0, 0), (50, 50, 300, 50), 2)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return None
                elif event.type == KEYDOWN:
                    # On keyboard press Space or Enter to start the process
                    if event.key == K_SPACE or event.key == K_RETURN:
                        # Valid the input if n_queen is None, so get the error_message text
                        n_queen, error_message = ChessBoardInput.validate_input(input_text)
                        if n_queen is not None:
                            input_active = False
                            return n_queen
                    elif event.key == K_BACKSPACE:
                            input_text = ""
                            error_message = ""
                    else:
                        input_text += event.unicode
            # Show texts on interface
            ChessBoardInput.show_text(screen, "Choice N Queen in Chessboard", (20, 20), 36)
            ChessBoardInput.show_text(screen, input_text, (60, 60), 36)
            if error_message != "":
                ChessBoardInput.show_text(screen, error_message, (10, 120), 28)
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

def main():
    board_size = ChessBoardInput.get_input()
    if board_size is not None:
        gui = ChessBoardGUI(board_size)
        gui.run()

if __name__ == "__main__":
    main()
