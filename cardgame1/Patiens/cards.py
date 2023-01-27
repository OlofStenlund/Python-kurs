from enum import Enum
from typing import List
from random import shuffle

class CardValue(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    KNIGHT = "Knight"
    QUEEN = "Queen"
    KING = "King"


class CardSuit(Enum):
    HEARTS = "♡"
    DIAMONDS = "♢"
    SPADES = "♠"
    CLUBS = "♣"

class Card:
    suit: CardSuit
    value: CardValue

    def __init__(self, suit, value): # value refers to class CardValue, suit refers to class CardCalue
        self.suit = suit
        self.value = value


    def __str__(self):
        return f"{self.suit.value} {self.value.value}" #self.suit.value = self.suit referes to class Cardsuit, take the value from that ie. the enum-value
                                                        # self.value.value -> tkae the value from "self.value" which refers to the class CardValue

class Deck:
    cards: List[Card] = [] # Create an empty list containing items of the class Card. This is the draw pile?

    def __init__(self):
        for suit in CardSuit:
            for value in CardValue:
                self.cards.append(Card(suit, value))
                # print(Card(suit, value))



    def pull_card(self):
        return self.cards.pop()

    def shuffle_deck(self):
        shuffle(self.cards)

