class Player:

    def __init__(self, name, color, plrID):
        self.name = name
        self.color = color
        self.points = 0
        self.plrID = plrID

class Weight:

    def __init__(self, mass, location, ownerID):
        self.objectID = 1
        self.mass = mass
        self.location = location ## [x,y], x=scale, y=spot on scale
        self.ownerID = ownerID

    def changeOwner(self, newownerID):
        if self.ownerID != newownerID:
            self.ownerID = newownerID

class Scale:

    def __init__(self, length, scaleID, location=[0,0]):
        self.objectID = 0
        self.length = length
        self.scaleID = scaleID
        self.location = location
        self.contains = []
        self.weight
        self.centerCoordinates = 0

    def addWeights(self, weight):
        self.contains.append(weight)
        self.mass += weight.mass
        self.balance += int(weight.location[1])
