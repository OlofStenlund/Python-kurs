from Deck import Deck

def InputError(Exception):
    pass


def main():
    deck = Deck() # create an object of class deck to draw from
    deck.shuffle_deck()
    while len(deck.cards) > 0:
        if len(deck.cards) == 52:
            print("Here is the first card: ")
            card = deck.pull_card() 
            print(card)
            card_value = card.value.value
        else:
            pass
        guess = input(f"Will the next value be higher or lower than {card}? Or maybe the same? (H/L/S): ")
        second_card = deck.pull_card()
        second_card_value = second_card.value.value
        print(card_value, type(card_value))
        print(second_card_value, type(second_card_value))
        if guess == "H" and second_card_value > card_value:
            print(f"Correct! You drew {second_card}, which is higher than {card}")
        elif guess == "L" and second_card_value < card_value:
            print(f"Correct! You drew {second_card}, which is lower than {card}")
        elif guess == "S" and second_card_value == card_value:
            print(f"Correct! You drew {second_card}, which is the same as {card}")
        elif guess != "H" and guess != "L" and guess != "S":
            print("Invalid input, try again.")
            continue   
        else:
            print(f"You were wrong! \nThe next card was {second_card}")
        card = second_card 
        card_value = second_card_value

main()
