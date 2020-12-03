import pygame
import time

pygame.init()
DISPLAY_SIZE = 600
screen = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
screen.fill((255, 255, 255))
pygame.display.set_caption('hide & seek')

HIDER = pygame.image.load('virus.png').convert()
pygame.display.set_icon(HIDER)
SEEKER = pygame.image.load('mask.png').convert()
""""
#init positions of SEEKER and HIDER
SEEKER_INIT = (2,2)     #human
HIDER_INIT = (23,23)    #virus
"""
GREY = pygame.Color(158,158,158)
YELLOW = pygame.Color(255, 193, 7)
BLACK = pygame.Color(0, 0, 0)
COLORS = {
  '0': BLACK,
  '1': GREY,
  '2': HIDER,
  '3': SEEKER,
  '4': YELLOW,
}

map = []

def loadMapToArr(path):
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  row = []
  for number in mapString:
    if number != '\n':
      row.append(int(number))
    else:
      map.append(row)
      row = []

def setupGame(path):
  drawMap(path)
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  squareSize = int(DISPLAY_SIZE / mapSize)
  loadMapToArr(path)
  print(map)
  #Posion Seeker:
  #Seek_xCoor = 1*squareSize #SEEKER_INIT[0]
  #Seek_yCoor = 1*squareSize #SEEKER_INIT[1]
  #Position Hider:
  #Hide_xCoor = 23*squareSize #HIDER_INIT[0]
  #Hide_yCoor = 23*squareSize #HIDER_INIT[1]
  Seek_xCoor = 1
  Seek_yCoor = 1
  Hider_xCoor = 23
  Hider_yCoor = 23
  RUNNING = True
  while RUNNING:

    #Draw Seeker:
    COLORS['3'].set_colorkey
    screen.blit(COLORS['3'], (Seek_xCoor*24, Seek_yCoor*24))
    #Draw Hider:
    COLORS['2'].set_colorkey
    screen.blit(COLORS['2'], (Hider_xCoor*24, Hider_yCoor*24))


    #Seek run to...: Algorithm here....
    time.sleep(0.3)
    if(ableToMoveRight(Seek_xCoor, Seek_yCoor)==True):
      Seek_xCoor +=1
    elif(ableToMoveDown(Seek_xCoor, Seek_yCoor)==True):
      Seek_yCoor +=1


    ##Hide_xCoor +=squareSize

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        RUNNING = False
    pygame.display.update()


def getMapString(path):
  f = open(path, 'r')
  next(f)       ##bo dong dau tien
  mapString = f.read()
  f.close()
  return mapString

def getMapSize(path):
  f = open(path, 'r')
  firstLine = f.readline()        
  size = int(firstLine[0] + firstLine[1])
  f.close()
  return size

def drawMap(path):
  global DISPLAY_SIZE
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  squareSize = int(DISPLAY_SIZE / mapSize)
  xCoor = 0
  yCoor = 0
  count = 0
  for number in mapString:
    if (number != '\n' and number != ','):
      pygame.draw.rect(screen, COLORS[number], [xCoor, yCoor, squareSize, squareSize])
      xCoor += squareSize
      count += 1
    if (count == mapSize):
      yCoor += squareSize 
      xCoor = 0
      count = 0


def ableToMoveRight(coorX, coorY):
  if((map[coorX+1][coorY]==1) or (map[coorX+1][coorY]==4)):
    return False
  return True

def ableToMoveLeft(coorX, coorY):
  if((map[coorX-1][coorY]==1) or (map[coorX-1][coorY]==4)):
    return False
  return True

def ableToMoveDown(coorX, coorY):
  if((map[coorX][coorY+1]==1) or (map[coorX][coorY+1]==4)):
    return False
  return True

def ableToMoveUp(coorX, coorY):
  if((map[coorX][coorY-1]==1) or (map[coorX][coorY-1]==4)):
    return False
  return True

def ableToMoveUpRight(coorX, coorY):
  if((map[coorX+1][coorY-1]==1) or (map[coorX+1][coorY-1]==4)):
    return False
  return True
def ableToMoveUpLeft(coorX, coorY):
  if((map[coorX-1][coorY-1]==1) or (map[coorX-1][coorY-1]==4)):
    return False
  return True

def ableToMoveDownLeft(coorX, coorY):
  if((map[coorX-1][coorY+1]==1) or (map[coorX-1][coorY+1]==4)):
    return False
  return True

def ableToMoveDownRight(coorX, coorY):
  if((map[coorX+1][coorY+1]==1) or (map[coorX+1][coorY+1]==4)):
    return False
  return True
setupGame('map11.txt')