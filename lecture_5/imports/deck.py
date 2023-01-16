from typing import List
from imports.card import Card, CardSuit, CardValue

class Deck:
    cards: List[Card] = []

    def __init__(self):
        for suit in CardSuit:
            for value in CardValue:
                self.cards.append(Card(suit, value))
        for card in self.cards:
            print(card)

    def pull_card(self):
        return self.cards.pop()