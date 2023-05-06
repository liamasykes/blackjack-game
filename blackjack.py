import random
import os

class Blackjack:
    """Blackjack Class // Blackjack game operations """

    # Blackjack constructor
    def __init__(self):
        self.players = self.createUsers()
        self.gameRunning = True
        self.deck = Deck()
        self.initialHand()

        self.promptPlayer()

    # Create the players
    def createUsers(self):
        return [Player("Dealer"), Player("Player1")]

    def promptPlayer(self):
        while self.gameRunning == True:
            userInput = input("Hit (H) / Stand (S)")
            self.determineInput(userInput)

    def determineInput(self, userInput):
        if userInput == "H" or userInput == "S":
            if userInput == "H": self.dealCard(self.players[1])
            else: self.runDealer()
        else: determineInput(input("Invalid option! Hit (H) / Stand (S)"))

    def runDealer(self):
        while players[0].score < 17:
            self.dealCard(players[0])
        
    # Deal a card to player chosen and print updated set
    def dealCard(self, player):
        player.addToHand(self.deck)
        self.printFunction()

    def printFunction(self):
        os.system('cls') # ClearScrn to keep sensible output
        if self.gameRunning == True: self.players[0].printCard() # If the game is !over (user hit) then dont show the hole card
        else: self.players[0].printHand() 
        self.players[1].printHand()

    def initialHand(self):
        for i in range(2):
            self.dealCard(self.players[1])
            self.dealCard(self.players[0])

    
class Player:
    """Player Class"""

    # Constructor assign player with given name, empty hand, and 0 total hand value
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    # Calls the method to remove card from deck, append to hand, add value to score
    def addToHand(self, deck):
        dealtCard = deck.removeFromDeck()
        self.hand.append(dealtCard)
        self.addToScore(dealtCard)

    # Add value of card to score, if face card add 10
    def addToScore(self, dealtCard):
        if dealtCard.value == 14:
            if self.score + 11 > 21: self.score += 1
            else: self.score += 11
        if dealtCard.value > 9: self.score += 10
        else: self.score += dealtCard.value

    # Messy print function properly prints cards in player's hand side-by-side
    def printHand(self):
        print("{}'s hand: {}".format(self.name, self.score))
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

    # Messy print function to print single card; for dealer's face up (still need to be dealt a second card for fairness)
    def printCard(self):
        for card in self.hand: 
            print("{}'s hand: {}".format(self.name, card.value))
            print("┌─────────┐")
            print("│ {}       │".format(card.suit))
            print("│         │")
            if card.value == 10: print("│    {}   │".format(card.value))
            else: print("│    {}    │".format(card.determineFace(card.value)))
            print("│         │")
            print("│       {} │".format(card.suit))
            print("└─────────┘")
            break

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
