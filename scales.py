from classes import Player, Weight, Scale
from random import randint
from string import ascii_uppercase
from draw import *
import pygame
from pygame.locals import *
import re



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


def placeScale(scales, spotsTaken, scaleIDs):
    scaleLength = 2 * (randint(1, 5))
    baseScale = scales[randint(0, len(scales) - 1)] ##scale where new scale is placed
    locIndex = randint(0, baseScale.length - 1)  ##location of new scale on base scale
    locOnScale = locIndex - (baseScale.length / 2)
    scaleLoc = [baseScale.scaleID, locOnScale]
    while locOnScale == 0 or scaleLoc in spotsTaken:
        locIndex = randint(0, baseScale.length - 1)
        locOnScale = locIndex - (baseScale.length / 2)
        scaleLoc = [baseScale.scaleID, locOnScale]
    scaleID = ascii_uppercase[len(scales)] ##letter ID for scale
    newScale = Scale(scaleLength, scaleID, scaleLoc, baseScale)
    print(newScale.scaleID)
    scales.append(newScale)
    scaleIDs.append(newScale.scaleID)
    baseScale.scales.append(newScale)
    spotsTaken.append(newScale.location)
    drawScale(newScale, baseScale)
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

def isBalanced(scales, scale, weight, basescale):
    totalMass = 0
    for entry in scales:
        if entry.scaleID == scale.scaleID and entry.scaleID == basescale.scaleID:
            if (entry.balance + int(weight)) <= (entry.length / 2):
                return True
            else:
                return False
        if len(entry.scales) != 0:
            totalMass = isBalanced(entry.scales, scale, weight, basescale)
        totalMass += (entry.mass * abs(entry.location[1]))
        if entry.scaleID == scale.scaleID:
            if (entry.balance + int(weight)) <= (entry.length / 2):
                totalMass += abs(int(weight))
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
    menurects = []
    plrrects = []
    players = []
    plrIDs = []
    scales = []
    spotsTaken = []
    gameStarted = False
    drawBoard(menurects, plrrects)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if menurects[0].collidepoint(mousepos): ##menurect = [newgame, startgame]
                    menurects = []
                    plrrects = []
                    players = []
                    plrIDs = []
                    scales = []
                    spotsTaken = []
                    gameStarted = False
                    drawBoard(menurects, plrrects)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if plrrects[0].collidepoint(mousepos) and 0 not in plrIDs:
                    plr1 = Player("Player 1", (0,255,0), 0)
                    enablePlayers(plr1)
                    players.append(plr1)
                    plrIDs.append(0)
                elif plrrects[0].collidepoint(mousepos) and 0 in plrIDs:
                    disablePlayers(plr1)
                    players.remove(plr1)
                    plrIDs.remove(0)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if plrrects[1].collidepoint(mousepos) and 1 not in plrIDs:
                    plr2 = Player("Player 2", (255,0,0), 1)
                    enablePlayers(plr2)
                    players.append(plr2)
                    plrIDs.append(1)
                elif plrrects[1].collidepoint(mousepos) and 1 in plrIDs:
                    disablePlayers(plr2)
                    players.remove(plr2)
                    plrIDs.remove(1)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if plrrects[2].collidepoint(mousepos) and 2 not in plrIDs:
                    plr3 = Player("Player 3", (0,0,255), 2)
                    enablePlayers(plr3)
                    players.append(plr3)
                    plrIDs.append(2)
                elif plrrects[2].collidepoint(mousepos) and 2 in plrIDs:
                    disablePlayers(plr3)
                    players.remove(plr3)
                    plrIDs.remove(2)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if plrrects[3].collidepoint(mousepos) and 3 not in plrIDs:
                    plr4 = Player("Player 4", (255,255,0), 3)
                    enablePlayers(plr4)
                    players.append(plr4)
                    plrIDs.append(3)
                elif plrrects[3].collidepoint(mousepos) and 3 in plrIDs:
                    disablePlayers(plr4)
                    players.remove(plr4)
                    plrIDs.remove(3)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if menurects[1].collidepoint(mousepos): ##menurect = [newgame, startgame]
                    gameStarted = True

        pygame.display.update()


def maind():

    WEIGHTSLEFT = 30

    while True:
        try:
            playerno = int(input("Give number of players\n"))
            players = []
            scales = []
            spotsTaken = []
            for i in range(playerno):
                players.append(createPlayer(i))

            basescale = Scale(2 * randint(1,5), 'A')
            scaleIDs = ['A']
            print("Length of scale A: ", basescale.length)
            scales.append(basescale)
            drawScale(basescale)

            weightsToBePlaced = WEIGHTSLEFT
            weightsLeft = weightsToBePlaced
            turnsDone = 0
            newScaleChance = 0
            while turnsDone < weightsToBePlaced:
                if newScaleChance == 1:
                    newScale = placeScale(scales, spotsTaken, scaleIDs)
                    pygame.display.update()
                    print("New scale placed on scale ", newScale.location[0], " at ", newScale.location[1])
                    print("Scale length of scale ", newScale.scaleID, " is ", newScale.length)
                for plr in players:
                    print(plr.name, ", your turn.")
                    print("There are ", weightsLeft, " weights left.")
                    placeWeight(plr, scales, scaleIDs, basescale, spotsTaken)
                    pygame.display.update()
                    turnsDone += 1
                    weightsLeft -= 1
                newScaleChance = randint(1, 1)
            for playr in players:
                scoreCount(basescale, playr)
        except ValueError:
            print("Input an integer value")

main()
