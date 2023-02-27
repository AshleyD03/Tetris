from grid import Grid 
from piece import Piece

class Game:

  def __init__ (self):
    self._alive = True 
    self._score = 0 
    self._grid = Grid()
    self._curP = Piece()
    self._nextP = Piece()

  #TODO
  def moveLeft (self):
    return 

  #TODO
  def moveRight (self):
    return 

  #TODO
  def moveDown (self):
    return 

  #TODO
  def rotateRight (self):
    return 

  #TODO 
  def swapPieces (self):
    return 

  #TODO 
  def nextPiece (self):
    return 

  #TODO 
  def addScore (self, a):
    self._score += a 

  #TODO 
  def printScreen (self):
    for line in self._grid.getPrintRows(self._curP):
      print(' '.join(line))
    return 