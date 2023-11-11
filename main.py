import random

VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ["clubs", "diamonds", "hearts", "spades"]

DEQUE = [(value, suit) for value in VALUES for suit in SUITS]

random.shuffle(DEQUE)
print(DEQUE.pop())
