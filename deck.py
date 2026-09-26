import random

from card import Card
from settings import NUM_DECKS


class Deck:

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self):
        self.cards = [Card(s, r) for s in Deck.suits for r in Deck.ranks] * NUM_DECKS
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __str__(self):
        return f"{len(self.cards)}: {self.cards}"

    def __repr__(self):
        return f"Deck({len(self.cards)} cards)"