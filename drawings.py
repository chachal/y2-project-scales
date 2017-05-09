import pygame
from pygame.locals import *
from place import *

pygame.init()
x = 1280
y = 960
GRIDDIM = 30
GAMEWINX = int(x * 0.75)
GAMEWINY = int(y * 0.75)
ORIGINX = 5 + (GAMEWINX / 2)
ORIGINY = y*0.1 + GAMEWINY
XGRIDS = int((x*0.75)/GRIDDIM)
YGRIDS = int((y*0.75)/GRIDDIM)
DISPLAYWIN = pygame.display.set_mode((x, y))
pygame.display.set_caption("Scales")
pygame.font.init()
font = pygame.font.SysFont("",25)

def drawBoard(menurects, plrrects):

    DISPLAYWIN.fill([100,100,100])
    pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.75) + 8, (y*0.1) + 8, (x*0.25) - 9, (y*0.1) + 4))
    turn = pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.75) + 10, (y*0.1) + 10, (x*0.25) - 15, y*0.1))
    pygame.draw.rect(DISPLAYWIN, (0,0,0), (1, (y*0.1) + 8, (x*0.75) + 6, (y*0.75) + 4))
    game = pygame.draw.rect(DISPLAYWIN, (150,150,150), (5, (y*0.1) + 10, (x*0.75), y*0.75))
    pygame.draw.rect(DISPLAYWIN, (0,0,0), (1, (y*0.85) + 13, (x*0.25) + 1, (y*0.15) - 14))
    weights = pygame.draw.rect(DISPLAYWIN, (150,150,150), (5, (y*0.85) + 15, (x*0.25) - 5, (y*0.15) - 20))
    pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.25) + 3, (y*0.85) + 13, (x*0.5) + 4, (y*0.15) - 14))
    info = pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.25) + 5, (y*0.85) + 15, (x*0.5), (y*0.15) - 20))

    pygame.draw.rect(DISPLAYWIN, (0,0,0), (1, 1, x - 2, (y*0.1) + 6))
    players = pygame.draw.rect(DISPLAYWIN, (150,150,150), (5, 5, x - 10, y*0.1))
    player1 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.24, 0.1*y/4, x*0.12 - 10, y*0.05))
    player2 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.44, 0.1*y/4, x*0.12 - 10, y*0.05))
    player3 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.64, 0.1*y/4, x*0.12 - 10, y*0.05))
    player4 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.84, 0.1*y/4, x*0.12 - 10, y*0.05))

    text = font.render("Click to enable players",True,(0,0,0))
    DISPLAYWIN.blit(text,(20,y*0.04))
    text = font.render("Player 1",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.27,y*0.04))
    text = font.render("Player 2",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.47,y*0.04))
    text = font.render("Player 3",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.67,y*0.04))
    text = font.render("Player 4",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.87,y*0.04))

    plrrects.append(player1)
    plrrects.append(player2)
    plrrects.append(player3)
    plrrects.append(player4)

    pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.75) + 8, (y*0.2) + 13, (x*0.25) - 9, (y*0.8) - 14))
    menu = pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.75) + 10, (y*0.2) + 15, (x*0.25) - 15, (y*0.8) - 20))
    pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.75) + 30, (y*0.3) + 15, (x*0.25) - 55, (y*0.1) - 20))
    newgame = pygame.draw.rect(DISPLAYWIN, (100,100,100), ((x*0.75) + 32, (y*0.3) + 17, (x*0.25) - 59, (y*0.1) - 24))
    pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.75) + 30, (y*0.4) + 15, (x*0.25) - 55, (y*0.1) - 20))
    startgame = pygame.draw.rect(DISPLAYWIN, (100,100,100), ((x*0.75) + 32, (y*0.4) + 17, (x*0.25) - 59, (y*0.1) - 24))

    text = font.render("MENU",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.85,y*0.25))
    text = font.render("New game",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.84,y*0.35 - 5))
    text = font.render("Start game",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.84,y*0.45 - 5))

    menurects.append(newgame)
    menurects.append(startgame)

    text = font.render("Now playing:",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.77,y*0.15))
    text = font.render("Weights left:",True,(0,0,0))
    DISPLAYWIN.blit(text,(20,y*0.92))
    text = font.render("When players have been selected, click [Start game] to play",True,(0,0,0))
    DISPLAYWIN.blit(text,((x*0.27),y*0.92))
    pygame.display.update()

    for i in range(0, YGRIDS):
        for j in range(0, XGRIDS):
            pygame.draw.rect(DISPLAYWIN, (200,200,200), (6+(j*GRIDDIM), ((y*0.1 + 11)+(i*GRIDDIM)), GRIDDIM-2, GRIDDIM-2))
            if i == YGRIDS - 1:
                num = j-int(XGRIDS/2)
                if num < 0:
                    if num == -1:
                        pass
                    else:
                        text = font.render(str(num),True,(0,0,0))
                        if num > -10:
                            DISPLAYWIN.blit(text,(12+(j*GRIDDIM),((y*0.1 + 17)+(i*GRIDDIM))))
                        else:
                            DISPLAYWIN.blit(text,(9+(j*GRIDDIM),((y*0.1 + 17)+(i*GRIDDIM))))
                else:
                    if num+1 == 1:
                        pass
                    else:
                        text = font.render(str(num+1),True,(0,0,0))
                        if num < 10:
                            DISPLAYWIN.blit(text,(14+(j*GRIDDIM),((y*0.1 + 17)+(i*GRIDDIM))))
                        else:
                            DISPLAYWIN.blit(text,(11+(j*GRIDDIM),((y*0.1 + 17)+(i*GRIDDIM))))
    pygame.display.update()

def changeInfo(gameStarted):
    if gameStarted == True:
        pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.25) + 5, (y*0.85) + 15, (x*0.5), (y*0.15) - 20))
        text = font.render("Click desired location to place weight. If the spot already ",True,(0,0,0))
        DISPLAYWIN.blit(text,((x*0.27),y*0.91))
        text = font.render("contains a weight, click on the existing weight to place weight.",True,(0,0,0))
        DISPLAYWIN.blit(text,((x*0.27),y*0.93))
    pygame.display.update()

def scoreInfo(players, winner):
    if len(winner) == 1:
        pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.25) + 5, (y*0.85) + 15, (x*0.5), (y*0.15) - 20))
        text = font.render("The winner is: Player " + str(winner[0].plrID + 1) + "! Scores:",True,(0,0,0))
        DISPLAYWIN.blit(text,((x*0.27),y*0.87+5))
    else:
        pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.25) + 5, (y*0.85) + 15, (x*0.5), (y*0.15) - 20))
        text = font.render("It's a draw! Scores:",True,(0,0,0))
        DISPLAYWIN.blit(text,((x*0.27),y*0.87+5))
    j = 0
    for i in players:
        text = font.render("Player " + str(i.plrID + 1) + ": " + str(i.points),True,(0,0,0))
        DISPLAYWIN.blit(text,((x*0.27),y*0.90+j))
        j += 20
    pygame.display.update()

def enablePlayers(plr):

    if plr.plrID == 0:
        player1 = pygame.draw.rect(DISPLAYWIN, plr.color, (x*0.24, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 1",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.27,y*0.04))
    elif plr.plrID == 1:
        player2 = pygame.draw.rect(DISPLAYWIN, plr.color, (x*0.44, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 2",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.47,y*0.04))
    elif plr.plrID == 2:
        player3 = pygame.draw.rect(DISPLAYWIN, plr.color, (x*0.64, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 3",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.67,y*0.04))
    elif plr.plrID == 3:
        player4 = pygame.draw.rect(DISPLAYWIN, plr.color, (x*0.84, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 4",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.87,y*0.04))
    pygame.display.update()

def disablePlayers(plr):
    if plr.plrID == 0:
        player1 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.24, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 1",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.27,y*0.04))
    elif plr.plrID == 1:
        player2 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.44, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 2",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.47,y*0.04))
    elif plr.plrID == 2:
        player3 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.64, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 3",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.67,y*0.04))
    elif plr.plrID == 3:
        player4 = pygame.draw.rect(DISPLAYWIN, (125,125,125), (x*0.84, 0.1*y/4, x*0.12 - 10, y*0.05))
        text = font.render("Player 4",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.87,y*0.04))
    pygame.display.update()

def playerTurnInfo(PLRTURN):
    if PLRTURN.plrID == 0:
        pygame.draw.rect(DISPLAYWIN, (PLRTURN.color), ((x*0.87) + 10, (y*0.125) + 10, (x*0.11) - 15, y*0.05))
        text = font.render("Player 1",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.9,y*0.15))
    elif PLRTURN.plrID == 1:
        pygame.draw.rect(DISPLAYWIN, (PLRTURN.color), ((x*0.87) + 10, (y*0.125) + 10, (x*0.11) - 15, y*0.05))
        text = font.render("Player 2",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.9,y*0.15))
    elif PLRTURN.plrID == 2:
        pygame.draw.rect(DISPLAYWIN, (PLRTURN.color), ((x*0.87) + 10, (y*0.125) + 10, (x*0.11) - 15, y*0.05))
        text = font.render("Player 3",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.9,y*0.15))
    elif PLRTURN.plrID == 3:
        pygame.draw.rect(DISPLAYWIN, (PLRTURN.color), ((x*0.87) + 10, (y*0.125) + 10, (x*0.11) - 15, y*0.05))
        text = font.render("Player 4",True,(0,0,0))
        DISPLAYWIN.blit(text,(x*0.9,y*0.15))
    pygame.display.update()

def weightsLeftCount(WEIGHTSLEFT):
    pygame.draw.rect(DISPLAYWIN, (150,150,150), (x*0.125, (y*0.87) + 15, (x*0.1), (y*0.1)))
    text = font.render(str(WEIGHTSLEFT),True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.15,y*0.92))
    pygame.display.update()

def drawScale(newScale, baseScale=0):
    length = (newScale.length) * GRIDDIM
    if newScale.location == [0, 0]:
        newScale.centerCoordinates = [int(ORIGINX), int(ORIGINY - 2*GRIDDIM + 10)]
        scaleSpots(newScale)
        scale = pygame.draw.rect(DISPLAYWIN, (0,0,0), (ORIGINX - length/2, ORIGINY - 2*GRIDDIM + 7, length, 4))
        scaleleg = pygame.draw.rect(DISPLAYWIN, (0,0,0), (ORIGINX - 2, ORIGINY - 2*GRIDDIM + 10, 4, 2*GRIDDIM))
        for i in range(0, GRIDDIM):
            pygame.draw.rect(DISPLAYWIN, (0,0,0), (ORIGINX - GRIDDIM + i, ORIGINY-i+10, 2*GRIDDIM-2*i, 1))
    else:
        height = len(baseScale.scales)*2
        basex = baseScale.centerCoordinates[0]
        basey = baseScale.centerCoordinates[1]
        newx = basex + (newScale.location[1] * GRIDDIM)
        newy = basey - (1+height)*GRIDDIM
        scale = pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx - length/2, newy - 3, length, 4))
        scaleleg = pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx - 2, newy, 4, (1 + height)*GRIDDIM))
        newScale.centerCoordinates = [int(newx), int(newy)]
        if newScale.location[1] < 0:
            for i in range(GRIDDIM, 0, -1):
                pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx, newy+(1 + height)*GRIDDIM-i-3, GRIDDIM-i, 1))
        elif newScale.location[1] > 0:
            for i in range(GRIDDIM, 0, -1):
                pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx - GRIDDIM + i, newy+(1 + height)*GRIDDIM-i-3, GRIDDIM-i, 1))
    pygame.display.update()

def scaleSpots(selScale):
    length = (selScale.length) * GRIDDIM
    centerX = selScale.centerCoordinates[0]
    centerY = selScale.centerCoordinates[1]
    for i in range(0, selScale.length):
        grid = pygame.draw.rect(DISPLAYWIN, (175,175,175), ((i*GRIDDIM) + centerX - length/2 + 1, centerY - GRIDDIM + 1, GRIDDIM - 2, GRIDDIM - 4))
        selScale.spots.append(grid)
    pygame.display.update()

def drawWeight(spot, selScale, spotsTaken, player, basescale, scales):
    inSpot = 0
    scaleLen = selScale.length
    i = selScale.spots.index(spot)
    length = (selScale.length) * GRIDDIM
    actLoca = []
    centerX = selScale.centerCoordinates[0]
    centerY = selScale.centerCoordinates[1]
    if i >= (scaleLen / 2):
        actLoca = [selScale.scaleID, int(i - (scaleLen / 2) + 1)]
    else:
        actLoca = [selScale.scaleID, int(i - (scaleLen / 2))]
    inSpot = placeWeight(actLoca, selScale, spotsTaken, player, basescale, scales) #returns number of lumps in spot, after placement of new lump
    if inSpot == "SCALE":
        return False
    elif inSpot == "IMBALANCE":
        pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.25) + 5, (y*0.85) + 15, (x*0.5), (y*0.15) - 20))
        text = font.render("Weight not added, resulting imbalance would've been too large",True,(0,0,0))
        DISPLAYWIN.blit(text,((x*0.27),y*0.92))
        pygame.display.update()
        return True
    else:
        grid = pygame.draw.rect(DISPLAYWIN, (175,175,175), ((i*GRIDDIM) + centerX - length/2 + 3, centerY - GRIDDIM + 1, GRIDDIM - 8, GRIDDIM - 5))
        frame = pygame.draw.rect(DISPLAYWIN, (0,0,0), ((i*GRIDDIM) + centerX - length/2 + 10, centerY - GRIDDIM + 17, GRIDDIM - 20, GRIDDIM - 20))
        lump = pygame.draw.rect(DISPLAYWIN, (player.color), ((i*GRIDDIM) + centerX - length/2 + 12, centerY - GRIDDIM + 19, GRIDDIM - 24, GRIDDIM - 24))
        if inSpot < 9:
            text = font.render(str(inSpot + 1),True,(0,0,0))
            DISPLAYWIN.blit(text,((i*GRIDDIM) + centerX - length/2 + 10, centerY - GRIDDIM + 1))
        else:
            text = font.render(str(inSpot + 1),True,(0,0,0))
            DISPLAYWIN.blit(text,((i*GRIDDIM) + centerX - length/2 + 6, centerY - GRIDDIM + 1))
    changeInfo(True)
    pygame.display.update()
    return True
