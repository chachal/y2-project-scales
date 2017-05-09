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
        self.scales = []
        self.mass = 0
        self.balance = 0
        self.centerCoordinates = 0
        self.spots = []

    def addWeights(self, weight):
        self.contains.append(weight)
        if self.location == [0, 0]:
            self.mass += weight.mass
        else:
            self.mass += weight.mass * abs(self.location[1])
        self.balance += int(weight.location[1])
