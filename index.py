import keyboard
from time import sleep
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
  currentPiece = Piece() 

  while True:
    ks = getInput()
    for key in ks:

      # Check if actual keypress
      if (key.event_type == "up"):
        continue

      # Translate key to move
      name = key.name 
      if (name in moves):
        name = moves[key.name]

      # Match key to action
      match name:
        case "up":
          currentPiece.rotateRight();

        case "r":
          currentPiece = Piece () 


      print("------")
      for line in currentPiece.getBody():
        print(' '.join(line))
      print("------")
      sleep(0.016)

if __name__ == "__main__":
  main()