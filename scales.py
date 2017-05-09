from classes import Player, Weight, Scale
from random import randint
from string import ascii_uppercase
from drawings import *
from calculate import *
from place import *
import pygame
from pygame.locals import *
import re


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
                if menurects[1].collidepoint(mousepos) and gameStarted == False and len(players) != 0:
                    gameStarted = True
                    changeInfo(gameStarted)
                    basescale = Scale(2 * randint(5,10), 'A')
                    scaleIDs = ['A']
                    scales.append(basescale)
                    drawScale(basescale)
                    WEIGHTSLEFT = 5 * len(players)
                    GAMEEND = WEIGHTSLEFT
                    TURNSDONE = 0
                    NEWSCALECHANCE = 1
                    PLRTURN = players[0]
                    playerTurnInfo(PLRTURN)
                    weightsLeftCount(WEIGHTSLEFT)
                    winner = []
            if event.type == MOUSEBUTTONDOWN and event.button == 1: ##Place weight
                mousepos = pygame.mouse.get_pos()
                for scale1 in scales:
                    for spot1 in scale1.spots:
                        if spot1.collidepoint(mousepos) and gameStarted == True and WEIGHTSLEFT > 0:
                            placed = drawWeight(spot1, scale1, spotsTaken, PLRTURN) #return true if weight successfully placed or placing would've caused the scales to fall, false if spot taken by scale
                            if placed:
                                if PLRTURN == players[-1]:
                                    PLRTURN = players[0]
                                else:
                                    PLRTURN = players[PLRTURN.plrID+1]
                                playerTurnInfo(PLRTURN)
                                WEIGHTSLEFT -= 1
                                TURNSDONE += 1
                                weightsLeftCount(WEIGHTSLEFT)
                                if PLRTURN.plrID == 0 and NEWSCALECHANCE == randint(0,2):
                                    placeScale(scales, spotsTaken, scaleIDs)
                                if TURNSDONE == GAMEEND:
                                    for pl in players:
                                        scoreCount(basescale, pl.points, pl)
                                    players = sorted(players, key=lambda player: player.points, reverse=True)
                                    winner.append(players[0])
                                    scoreInfo(players, winner)

        pygame.display.update()


main()
