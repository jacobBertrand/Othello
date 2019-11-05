import GameBoard
import Display

mainBoard = GameBoard.GameBoard()
mainDisplay = Display.Display(mainBoard)

isWhiteTurn = False

while mainDisplay.ContinueGame():
    if mainDisplay.UpdateDisplay(isWhiteTurn):
        isWhiteTurn = not isWhiteTurn

