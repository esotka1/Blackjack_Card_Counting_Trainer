from deck import Deck
from hand import Hand
from settings import NUM_PLAYERS


class Player:

    def __init__(self, bankroll=0, name='bot',user=False):

        self.name = name
        self.bankroll = bankroll
        self.user = user
        self.hand = [Hand()]

    '''
    def split(self, deck, curHand):
        old_hand = self.hand[curHand]

        if len(old_hand.cards) != 2:
            return False

        if old_hand.cards[0].rank != old_hand.cards[1].rank:
            return False

        new_hand = Hand()
        new_hand.add_card(old_hand.cards.pop())

        old_hand.add_card(deck.draw())
        new_hand.add_card(deck.draw())

        self.hand.append(new_hand)

        return True
    '''

    def __repr__(self):
      return f"{self.name}: {self.hand}"