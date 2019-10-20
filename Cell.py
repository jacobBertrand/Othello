class Cell:

    isEmpty = True
    isWhite = False

    def __init__(self, newIsEmpty, newIsWhite):
        self.isEmpty = newIsEmpty
        self.isWhite = newIsWhite

    def SetIsEmpty(self, newIsEmpty):
        self.isEmpty = newIsEmpty

    def SetIsWhite(self, newIsWhite):
        self.isWhite = newIsWhite

    def GetIsEmpty(self):
        return self.isEmpty

    def GetIsWhite(self):
        return self.isWhite
