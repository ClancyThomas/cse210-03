class Image: 

    def __init__(self):
        self.image = ""

    # Updates the parachute image based on the amount of lives left
    def updateParachute(self, livesLeft):
        match livesLeft:
            case 0:
                self.image = "\n  X \n -|-\n / \ \n\n ^^^^^^^^^^^ \n\n YOU LOST!!!\n"
            case 1:
                self.image = "\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 2:
                self.image = "\n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 3:
                self.image = "\n ____  \n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 4:
                self.image = "\n/____\ \n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case 5:
                self.image = "\n ____\n/____\ \n\    /\n \  /\n  O\n -|-\n / \ \n\n^^^^^^^^^^^"
            case _: 
                self.image = "BROKEN"
    
    def getImage(self):
        return self.image




