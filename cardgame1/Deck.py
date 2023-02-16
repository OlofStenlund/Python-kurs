# Higher lower, but with a deck of playing cards

from typing import List
from Cards import CardSuit, CardValue
from random import shuffle
from dataclasses import dataclass


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

        

class HalfDeck:
    cards: List[Card] = []

    def __init__(self, cards):
        self.cards = cards

    def shuffle_deck(self):
        shuffle(self.cards)

    def pull_card(self):
        return self.cards.pop()

    def append_card(self, x):
        self.cards.append(x)
    
    def insert_card(self, x, y):
        self.cards.insert(x, y)



class MemoryDeck():
    cards: List[Card] = []

    def __init__ (self, x):
        for suit in CardSuit.CLUBS.value:
            for value in CardValue:
                if value.value <= x:
                    self.cards.append(Card(suit, value))
                    self.cards.append(Card(suit, value))
        return x
    def choose_card(self, number):
        num = number-1
        return self.cards[num]

    def shuffle_deck(self):
        shuffle(self.cards)
       


# when main is run, we create an objcet called "deck" that is of the class Deck
# An object of class Deck contains a list of objects och class Card.
# init-method runs, for each suit in cardsuit it will go to each value in cardvalue
# it will then append the list cards with an object of class Card
# suit is CardSuit (in Cards), return value in __str__ method becomes self.suit.value, ie the value from the suit class
# value is CardValue (in Cards), return values in __str__ method becomes self.value.value. ir the value from the value class
#  



# Checks that this is the file that's run
# The file that is run is always named __main__
# If a file runs imports from other files, these names will be the names of the files.
# If we import cards, and run main, then main == __main__ and cards == __cards__
# If we run cards, cards == __main__

# if __name__ == '__main__':
#     main()
