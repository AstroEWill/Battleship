"Functions to coordinate game mechanics"
import random
class Ship:
        def __init__(self, name, length):
            self.name = name
            self.length = length
            self.hits = 0
            self.status = 1

        def checkStatus(self):
            if self.hits == self.length:
                return 0
            else:
                return 1
        
        def shipHit(self):
            self.hits += 1

            self.status = self.checkStatus()

            if self.status == 0:
                print(f'The enemy\'s {self.name} has sunk.')
            return self.status

def make_grid():
    genGrid = []
    shipLengths = [5,4,3,3,2]
    shipType = ['C','B','D','S','P']

    for i in range(0,10):
        genGrid.append(['~'] * 10)
    
    for n in range(len(shipLengths)):
        orientation = random.randint(0,1)
        if orientation: #1 represents a vertical orientation and 0 represents a horizontal orientation
            while True:
                startCol = random.randint(0,9)
                startRow = random.randint(0, 9 - shipLengths[n])
                
                transposeCheck = []
                for i in range(0,shipLengths[n]):
                    transposeCheck.append(genGrid[startRow+i][startCol])
                
                if transposeCheck == ['~'] * shipLengths[n]:
                    for i in range(0,shipLengths[n]):
                        genGrid[startRow+i][startCol] = shipType[n]
                    break
        else:
            while True:
                startCol = random.randint(0,9-shipLengths[n])
                startRow = random.randint(0,9)
                if list(genGrid[startRow][startCol:startCol+shipLengths[n]]) == ['~'] * shipLengths[n]:
                    for i in range(0,shipLengths[n]):
                        genGrid[startRow][startCol+i] = shipType[n]
                    break
        
    return genGrid

def shipCheck():
    carrier = Ship('Carrier',5)
    battleship = Ship('Battleship',4)
    destroyer = Ship('Destroyer',3)
    submarine = Ship('Submarine',3)
    patrol = Ship('Patrol Boat',2)

    shipList = [carrier, battleship, destroyer, submarine, patrol]
    abbrevList = ['C','B','D','S','P']

    numShots = 0
    numHits = 0
    shipSunk = 0

    numShips = 5