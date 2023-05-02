class Blackjack:
    """Blackjack Class"""

    def __init__(self):
        self.createUsers()

    def createUsers(self):
        computerUser = Computer()
        playerUser = Player()
        deck = Deck()
        deck.printDeck()


class Users:
    """Users Class"""


class Computer(Users):
    """Computer Class"""

    def __init__(self):
        self.name = "Dealer"
        print("My name is " + self.name)


class Player(Users):
    """Player Class"""

    def __init__(self):
        self.name = "Player"
        print("My name is " + self.name)


class Deck:
    """Deck Class"""
    
    # Create the 52 card deck and dictionary suits for UI
    def __init__(self):
        self.suits = { "Clubs" : "♧", "Spades" : "♤", "Hearts" : "♡", "Diamonds" : "♢" }
        self.cards = []
        self.buildDeck()
    
    def buildDeck(self):
        for i in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            for j in range(2, 15):
                self.cards.append(Cards(i, j))

    def removeFrom(self):
        pass

    def printDeck(self):
        for card in self.cards:
            card.printCard(card)

class Cards:
    """Cards Class"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def determineFace(self, value):
        switch_faces = {
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace"
        }
        return switch_faces.get(value)

    def printCard(self, card):
        if card.value > 10:
            print("{} of {}".format(self.determineFace(card.value), card.suit))
        else:
            print("{} of {}".format(self.value, self.suit))


if __name__ == '__main__':
    print("Starting blackjack.py...\n\n")
    userInput = input("\"/start\" to play!\n")
    while(userInput != "/start"):
        if userInput == "/help":
            print("\nHelp Menu\n")
            userInput = input()
        else: userInput = input("Invalid command...\"/help\" to see list of commands.\n")
        
    Blackjack()
