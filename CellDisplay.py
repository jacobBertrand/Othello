import Cell
import pygame


class CellDisplay:

    surface = pygame.Surface
    screen = pygame.display
    cell = Cell.Cell
    green = (0, 128, 0)
    light_green = (0, 255, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    useColor = white
    size = (0, 0)
    pos = (0, 0)
    isWhite = True
    isEmpty = True

    def __init__(self, x, y, w, h, screen, cell):
        self.size = (w, h)
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.green)
        self.screen = screen
        self.cell = cell
        self.pos = (x, y)
        self.screen.blit(self.surface, self.pos)

    def updateCellDisplay(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.pos[0] + self.size[0] > mouse[0] > self.pos[0] and\
        self.pos[1] + self.size[1] > mouse[1] > self.pos[1] and self.cell.GetIsEmpty():
            self.surface.fill(self.light_green)

            if click[0] == 1:
                return True
        else:
            self.surface.fill(self.green)

        if self.cell.GetIsWhite():
            self.useColor = self.white
        else:
            self.useColor = self.black

        pos = (0, 0)
        if not self.cell.GetIsEmpty():
            pygame.draw.circle(self.surface, self.useColor, (49, 49), 40)

        self.screen.blit(self.surface, self.pos)
        return False
