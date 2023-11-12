from deck import Deck
from hand import Hand
from player import Player


def main():
    players = [Player("player 0"), Player("player 2"), Player("player 3")]
    hand = Hand(players)
    hand.deal_cards()
    hand.uncover_community_cards(3)
    hand.print_ui()


if __name__ == '__main__':
    main()
