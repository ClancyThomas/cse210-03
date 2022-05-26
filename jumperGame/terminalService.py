class terminalService:

    def __init__(self):
        self.print = ""

    def printGame(self, parachute, word):
        self.printWord(word)
        print(parachute)

    def printWord(self, word):
        print()
        for i in range(0, len(word)):
            print(f"{word[i]} ", end="")
        print()



    
