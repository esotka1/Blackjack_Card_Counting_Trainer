from deck import Deck
from hand import Hand
from player import Player
from strategy import hard_strategy
import settings


class BlackjackGame:

    def __init__(self):
        self.deck = Deck()

        self.players = [Player(*info) for info in settings.PLAYER_SETTINGS]
        self.dealer = Hand()

        self.curPlayer = 0

        self.count = 0

    def deal(self):

        for _ in range(2):
            for player in self.players:
                player.hand[0].add_card(self.deck.draw())

            self.dealer.add_card(self.deck.draw())

        return True

    def cards_reset(self):
        if len(self.deck.cards) < int(settings.NUM_DECKS * settings.RESHUFFLE_RATIO * 52):
            self.deck = Deck()
            print("Cards Shuffled")


    def nonuser_decsion(self, user_total, dealer_value):
        return hard_strategy[user_total][dealer_value - 2]

    def get_user_input (self):

        for player in self.players:

            hand_index = 0
            while hand_index < len(player.hand):
                hand = player.hand[hand_index]
                userInput = 'A'

                while userInput.upper() not in ('S','D'):
                    print(f"{player}")
                    if player.user:

                        userInput = input("Your Turn: (H = hit, S = Stand, D = Double, P = Split): ")
                        if not self.action(player, hand, userInput.upper()):
                            # BUST
                            break
                    else:
                        print(self.dealer.cards[0])
                        userInput = self.nonuser_decsion(hand.get_value(), self.dealer.cards[0].get_value())
                        if not self.action(player, hand, userInput.upper()):
                            # BUST
                            break
                hand_index += 1

        return True

    def action(self, curPlayer:Player, curHand: Hand, decision):
        # Returns if hand is still viable (not over 21)
        if decision == 'S':
            return True
        elif decision == 'H':
            curHand.add_card(self.deck.draw(), True)
            return curHand.get_value() < 22
        elif decision == 'D':
            # NEED TO DOUBLE BET
            curHand.add_card(self.deck.draw(), True)
            decision = 'S'
            return curHand.get_value() < 22
        elif decision == 'P':
            # FINISH UP SPLIT action
            old_hand = curHand

            if len(old_hand.cards) != 2:
                print("You can't split")
                return True

            if old_hand.cards[0].rank != old_hand.cards[1].rank:
                print("You can't split")
                return True

            new_hand = Hand()
            new_hand.add_card(old_hand.cards.pop())

            old_hand.add_card(self.deck.draw(), True)
            new_hand.add_card(self.deck.draw(), True)

            curPlayer.hand.append(new_hand)

            return True


