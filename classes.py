class Player:

    def __init__(self, name, color, plrID):
        self.name = name
        self.color = color
        self.points = 0
        self.plrID = plrID

    def addPoints(points):
        if self.points == 0:
            self.points = points
        else:
            self.points += points

class Weight:

    def __init__(self, weight, location, ownerID):
        self.objectID = 1
        self.weight = weight
        self.location = location ## [x,y], x=scale, y=spot on scale
        self.ownerID = ownerID

    def changeOwner(self, newownerID):
        if self.ownerID != newownerID:
            self.ownerID = newownerID

class Scale:

    def __init__(self, length, scaleID, location=0):
        self.objectID = 0
        self.length = length
        self.scaleID = scaleID
        self.location = location
        self.contains = []
        self.centerCoordinates = 0

    def addWeights(self, weight):
        self.weights.append(weight)
        self.mass += weight.weight
        self.balance += int(weight.location[1])
