import pygame

from blackjack_game import BlackjackGame
from button import Button
from deck import Deck

print("\n" * 10)

Active = True
print("------------- Welcome to Blackjack -------------")
print("Once Cards are dealt press ENTER for all details")
print("\n" * 2)

while Active:
    userInput = input("Press S to Start (Anything else to exit): ")

    if userInput.upper() != 'S':
        break

    game = BlackjackGame()
    game.deal()

    print(f"\nDealer: {game.dealer.cards[0]}")
    for player in game.players:
        print(f"{player.name}: {player.hand}")

    print("\n")

    game.get_user_input()
'''
    for player in game.players:
        for hand in player.hand:
            print(f"Current Hand: {hand}")
            userInput = 'A'

            if player.user:

                while userInput.upper() != 'S': # Starts with S, need to fix
                    userInput = input("Your Turn: (H = hit, S = Stand, D = Double, P = Split)")

            else:
                print(game.dealer.cards[0])
                userInput = game.nonuser_turn(hand.get_value(),game.dealer.cards[0].get_value())
'''