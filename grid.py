from time import sleep
from piece import Piece
from math import ceil 

class Grid:

  def __init__ (self):
    self._width = 10 
    self._height = 40
    self._rows = [ [' ']*self._width for i in range (self._height) ]
    self._changed = True


  def placePiece(self, piece: Piece):
    self.setChanged(True)
    body = piece.getBody();
    pos = piece.getPos();

    for y in range (0,len(body)):
      row = body[y]
      for x in range (0,len(row)):
        if (body[y][x] != ' '):
          self._rows[pos['y'] + y][pos['x'] + x] = body[y][x]


  def isPiecePlacable(self, piece: Piece):
    body = piece.getBody();
    pos = piece.getPos();

    # Check if touching another 
    for y in range (0,len(body)):
      row = body[y]
      for x in range (0,len(row)):
        if (body[y][x] != ' '):
          newX = pos['x'] + x
          newY = pos['y'] + y
          # Check if out of bounds
          if (newX < 0 or newX >= self._width or newY < 0 or newY >= self._height):
            return False 
        
          # Check if touching another piece
          if (self._rows[newY][newX] != ' '):
            return False

    return True
  

  def anyRowsFull(self):
    full = []
    for y in range(len(self._rows)):
      row = self._rows[y]
      for i in range(len(row)):
        if (row[i] == ' '):
          break 
        if (i == len(row) - 1):
          full.append(y)
    
    print('any full:')
    print(full)
    return full


  def clearRows(self, ys) -> int:
    self.setChanged(True)
    ys.sort();
    for y in ys:
      del self._rows[y]
      self._rows.insert(0, [' ']*10)
    return 100 * ceil(pow(len(ys), 1.5))
  

  def getRows(self):
    return self._rows
  

  def getChanged(self):
    return self._changed
  
  
  def setChanged(self, a: bool):
    self._changed = a 