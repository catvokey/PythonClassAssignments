
from dataclasses import dataclass

import random

@dataclass
class Card:
    rank: str
    suit: str

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def get_str(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.build_deck()

    def build_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def count_cards(self):
        return len(self.cards)

    def deal_card(self):
        return self.cards.pop()

def main():
    deck = Deck()
    deck.shuffle_deck()

    print("Card Dealer")
    print()
    print(f"I have shuffled a deck of {deck.count_cards()} cards.")
    print()

    user_cards = int(input("How many cards would you like? "))
    print()
    print("Here are your cards:")
    for card in range(user_cards):
        card = deck.deal_card()
        print(f"{card.get_str()}")
    print()

    print(f"There are {deck.count_cards()} cards left in the deck.")
    print()
    print("Good luck!")

if __name__ == "__main__":
    main()