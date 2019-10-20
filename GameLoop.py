import GameBoard

mainBoard = GameBoard.GameBoard()

mainBoard.DrawBoard()
print("")

isWhiteTurn = False

while True:

    coordinateInput = [0, 0]
    exitInput = ""

    keepGoing = True
    while keepGoing:
        try:
            coordinateInput[0] = int(input("Enter Row: "))
            coordinateInput[1] = int(input("Enter Column: "))
        except ValueError:
            print("Invalid Input")
            keepGoing = True
        else:
            if coordinateInput[0] < 0 or coordinateInput[0] > 7 or coordinateInput[1] < 0 or coordinateInput[1] > 7:
                keepGoing = True
                print("Please Enter Numbers Between 0 and 7")
            else:
                keepGoing = False

    mainBoard.PlacePice(coordinateInput, isWhiteTurn)
    mainBoard.DrawBoard()
    if isWhiteTurn:
        isWhiteTurn = False
    else:
        isWhiteTurn = True

    exitInput = input("Exit?(Y/N) ")
    exitInput = exitInput.upper()
    exitInput = exitInput.strip()

    if exitInput == 'Y':
        break
