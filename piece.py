from random import randint 
from colorama import Fore

class Piece:

  def __init__ (self):
    self._num = randint (0,5)
    self._body = self.makeBody(self._num);
    self._x = 4
    self._y = 20
    self._changed = True


  def moveLeft (self):
    self._x -= 1
    self.setChanged(True)


  def moveRight (self):
    self._x += 1
    self.setChanged(True)


  def moveDown (self):
    self._y += 1;
    self.setChanged(True)


  def rotateRight(self):
    self._body = self.rotateBody(self._body)
    self.setChanged(True)


  def getBody(self):
    return self._body 


  def resetPos(self):
    self._x=4
    self._y=20


  def getPos(self):
    return {'x': self._x, 'y': self._y}


  @staticmethod
  def rotateBody (body: list[list[str]]):
    def rotate (body): 
      return list(zip(*body[::-1]))

    body = rotate(body)

    # Handle issues with rotate line piece
    if (len(body) == 4): 
      if (body[0][2] != ' '):
        body = rotate(rotate(body))
      elif (body[2][3] != ' '):
        body = rotate(body)

    return body 


  def getChanged(self):
    return self._changed
  

  def setChanged(self, a: bool):
    self._changed = a 


  @staticmethod
  def makeBody (k: list[list[str]]):
    body = []
    color = Fore.CYAN
    match k: 
      # Line Piece
      case 0:
        body = [
          ['','','',''],
          ['▇','▇','▇','▇'],
          ['','','',''],
          ['','','','']
        ]
      # L Right
      case 1:
        color = Fore.BLUE
        body = [
          ['','',''],
          ['▇','▇','▇'],
          ['','','▇']
        ]
      # L Left
      case 2:
        color = Fore.WHITE
        body = [
          ['','',''],
          ['▇','▇','▇'],
          ['▇','','','']
        ]
      # Square
      case 3:
        color = Fore.YELLOW
        body = [
          ['▇','▇'],
          ['▇','▇']
        ]
      # S Right
      case 4:
        color = Fore.GREEN
        body = [
          ['','',''],
          ['','▇','▇'],
          ['▇','▇','']
        ]

      # T shape 
      case 5:
        color = Fore.MAGENTA
        body = [
          ['','▇',''],
          ['▇','▇','▇'],
          ['','','']
        ]
      # S Left
      case 6:
        color = Fore.RED
        body = [
          ['','',''],
          ['▇','▇',''],
          ['','▇','▇']
        ]

    body = list(map(lambda x: list(map(lambda y: color + y + Fore.RESET if y != '' else ' ', x)), body))
    return body 