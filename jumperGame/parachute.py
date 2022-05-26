class Image: 

    def __init__(self):
        self.image = ""

    def updateParachute(self, livesLeft):
        match livesLeft:
            case 0:
                self.image = " X \n-|-\n/ \ "
            case 1:
                self.image = "\  /\nO\n-|-\n/ \ "
            case 2:
                self.image = "\    /\n\  /\nO\n-|-\n/ \ "
            case 3:
                self.image = " ____  \n\    /\n\  /\nO\n-|-\n/ \ "
            case 4:
                self.image = "/____\ \n\    /\n\  /\nO\n-|-\n/ \ "
            case 5:
                self.image = " ____\n/____\ \n\    /\n\  /\nO\n-|-\n/ \ "
            case _: 
                self.image = "BROKEN"
    
    def getImage(self):
        return self.image



