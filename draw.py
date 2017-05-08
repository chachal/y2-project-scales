import pygame
from pygame.locals import *

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
    scales = pygame.draw.rect(DISPLAYWIN, (150,150,150), ((x*0.25) + 5, (y*0.85) + 15, (x*0.5), (y*0.15) - 20))

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
    loadgame = pygame.draw.rect(DISPLAYWIN, (100,100,100), ((x*0.75) + 32, (y*0.4) + 17, (x*0.25) - 59, (y*0.1) - 24))
    pygame.draw.rect(DISPLAYWIN, (0,0,0), ((x*0.75) + 30, (y*0.5) + 15, (x*0.25) - 55, (y*0.1) - 20))
    savegame = pygame.draw.rect(DISPLAYWIN, (100,100,100), ((x*0.75) + 32, (y*0.5) + 17, (x*0.25) - 59, (y*0.1) - 24))

    text = font.render("MENU",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.85,y*0.25))
    text = font.render("New game",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.84,y*0.35 - 5))
    text = font.render("Start game",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.84,y*0.45 - 5))
    text = font.render("Save game",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.84,y*0.55 - 5))

    menurects.append(newgame)
    menurects.append(loadgame)
    menurects.append(savegame)

    text = font.render("Now playing:",True,(0,0,0))
    DISPLAYWIN.blit(text,(x*0.77,y*0.15))
    text = font.render("Weights left:",True,(0,0,0))
    DISPLAYWIN.blit(text,(20,y*0.92))
    text = font.render("Scales placed:",True,(0,0,0))
    DISPLAYWIN.blit(text,((x*0.27),y*0.92))
    pygame.display.update()

    for i in range(0, YGRIDS):
        for j in range(0, XGRIDS):
            pygame.draw.rect(DISPLAYWIN, (200,200,200), (6+(j*GRIDDIM), ((y*0.1 + 11)+(i*GRIDDIM)), GRIDDIM-2, GRIDDIM-2))
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

def drawScale(newScale, baseScale=0):
    length = (newScale.length) * GRIDDIM
    if newScale.location == 0:
        scale = pygame.draw.rect(DISPLAYWIN, (0,0,0), (ORIGINX - length/2 - 3, ORIGINY - 2*GRIDDIM + 10, length + 6, 6))
        scaleleg = pygame.draw.rect(DISPLAYWIN, (0,0,0), (ORIGINX - 3, ORIGINY - 2*GRIDDIM + 10, 6, 2*GRIDDIM))
        scalewallr = pygame.draw.rect(DISPLAYWIN, (0,0,0), (ORIGINX + length/2, ORIGINY - 2*GRIDDIM - 10, 3, GRIDDIM))
        scalewalll = pygame.draw.rect(DISPLAYWIN, (0,0,0), (ORIGINX - length/2 - 3, ORIGINY - 2*GRIDDIM - 10, 3, GRIDDIM))
        newScale.centerCoordinates = [int(ORIGINX), int(ORIGINY - 2*GRIDDIM + 10)]
    else:
        height = len(baseScale.scales)
        basex = baseScale.centerCoordinates[0]
        basey = baseScale.centerCoordinates[1]
        newx = basex + (newScale.location[1] * GRIDDIM)
        newy = basey - (1+height)*GRIDDIM
        scale = pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx - length/2 - 3, newy, length + 6, 6))
        scaleleg = pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx - 3, newy, 6, 2*GRIDDIM))
        scalewallr = pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx + length/2, newy - 20, 3, GRIDDIM))
        scalewalll = pygame.draw.rect(DISPLAYWIN, (0,0,0), (newx - length/2 - 3, newy - 20, 3, GRIDDIM))
        newScale.centerCoordinates = [int(newx), int(newy)]

    text = font.render(newScale.scaleID,True,(0,0,0))
    DISPLAYWIN.blit(text,((x*0.4),y*0.92))
    pygame.display.update()

def drawWeight(weight, baseScale, player):
    pass
