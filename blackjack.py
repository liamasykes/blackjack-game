import random

class Blackjack:
    """Blackjack Class"""

    def __init__(self):
        self.createUsers()
        self.gameRunning = True

    def createUsers(self):
        Players = [Computer("Dealer"), Player("Player1")]
        deck = Deck()
        deck.removeFrom()
        for player in Players:
            player.receiveCard(deck)
        deck.printDeck()
        
    def dealCards(self, player):
        pass


class Users:
    """Users Class"""

    def receiveCard(self, deck):
        self.hand.append(deck.removeFrom())
        print(self.name)
        print(self.hand)
        print("My hand is: ")
        for card in self.hand:
            card.printCard(card)

class Computer(Users):
    """Computer Class"""

    def __init__(self, name):
        self.name = name
        self.hand = []


class Player(Users):
    """Player Class"""

    def __init__(self, name):
        self.name = name
        self.hand = []


class Deck:
    """Deck Class"""
    
    # Create the 52 card deck and dictionary suits for UI
    def __init__(self):
        self.suits = { "Clubs" : "♧", "Spades" : "♤", "Hearts" : "♡", "Diamonds" : "♢" }
        self.deck = []
        self.buildDeck()
    
    def buildDeck(self):
        for i in ["♧", "♤", "♡", "♢"]:
            for j in range(2, 15):
                self.deck.append(Cards(i, j))

    def removeFrom(self):
        removedCard = self.deck.pop(random.randrange(len(self.deck)))
        return removedCard

    def printDeck(self):
        for card in self.deck:
            card.printCard(card)

class Cards:
    """Cards Class"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def determineFace(self, value):
        switch_faces = { # Jack, Queen, King, Ace, Respectively
            11: "J",
            12: "Q",
            13: "K",
            14: "A"
        }
        if value > 10: return switch_faces.get(value)
        else: return value

    def printCard(self, card):
        print("┌─────────┐")
        print("│ {}       │".format(self.suit))
        print("│         │")
        if card.value == 10:
            print("│    {}   │".format(card.value))
        else:
            print("│    {}    │".format(self.determineFace(card.value)))
        print("│         │")
        print("│       {} │".format(self.suit))
        print("└─────────┘")


if __name__ == '__main__':
    print("Starting blackjack.py...\n\n")
    userInput = input("\"/start\" to play!\n")
    while(userInput != "/start"):
        if userInput == "/help":
            print("\nHelp Menu\n")
            userInput = input()
        else: userInput = input("Invalid command...\"/help\" to see list of commands.\n")
        
    Blackjack()
