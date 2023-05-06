import random

class Blackjack:
    """Blackjack Class"""

    def __init__(self):
        self.players = self.createUsers()
        self.gameRunning = True
        self.deck = Deck()
        for player in self.players:
            self.dealCard(player)
            self.dealCard(player)
            self.dealCard(player)
        self.players[0].printHand()
        self.players[1].printHand()
        self.deck.printDeck()

    def createUsers(self):
        return [Player("Dealer"), Player("Player1")]
        
    def dealCard(self, player):
        player.addToHand(self.deck)

    


class Player:
    """Users Class"""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def addToHand(self, deck):
        self.hand.append(deck.removeFromDeck())

    def printHand(self):
        print("My name is {}".format(self.name))
        for card in self.hand: print("┌─────────┐", end=" ")
        print()
        for card in self.hand: print("│ {}       │".format(card.suit), end=" ")
        print()
        for card in self.hand: print("│         │", end=" ")
        print()
        for card in self.hand: 
            if card.value == 10:
                print("│    {}   │".format(card.value), end=" ")
            else:
                print("│    {}    │".format(card.determineFace(card.value)), end=" ")
        print()
        for card in self.hand: print("│         │", end=" ")
        print()
        for card in self.hand: print("│       {} │".format(card.suit), end=" ")
        print()
        for card in self.hand: print("└─────────┘", end=" ")
        print()

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

    def removeFromDeck(self):
        removedCard = self.deck.pop(random.randrange(len(self.deck)))
        return removedCard

    def printDeck(self):
        for card in self.deck:
            if card.value > 10:
                print("{} of {}".format(card.determineFace(card.value), card.suit))
            else:
                print("{} of {}".format(card.value, card.suit))

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

if __name__ == '__main__':
    print("Starting blackjack.py...\n\n")
    userInput = input("\"/start\" to play!\n")
    while(userInput != "/start"):
        if userInput == "/help":
            print("\nHelp Menu\n")
            userInput = input()
        else: userInput = input("Invalid command...\"/help\" to see list of commands.\n")
        
    Blackjack()
