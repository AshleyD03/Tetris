from random import randint 
from colorama import Fore

class Piece:

  def __init__ (self, x=1, y=1):
    self._num = randint (0,5)
    self._body = self.makeBody(self._num);
    self._x = x
    self._y = y

  def moveLeft (self):
    if (self._x + len(self._body[0]) + 1 < 10): 
      self._x += 1

  def moveRight (self):
    if (self._x - 1 < 0):
      self._x -= 1

  def rotateRight(self):
    self._body = self.rotateBody(self._body)

  def getBody(self):
    return self._body 

  def getPos(self):
    return {'x': self._x, 'y': self._y}

  @staticmethod
  def rotateBody (body):
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

  @staticmethod
  def makeBody (k):
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

