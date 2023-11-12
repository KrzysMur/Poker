from deck import Deck, format_card


class Hand:
    def __init__(self, players):
        self.players = players
        self.pot = 0
        self.deck = Deck()
        self.community_cards = []

    def deal_cards(self):
        for _ in range(2):
            for player in self.players:
                player.cards.append(self.deck.take_card_from_deck())

    def uncover_community_cards(self, n):
        for _ in range(n):
            self.community_cards.append(self.deck.take_card_from_deck())

    def print_ui(self):
        print(f"              Pot:      {self.pot}")
        print(self.community_cards)
        for player in self.players:
            print(f"              {player.name}:  {player.stack}   {format_card(player.cards[0])}  {format_card(player.cards[1])}")
        print("Action input")