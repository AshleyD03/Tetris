from grid import Grid 
from piece import Piece
from copy import deepcopy
import os 

class Game:

  def __init__ (self):
    self._alive = True 
    self._score = 0 
    self._grid = Grid()
    self._curP = Piece()
    self._nextP = Piece()
    self._storeP = Piece()
    self._swapped = False
    self._isRunning = True


  def moveLeft (self):
    copy = deepcopy(self._curP)
    copy.moveLeft()
    if (self._grid.isPiecePlacable(copy)):
      self._curP.moveLeft()


  def moveRight (self):
    copy = deepcopy(self._curP)
    copy.moveRight()
    if (self._grid.isPiecePlacable(copy)):
      self._curP.moveRight()


  def moveDown (self):
    copy = deepcopy(self._curP)
    copy.moveDown()
    if (self._grid.isPiecePlacable(copy)):
      self._curP.moveDown()
    else: 
      self._grid.placePiece(self._curP)
      self.nextPiece()
      fullRows = self._grid.anyRowsFull()
      self._score += self._grid.clearRows(fullRows)
      self._swapped = False 
      

  def rotateRight (self):
    copy = deepcopy(self._curP)
    copy.rotateRight()
    if (self._grid.isPiecePlacable(copy)):
      self._curP.rotateRight()


  def swapPieces (self):
    if (self._swapped):
      return 
    
    swap = deepcopy(self._curP)
    self._curP = self._storeP
    self._curP.setChanged(True)
    self._storeP = swap
    self._storeP.setChanged(True)
    self._storeP.resetPos()
    self._swapped = True 


  def nextPiece (self):
    self._curP = deepcopy(self._nextP)
    self._nextP = Piece()


  def addScore (self, a):
    self._score += a 


  def printScreen (self):
    # Check if there is any new changes to need to print 
    if (not self._curP.getChanged() and not self._grid.getChanged()):
      return 
    
    self._curP.setChanged(False)
    self._grid.setChanged(False)

    # Overlay current piece on grid 
    grid = deepcopy(self._grid)
    grid.placePiece(self._curP) 
    rows = grid.getRows()

    # Build printable
    screen = [] 
    bar = '##' + '='*21 + '##'
    screen.append(bar)
    screen.append(bar)
    for y in range(20, len(rows)):
      screen.append('|| ' + ' '.join(rows[y]) + ' ||')
    screen.append(bar)
    screen.append(' Score : ' + str(self._score))
    screen.append(bar)

    # Print
    os.system('cls')
    print('\n'.join(screen))


  def isRunning(self):
    return self._isRunning;


  def getScore(self):
    return self._score