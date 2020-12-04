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
  #init positions of SEEKER and HIDER
  Seek_xCoor = 10
  Seek_yCoor = 5
  Hider_xCoor = 23
  Hider_yCoor = 23
  drawMap(path)
  mapString = getMapString(path)
  mapSize = getMapSize(path)
  squareSize = int(DISPLAY_SIZE / mapSize)
  loadMapToArr(path)
   #Draw Seeker:
  COLORS['3'].set_colorkey
  screen.blit(COLORS['3'], (Seek_xCoor*24, Seek_yCoor*24))
  #Draw Hider:
  COLORS['2'].set_colorkey
  screen.blit(COLORS['2'], (Hider_xCoor*24, Hider_yCoor*24))
  RUNNING = True
  while RUNNING:
    #Seek run to...: Algorithm here....
    time.sleep(0.3)
 #**********Test some move functions******Chay dung a mn*************   
  #  if(moveDown(Seek_xCoor, Seek_yCoor, 3)):
  #    Seek_yCoor+=1
  #  if(moveUp(Seek_xCoor, Seek_yCoor, 3)):
  #    Seek_yCoor-=1
  #  if(moveDownLeft(Seek_xCoor, Seek_yCoor,3)):
  #    Seek_yCoor+=1
  #    Seek_xCoor-=1
  #  if(moveDownRight(Seek_xCoor, Seek_yCoor, 3)):
  #    Seek_yCoor+=1
  #    Seek_xCoor+=1
  #  if(moveUpLeft(Seek_xCoor, Seek_yCoor, 3)):
  #    Seek_yCoor-=1
  #    Seek_xCoor-=1
  #  if(moveUpRight(Seek_xCoor, Seek_yCoor, 3)):
  #    Seek_yCoor-=1
  #    Seek_xCoor+=1
    if(moveLeft(Seek_xCoor, Seek_yCoor, 3)):
      Seek_xCoor-=1
  #  if(moveRight(Seek_xCoor, Seek_yCoor, 3)):
  #    Seek_xCoor+=1
     

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
def drawObjectAfterMove(curX, curY, nextX, nextY, typeOfAgent):
  if(typeOfAgent == 3):
    COLORS['3'].set_colorkey
    screen.blit(COLORS['3'], (nextX*24, nextY*24))
  if(typeOfAgent == 2):
    COLORS['2'].set_colorkey
    screen.blit(COLORS['2'], (nextX*24, nextY*24))
  pygame.draw.rect(screen, COLORS['0'], [curX*24, curY*24, 24, 24]) #squareSize=24
  
#*******************check able to move ******************************#
def ableToMoveRight(coorX, coorY):
  if((map[coorY][coorX+1]!=0)):
    return False
  return True
def ableToMoveLeft(coorX, coorY):
  if((map[coorY][coorX-1]!=0)):
    return False
  return True
def ableToMoveDown(coorX, coorY):
  if((map[coorY+1][coorX]!=0)):
    return False
  return True
def ableToMoveUp(coorX, coorY):
  if((map[coorY-1][coorX]!=0)):
    return False
  return True
def ableToMoveUpRight(coorX, coorY):
  if((map[coorY-1][coorX+1]!=0)):
    return False
  return True
def ableToMoveUpLeft(coorX, coorY):
  if((map[coorY-1][coorX-1]!=0)):
    return False
  return True
def ableToMoveDownLeft(coorX, coorY):
  if((map[coorY+1][coorX-1]!=0)):
    return False
  return True
def ableToMoveDownRight(coorX, coorY):
  if(map[coorY+1][coorX+1]!=0):
    return False
  return True

#***************************move**************************#
def moveRight(coorX, coorY, typeOfAgent):
  if(ableToMoveRight(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY][coorX+1]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX+1,coorY,typeOfAgent)
      return True
  return False
def moveLeft(coorX, coorY, typeOfAgent):
  if(ableToMoveLeft(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY][coorX-1]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX-1,coorY,typeOfAgent)
      return True
  return False
def moveUp(coorX, coorY, typeOfAgent):
  if(ableToMoveUp(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY-1][coorX]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX,coorY-1,typeOfAgent)
      return True
  return False
def moveDown(coorX, coorY, typeOfAgent):
  if(ableToMoveDown(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY+1][coorX]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX,coorY+1,typeOfAgent)
      return True
  return False
def moveDownLeft(coorX, coorY, typeOfAgent):
  if(ableToMoveDownLeft(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY+1][coorX-1]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX-1,coorY+1,typeOfAgent)
      return True
  return False
def moveDownRight(coorX, coorY, typeOfAgent):
  if(ableToMoveDownRight(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY+1][coorX+1]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX+1,coorY+1,typeOfAgent)
      return True
  return False
def moveUpRight(coorX, coorY, typeOfAgent):
  if(ableToMoveUpRight(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY-1][coorX+1]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX+1,coorY-1,typeOfAgent)
      return True
  return False
def moveUpLeft(coorX, coorY, typeOfAgent):
  if(ableToMoveUpLeft(coorX, coorY)==True):
      map[coorY][coorX]=0
      map[coorY-1][coorX-1]=typeOfAgent
      drawObjectAfterMove(coorX, coorY, coorX-1,coorY-1,typeOfAgent)
      return True
  return False

setupGame('map14.txt')