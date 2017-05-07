from classes import Player, Weight, Scale
from random import randint
from string import ascii_uppercase
import pygame
from pygame.locals import *
import re

pygame.init()
x = 1280
y = 960
DISPLAYWIN = pygame.display.set_mode((x, y))
DISPLAYWIN.fill([100,100,100])
pygame.display.set_caption("Scales")
pygame.font.init()
font = pygame.font.SysFont("",25)
pygame.draw.rect(DISPLAYWIN, (0,0,0), (1, 1, x - 2, (y*0.1) + 6))
players = pygame.draw.rect(DISPLAYWIN, (150,150,150), (5, 5, x - 10, y*0.1))
pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.75) + 8, (y*0.1) + 8, (x*0.25) - 9, (y*0.1) + 4))
turn = pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.75) + 10, (y*0.1) + 10, (x*0.25) - 15, y*0.1))
pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.75) + 8, (y*0.2) + 13, (x*0.25) - 9, (y*0.8) - 14))
high = pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.75) + 10, (y*0.2) + 15, (x*0.25) - 15, (y*0.8) - 20))
pygame.draw.rect(DISPLAYWIN, (0,0,0), (1, (y*0.1) + 8, (x*0.75) + 6, (y*0.75) + 4))
game = pygame.draw.rect(DISPLAYWIN, (150,150,150), (5, (y*0.1) + 10, (x*0.75), y*0.75))
pygame.draw.rect(DISPLAYWIN, (0,0,0), (1, (y*0.85) + 13, (x*0.25) + 1, (y*0.15) - 14))
weights = pygame.draw.rect(DISPLAYWIN, (150,150,150), (5, (y*0.85) + 15, (x*0.25) - 5, (y*0.15) - 20))
pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.25) + 3, (y*0.85) + 13, (x*0.5) + 4, (y*0.15) - 14))
scales = pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.25) + 5, (y*0.85) + 15, (x*0.5), (y*0.15) - 20))
text = font.render("Players:",True,(0,0,0))
DISPLAYWIN.blit(text,(10,y*0.04))
text = font.render("High Scores:",True,(0,0,0))
DISPLAYWIN.blit(text,(x*0.77,y*0.25))
text = font.render("Now playing:",True,(0,0,0))
DISPLAYWIN.blit(text,(x*0.77,y*0.15))
text = font.render("Weights left:",True,(0,0,0))
DISPLAYWIN.blit(text,(10,y*0.92))
text = font.render("Scales placed:",True,(0,0,0))
DISPLAYWIN.blit(text,((x*0.27),y*0.92))
pygame.display.update()


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
            if (entry.balance + weight) <= (entry.length / 2):
                return True
            else:
                return False
        if len(entry.scales) != 0:
            totalMass = isBalanced(entry.scales, scale, weight, bscale)
        totalMass += (entry.mass * abs(entry.location[1]))
        if entry.scaleID == scale.scaleID:
            if (entry.balance + weight) <= (entry.length / 2):
                totalMass += abs(weight)
                return totalMass
            else:
                return False
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

    SCALESLEFT = 30

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
            weightsToBePlaced = SCALESLEFT
            weightsLeft = weightsToBePlaced + 1
            turnsDone = 0
            newScaleChance = 0
            while turnsDone < weightsToBePlaced:
                if newScaleChance == 1:
                    newScale = placeScale(scales, scaleIDs)
                    pygame.display.update()
                    print("New scale placed on scale ", newScale.location[0], " at ", newScale.location[1])
                    print("Scale length of scale ", newScale.scaleID, " is ", newScale.length)
                for plr in players:
                    print(plr.name, ", your turn.")
                    print("There are ", weightsLeft, " weights left.")
                    placeWeight(plr, scales, scaleIDs, bscale, spotsTaken)
                    pygame.display.update()
                    turnsDone += 1
                    weightsLeft -= 1
                newScaleChance = randint(0, 1)
            for playr in players:
                scoreCount(bscale, playr)
        except ValueError:
            print("Input an integer value")

main()
