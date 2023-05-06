import random

class Blackjack:
    """Blackjack Class // Blackjack game operations """

    # Blackjack constructor
    def __init__(self):
        self.players = self.createUsers()
        self.gameRunning = True
        self.deck = Deck()
        for player in self.players:
            self.dealCard(player)
            self.dealCard(player)
        self.players[0].printHand()
        self.players[1].printHand()
        self.deck.printDeck()

    # Create the players
    def createUsers(self):
        return [Player("Dealer"), Player("Player1")]
        
    # Deal a card to player chosen
    def dealCard(self, player):
        player.addToHand(self.deck)

    
class Player:
    """Player Class"""

    # Constructor assign player with given name, empty hand, and 0 total hand value
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    # Calls the method to remove card from deck...append to hand
    def addToHand(self, deck):
        self.hand.append(deck.removeFromDeck())

    # Messy print function properly prints cards in player's hand side-by-side
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
    
    # Constructor creates the deck list, call buildDeck() method to create the deck of 52 unique cards
    def __init__(self):
        self.deck = []
        self.buildDeck()

    # For 12 cards per set of 4 suits, add to deck list
    def buildDeck(self):
        for i in ["♧", "♤", "♡", "♢"]:
            for j in range(2, 15):
                self.deck.append(Cards(i, j))

    # Removes a random card from the deck, returns it to allow dealing
    def removeFromDeck(self):
        removedCard = self.deck.pop(random.randrange(len(self.deck)))
        return removedCard

    # Print function used for testing; Prints the entire deck of cards
    def printDeck(self):
        for card in self.deck:
            if card.value > 10:
                print("{} of {}".format(card.determineFace(card.value), card.suit))
            else:
                print("{} of {}".format(card.value, card.suit))


class Cards:
    """Cards Class"""

    # Upon initialization, assign a suit and value to a card object
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    # For face cards, assign a corresponding letter rather than an int > 10
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
