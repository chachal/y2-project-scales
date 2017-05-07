from random import randint
from string import ascii_uppercase
import pygame
from pygame.locals import *
import re
"""
pygame.init()
displaywin = pygame.display.set_mode((450, 300))
pygame.display.set_caption("Scales")"""

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


def createPlayer(number):
    plrname = None
    plricon = None
    plrno = str(number + 1)
    while plrname == None:
        plrname = input("Give name of player " + plrno + "\n")
    while plricon == None:
        plricon = input("Give icon for player " + plrno + "\n")
    newPlayer = Player(plrname, plricon, number)
    return newPlayer


def placeScale(scales, scaleIDs, spotsTaken):
    scaleLength = 2 * (randint(1, 5)) + 1
    baseScale = scales[randint(0, len(scales) - 1)] ##scale where new scale is placed
    locIndex = randint(0, baseScale.length - 1)  ##location of new scale on base scale
    locOnScale = locIndex - (baseScale.length / 2)
    scaleLoc = [baseScale.scaleID, locOnScale]
        while locOnScale == 0 or scaleLoc in spotsTaken:
            locIndex = randint(0, baseScale.length - 1)
            locOnScale = locIndex - (baseScale.length / 2)
            scaleLoc = [baseScale.scaleID, locOnScale]
    scaleID = ascii_uppercase[len(scales)] ##letter ID for scale
    newScale = Scale(scaleLength, scaleID, scaleLoc)
    scales.append(newScale)
    baseScale.scales.append(newScale)
    scaleIDs.append(newScale.scaleID)
    spotsTaken.append(newScale.location)
    return newScale


def placeWeight(player, scales, scaleIDs, bscale, spotsTaken):
        scalID = input("Give scale where to place weight\n").upper()
        while not re.match("^[a-zA-Z]*$", scalID) or scalID not in scaleIDs:
            scalID = input("Scale doesn't exist, input another one\n").upper()
        if re.match("^[A-Z]*$", scalID):
            for entry in scales:
                if entry.scaleID == scalID:
                    scalePlace = input("Give position of weight on scale\n")
                    rad = abs(int(scalePlace))
                    maxRad = int(entry.length / 2)
                    while not rad <= maxRad:
                        scalePlace = input("Give value between -"+ str(maxRad) + " and " + str(maxRad) + "\n")
                        rad = abs(int(scalePlace))
                    if isBalanced(scales, entry, scalePlace, bscale):
                        newLoc = [scalID, scalePlace]
                        weightOfWeight = abs(int(scalePlace))
                        wght = Weight(weightOfWeight, newLoc, player.plrID)
                        entry.addWeights(wght)
                        spotsTaken.append(wght.location)
                        for one in entry.weights:
                            if one.location == newLoc:
                                one.changeOwner(player.plrID)
                        return True
                    else:
                        print("Weight not placed, imbalance too large")
                        return True
                else:
                    continue

def isBalanced(scales, scale, weight, bscale):
    totalMass = 0
    for entry in scales:
        if entry.scaleID == scale.scaleID and entry.scaleID == bscale.scaleID:
            if (entry.balance += weight) <= (entry.length / 2):
                return True
            else:
                return False
        if len(entry.scales) != 0:
            totalMass = isBalanced(entry.scales, scale, weight, bscale)
        totalMass += (entry.mass * abs(entry.location[1]))
        if entry.scaleID == scale.scaleID:
            if (entry.balance += weight) <= (entry.length / 2):
                totalMass += abs(weight)
                return totalMass
            else:
                return False
        elif:
            if entry.scaleID == bscale.scaleID:

        else:
            return totalMass




def scoreCount(basescale, player):
    points = 0
    scalespop = list(basescale.scales)
    for entry in scalespop:     ##entry = Scale object in basescale list
        while len(entry.scales) != 0: ##number of scales directly on top of entry-scale
            popped = entry.scales.pop()
            points = scoreCount(popped, player)
        for weight in entry.weights:
            if player.plrID == weight.ownerID:
                points += weight.weight
        if entry.location != 0:
            points *= abs(entry.location[1])
        return points


def main():

    while True:
        try:
            playerno = int(input("Give number of players\n"))
            players = []
            scales = []
            spotsTaken = []
            for i in range(playerno):
                players.append(createPlayer(i))
            bscale = Scale(2 * randint(1,5), 'A')
            scaleIDs = ['A']
            print("Length of scale A: ", bscale.length)
            scales.append(bscale)
            weightsToBePlaced = randint(0, 20)
            weightsLeft = weightsToBePlaced + 1
            turnsDone = 0
            newScaleChance = 0
            while turnsDone < weightsToBePlaced:
                if newScaleChance == 1:
                    newScale = placeScale(scales, scaleIDs)
                    print("New scale placed on scale ", newScale.location[0], " at ", newScale.location[1])
                    print("Scale length of scale ", newScale.scaleID, " is ", newScale.length)
                for plr in players:
                    print(plr.name, ", your turn.")
                    print("There are ", weightsLeft, " weights left.")
                    placeWeight(plr, scales, scaleIDs, spotsTaken)
                    turnsDone += 1
                    weightsLeft -= 1
                newScaleChance = randint(0, 1)
            for playr in players:
                scoreCount(bscale, playr)
        except ValueError:
            print("Input an integer value")

main()
