from calculate import *
from classes import *
from drawings import *
from random import randint
from string import ascii_uppercase
import drawings

def placeScale(scales, spotsTaken, scaleIDs):
    scaleLength = 2 * (randint(3, 7))
    baseScale = scales[randint(0, len(scales) - 1)] ##scale where new scale is placed
    locIndex = randint(0, baseScale.length - 1)  ##location of new scale on base scale
    locOnScale = locIndex - (baseScale.length / 2)
    scaleLoc = [baseScale.scaleID, int(locOnScale)]
    for entry in spotsTaken:
        if scaleLoc == entry[0]:
            locOnScale = 0
    while locOnScale == 0:
        locIndex = randint(0, baseScale.length - 1)
        locOnScale = locIndex - (baseScale.length / 2)
        scaleLoc = [baseScale.scaleID, int(locOnScale)]
        for entry in spotsTaken:
            if scaleLoc == entry[0]:
                locOnScale = 0
                break
    scaleID = ascii_uppercase[len(scales)] ##letter ID for scale
    newScale = Scale(scaleLength, scaleID, scaleLoc)
    scales.append(newScale)
    scaleIDs.append(newScale.scaleID)
    baseScale.contains.append(newScale)
    baseScale.scales.append(newScale)
    spotsTaken.append([newScale.location, 0]) # spotsTaken[i][1] == 0 if scale, == if weight
    drawings.drawScale(newScale, baseScale)
    drawings.scaleSpots(newScale)


def placeWeight(wLoc, scale, spotsTaken, player):
    inSpot = 0
    wmass = abs(int(wLoc[1]))
    for entry in scale.contains:
        if entry.location == wLoc and entry.objectID == 1:
            entry.changeOwner(player)
            inSpot += 1
        elif entry.location == wLoc and entry.objectID == 0:
            return "SCALE"
    balanced = isBalanced(scale, wLoc) #return true if scale balance after adding weight
    if balanced:
        newWeight = Weight(wmass, wLoc, player)
        scale.addWeights(newWeight)
        spotsTaken.append([wLoc, 1]) # spotsTaken[i][1] == 0 if scale, == if weight
        return inSpot
    else:
        return "IMBALANCE"
