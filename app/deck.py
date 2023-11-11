import random

VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = [9828, 9825, 9831, 9826]


class Deck:
    def __init__(self, shuffle=True):
        self.deck = [(value, suit) for value in VALUES for suit in SUITS]
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def take_card_from_deck(self):
        return self.deck.pop()
