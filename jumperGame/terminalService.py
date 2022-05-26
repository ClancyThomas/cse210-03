class terminalService:

    def __init__(self):
        self.start = ""

    # Handles all the printing for each turn of the game
    def printGame(self, parachute, word):
        self.printWord(word)
        print(parachute)

    # Prints the word in an easy to read format
    def printWord(self, word):
        print()
        for i in range(0, len(word)):
            print(f"{word[i]} ", end="")
        print()



    
