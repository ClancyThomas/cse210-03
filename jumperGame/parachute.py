class Image: 

    def __init__(self):
        self._image = ""

    # Updates the parachute image based on the amount of lives left
    def updateParachute(self, livesLeft):
        match livesLeft:
            case 0:
                self._image = "\n  X \n -|-\n / \ \n\n ^^^^^^^^^^^ \n\n YOU LOST!!!\n"
            case 1:
                self._image = "\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 2:
                self._image = "\n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 3:
                self._image = "\n ____  \n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 4:
                self._image = "\n/____\ \n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 5:
                self._image = "\n ____\n/____\ \n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case _: 
                self._image = "BROKEN"
    
    def getImage(self):
        return self._image




