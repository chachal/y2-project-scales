class Player:

    def __init__(self, name, icon, plrID):
        self.name = name
        self.icon = icon
        self.points = 0
        self.plrID = plrID

    def addPoints(points):
        if self.points == 0:
            self.points = points
        else:
            self.points += points

class Weight:

    def __init__(self, weight, location, ownerID):
        self.weight = weight
        self.location = location ## [x,y], x=scale, y=spot on scale
        self.ownerID = ownerID

    def changeOwner(self, newownerID):
        if self.ownerID != newownerID:
            self.ownerID = newownerID

class Scale:

    def __init__(self, length, scaleID, location=0):
        self.length = length
        self.scaleID = scaleID
        self.location = location
        self.weights = []
        self.scales = []
        self.mass = 0
        self.balance = 0

    def addWeights(self, weight):
        self.weights.append(weight)
        self.mass += weight.weight
        self.balance += int(weight.location[1])
