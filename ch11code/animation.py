import pygame, sys
from pygame.locals import *
import numpy as np
import os

homedir = os.getcwd()+'/NumPy/ch11code/'

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Animating Objects')
img = pygame.image.load(homedir+'head.jpg')

steps = np.linspace(20, 360, 40).astype(int)
right = np.zeros((2, len(steps)))
down = np.zeros((2, len(steps)))
left = np.zeros((2, len(steps)))
up = np.zeros((2, len(steps)))
# print "steps:",steps
# print "right:",right
# print "down:",down
# print "left:",left
# print "up:",up


right[0] = steps
right[1] = 20
# print "right[0]:",right[0]

down[0] = 360
down[1] = steps
# print "down[1]:",down[1]

left[0] = steps[::-1]
left[1] = 360
# print "left[0]:",left[0]

up[0] = 20
up[1] = steps[::-1]
# print "up[1]:",up[1]

pos = np.concatenate((right.T, down.T, left.T, up.T))
# print "pos:",pos
i = 0

while True:
   # Erase screen
   screen.fill((255, 255, 255))

   if i >= len(pos):
      i = 0

   screen.blit(img, pos[i])
   i += 1

   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   pygame.display.update()
   clock.tick(30)
