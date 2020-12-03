import pygame

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

def setupGame(path):
  drawMap(path)

  RUNNING = True
  while RUNNING:
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
    if (number != '\n'):
      if (number != '2' and number != '3'):
        pygame.draw.rect(screen, COLORS[number], [xCoor, yCoor, squareSize, squareSize])
      else:
        COLORS[number].set_colorkey
        screen.blit(COLORS[number], (xCoor, yCoor))
      xCoor += squareSize
      count += 1
    if (count == mapSize):
      yCoor += squareSize 
      xCoor = 0
      count = 0

setupGame('map42.txt')