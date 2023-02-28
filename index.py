from math import floor
import keyboard
from time import sleep
from game import Game
from piece import Piece
from colorama import init 

moves = {
  "w": "up",
  "a": "left",
  "s": "down",
  "d": "right"
}

def getInput (): 
  keyboard.start_recording()
  sleep(0.016)
  return keyboard.stop_recording()

def main ():
  init()
  game = Game()
  clock = 0
  while game.isRunning():
    ks = getInput()
    for key in ks:
      onKeyPress(key, game)
      game.printScreen()

    # Time before going down
    clock += 1 

    if (clock >= max(5, 60 - floor(game.getScore() / 100))):
      clock = 0 
      game.moveDown()

    game.printScreen()

def onKeyPress (key: keyboard.KeyboardEvent, game: Game):
  # Check if actual keypress
  if (key.event_type == "up"):
    return 
  
  # Translate key name to action
  action = key.name 
  if (action in moves):
    action = moves[key.name]

  # Perform action
  match action:
    case "up":
      print(action)
      game.rotateRight();
    
    case "r":
      print(action)
      game.swapPieces();

    case "down":
      print(action)
      game.moveDown()

    case "left":
      print(action)
      game.moveLeft()

    case "right":
      print(action)
      game.moveRight()


if __name__ == "__main__":
  main()