class Blackjack:
    """Blackjack Class"""
    

class Users:
    """Users Class"""


class Computer(Users):
    """Computer Class"""


class Player(Users):
    """Player Class"""

class Deck:
    """Deck Class"""


class Cards(Deck):
    """Cards Class"""


if __name__ == '__main__':
    print("Starting blackjack.py...\n\n")
    userInput = input("\"/start\" to play!\n")
    while(userInput != "/start"):
        userInput = input("Invalid command...\"/help\" to see list of commands.\n")
        if userInput == "/help": print("\nHelp Menu\n")
    Blackjack()