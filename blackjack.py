class Blackjack:
    """Blackjack Class"""

    def __init__(self):
        self.createUsers()

    def createUsers(self):
        computerUser = Computer()
        playerUser = Player()
        cards = Cards()


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
    
    def __init__(self):
        self.suits = { "Clubs" : "♧", "Spades" : "♤", "Hearts" : "♡", "Diamonds" : "♢" }
        self.cards = Cards()

class Cards(Deck):
    """Cards Class"""

    def __init__(self):
        self.total = 52
    

if __name__ == '__main__':
    print("Starting blackjack.py...\n\n")
    userInput = input("\"/start\" to play!\n")
    while(userInput != "/start"):
        if userInput == "/help":
            print("\nHelp Menu\n")
            userInput = input()
        else: userInput = input("Invalid command...\"/help\" to see list of commands.\n")
        
    Blackjack()
