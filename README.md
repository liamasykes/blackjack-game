# Blackjack Game

This is a Python implementation of the popular casino card game, Blackjack. This game was created using object-oriented programming, and it allows users to play Blackjack against a computer dealer. 

## Requirements
- Python 3

## How to Play
1. Run the `blackjack.py` script in your terminal.
2. You will be prompted with the dealer's face-up card and your two face-up cards.
3. You can choose to either "hit" or "stand". Enter "H" to hit, or "S" to stand.
4. If you choose to hit, you will receive another card, and your total score will increase.
5. If you choose to stand, the dealer will start hitting until their score is 17 or higher.
6. If you get a score of 21, you automatically win.
7. If your score exceeds 21, you automatically lose.
8. The game ends when you or the dealer reaches a score of 21, or when both you and the dealer choose to stand.

## Classes
### Blackjack
This class is responsible for the main gameplay of Blackjack. The `__init__` function initializes the game with the players, the game status, and a new deck. It also calls the `initialHand()` function to deal two cards to the dealer and the player. 

The `createUsers()` function creates two players: "Dealer" and "Player1". 

The `promptPlayer()` function prompts the user to choose between hitting and standing. It then calls the `determineInput()` function to determine the player's decision.

The `determineInput()` function takes the user's input and decides whether to call the `dealCard()` function to add a card to the player's hand or to end the game and call the `runDealer()` function.

The `runDealer()` function is called when the player chooses to stand. It makes the dealer keep hitting until their score is 17 or higher. 

The `dealCard()` function adds a new card to the player's hand and prints out the updated cards. 

The `printFunction()` function prints out the current cards for both the dealer and the player.

The `initialHand()` function is called at the beginning of the game to deal two cards to both the player and the dealer. If the player's initial score is 21, the game ends immediately.

The `replaceAce()` function replaces the value of an ace from 11 to 1 if the score exceeds 21.

The `gameOutcomes()` function checks the scores of the player and the dealer and determines the outcome of the game.

### Player
This class is responsible for managing a player's hand and score. The `__init__` function initializes the player's name, an empty hand, and a score of 0. 

The `addToHand()` function adds a new card to the player's hand and calls the `addToScore()` function to update the score.

The `addToScore()` function updates the player's score based on the value of the newly added card.

The `checkAce()` function checks if the player's hand contains an ace.

The `subtractTen()` function subtracts 10 from the player's score if the player has an ace and their score exceeds 21.

The `printHand()` function prints out the player's hand in a formatted way.