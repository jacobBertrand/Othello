import Cell


class GameBoard:

    Cells = [[], [], [], [], [], [], [], []]

    def __init__(self):
        for x in range(8):
            for y in range(8):
                self.Cells[y].append(Cell.Cell(True, False))

        self.Cells[3][3].SetIsEmpty(False)
        self.Cells[3][3].SetIsWhite(True)
        self.Cells[4][4].SetIsEmpty(False)
        self.Cells[4][4].SetIsWhite(True)
        self.Cells[3][4].SetIsEmpty(False)
        self.Cells[3][4].SetIsWhite(False)
        self.Cells[4][3].SetIsEmpty(False)
        self.Cells[4][3].SetIsWhite(False)

    def DrawBoard(self):
        newRow = ""
        for x in range(8):
            print(newRow)
            newRow = ""
            for y in range(8):
                if self.Cells[x][y].GetIsEmpty():
                    newRow += "E"
                else:
                    if self.Cells[x][y].GetIsWhite():
                        newRow += "W"
                    else:
                        newRow += "B"

    def PlacePiece(self, coordinates, isWhite):
        self.Cells[coordinates[0]][coordinates[1]].SetIsEmpty(False)
        self.Cells[coordinates[0]][coordinates[1]].SetIsWhite(isWhite)
