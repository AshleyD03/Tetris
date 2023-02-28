
class Grid:

  def __init__ (self):
    self._rows = [ [' ']*10 for i in range (40) ]

  def placePiece(self, piece):
    body = piece.getBody();
    pos = piece.getPos();

    for y in range (0,len(body)):
      row = body[y]
      for x in range (0,len(row)):
        if (body[y][x] != ' '):
          self._rows[pos.y + y][pos.x + x] = body[y][x]


  #TODO
  def isPiecePlacable(self, piece):
    return 

  #TODO 
  def isRowFull(self):
    return 

  #TODO
  def clearRow(self):
    return 