from classes import Player, Weight, Scale
from random import randint
from string import ascii_uppercase
from draw import *
import pygame
from pygame.locals import *
import re



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
    newScale = Scale(scaleLength, scaleID, scaleLoc)
    print(newScale.scaleID)
    scales.append(newScale)
    scaleIDs.append(newScale.scaleID)
    baseScale.contains.append(newScale)
    spotsTaken.append(newScale.location)
    drawScale(newScale, baseScale)
    return newScale


def scoreCount(scaleA, points, player, level=0):
    apoints = 0
    contained = list(scaleA.contains)
    for entry in contained:
        if entry.objectID == 0:
            if entry.location[0] != "A":
                level += 1
                points = scoreCount(entry, points, player, level) * abs(entry.location[1])
                level -= 1
            else:
                level += 1
                points += scoreCount(entry, points, player, level) * abs(entry.location[1])
                level -= 1
                apoints += points
                points = 0
        else:
            if scaleA.scaleID == "A" and entry.owner == player.pID:
                apoints += entry.weight
                points = apoints
            elif scaleA.scaleID != "A" and entry.owner == player.pID:
                points += entry.weight
    if level == 0:
        points = apoints
    return points

def isBalanced(scaleA, weight):
    apoints = 0
    contained = list(scaleA.contains)
    for entry in contained:
        if entry.objectID == 0:
            if entry.location[0] != "A":
                points = isBalanced(entry, points) * abs(entry.location[1])
            else:
                points += isBalanced(entry, points) * abs(entry.location[1])
                apoints += points
                points = 0
        else:
            if scaleA.scaleID == "A":
                apoints += entry.weight
                points = apoints
            else:
                points += entry.weight
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
            if event.type == MOUSEBUTTONDOWN and event.button == 1: ##New game
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
            if event.type == MOUSEBUTTONDOWN and event.button == 1: ##Player 1
                mousepos = pygame.mouse.get_pos()
                if plrrects[0].collidepoint(mousepos) and 0 not in plrIDs and gameStarted == False:
                    plr1 = Player("Player 1", (0,255,0), 0)
                    enablePlayers(plr1)
                    players.append(plr1)
                    plrIDs.append(0)
                elif plrrects[0].collidepoint(mousepos) and 0 in plrIDs and 1 not in plrIDs and gameStarted == False: #players selected/deselected in numerical order
                    disablePlayers(plr1)
                    players.remove(plr1)
                    plrIDs.remove(0)
            if event.type == MOUSEBUTTONDOWN and event.button == 1: ##Player 2
                mousepos = pygame.mouse.get_pos()
                if plrrects[1].collidepoint(mousepos) and 1 not in plrIDs and 0 in plrIDs and gameStarted == False:
                    plr2 = Player("Player 2", (255,0,0), 1)
                    enablePlayers(plr2)
                    players.append(plr2)
                    plrIDs.append(1)
                elif plrrects[1].collidepoint(mousepos) and 1 in plrIDs and 2 not in plrIDs and gameStarted == False:
                    disablePlayers(plr2)
                    players.remove(plr2)
                    plrIDs.remove(1)
            if event.type == MOUSEBUTTONDOWN and event.button == 1: ##Player 3
                mousepos = pygame.mouse.get_pos()
                if plrrects[2].collidepoint(mousepos) and 2 not in plrIDs and 1 in plrIDs and gameStarted == False:
                    plr3 = Player("Player 3", (0,0,255), 2)
                    enablePlayers(plr3)
                    players.append(plr3)
                    plrIDs.append(2)
                elif plrrects[2].collidepoint(mousepos) and 2 in plrIDs and 3 not in plrIDs and gameStarted == False:
                    disablePlayers(plr3)
                    players.remove(plr3)
                    plrIDs.remove(2)
            if event.type == MOUSEBUTTONDOWN and event.button == 1: ##Player 4
                mousepos = pygame.mouse.get_pos()
                if plrrects[3].collidepoint(mousepos) and 3 not in plrIDs and 2 in plrIDs and gameStarted == False:
                    plr4 = Player("Player 4", (255,255,0), 3)
                    enablePlayers(plr4)
                    players.append(plr4)
                    plrIDs.append(3)
                elif plrrects[3].collidepoint(mousepos) and 3 in plrIDs and gameStarted == False:
                    disablePlayers(plr4)
                    players.remove(plr4)
                    plrIDs.remove(3)
            if event.type == MOUSEBUTTONDOWN and event.button == 1: ##Start game
                mousepos = pygame.mouse.get_pos()
                if menurects[1].collidepoint(mousepos) and gameStarted == False:
                    gameStarted = True
                    basescale = Scale(2 * randint(2,5), 'A')
                    scaleIDs = ['A']
                    scales.append(basescale)
                    drawScale(basescale)
                    WEIGHTSLEFT = 10 * len(players)
                    turnsDone = 0
                    newScaleChance = 0
                    PLRTURN = players[0]
                    changeInfo(gameStarted)
                    weightsLeftCount(WEIGHTSLEFT)
                    playerTurnInfo(PLRTURN)
            #if event.type == MOUSEBUTTONDOWN and event.button == 1: ##Place weight
                #mousepos = pygame.mouse.get_pos()
                #if menurects[1].collidepoint(mousepos)

        pygame.display.update()


def maind():

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

main()
