class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card, show_card=False):
        if show_card:
            print(card)
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            value += card.get_value()

            if card.rank == 'A':
                aces += 1

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def __str__(self):
        return f"{self.cards} ({self.get_value()})"

    def __repr__(self):
        return f"{self.cards} ({self.get_value()})"
        #return f"{[hand for hand in self.]} {[hand.get_value() for hand in self.cards]}"