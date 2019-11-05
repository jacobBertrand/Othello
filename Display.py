import CellDisplay
import GameBoard
import pygame
pygame.init()


class Display:

    screen = pygame.display
    Cells = [[], [], [], [], [], [], [], []]
    gameBoard = GameBoard.GameBoard

    def __init__(self, gameBoard):
        self.screen = pygame.display.set_mode([800, 800])
        black = (0, 0, 0)
        self.screen.fill(black)
        self.gameBoard = gameBoard

        for x in range(8):
            for y in range(8):
                self.Cells[x].append\
                    (CellDisplay.CellDisplay(1 + (100 * y), 1 + (100 * x), 98, 98, self.screen, gameBoard.Cells[x][y]))

    def ContinueGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        return True

    def UpdateDisplay(self, isWhite):
        for x in range(8):
            for y in range(8):
                if self.Cells[x][y].updateCellDisplay():
                    self.gameBoard.PlacePiece((x, y), isWhite)
                    return True

        pygame.display.update()
        return False
