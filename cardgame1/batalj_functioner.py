
# Draw card 1 and card 2
# Add to the piles
def draw_cards():
    kort1 = halvlek1.pull_card()
    pile1.append(kort1)
    print(f"player 1 card is: {kort1}")
    print(f"player 1 deck is now {len(halvlek1.cards)} cards big")
    if len(played_cards_player1.cards) > 0:
        if kort1 == played_cards_player1.cards[1]:
            halvlek1.shuffle_deck()
            played_cards_player1 = HalfDeck([])
        else:
            pass
    return kort1


# Cheks if a card comes face up.
# If so, shuffle the deck.
# Probably take the player as input?
def check_played_cards():
    if kort1.value.value > kort2.value.value:
        for i in pile1:
            halvlek1.cards.insert(0, i)
        for i in pile2:
            halvlek1.cards.insert(0, i)
        print("Player 1 gets the cards")
        played_cards_player1.cards.insert(-1, kort1)
        played_cards_player1.cards.insert(-1, kort2)
        print(f"Player 1 now has {len(played_cards_player1.cards)} played cards.")
        pile1 = []
        pile2 = []
        # print(played_cards_player1[1])
        input("")  


# Check to see which player wins
# If draw, let the piles be
def check_winner():
    pass
# Append the cards drawn to the risght decks.
# Append in order so the first card is always index 0
# Once index 0 is drawn again, the deck is instead shuffled
# Shuffle before drawing a new card
# If a player gets the cards, empty the pile
def append_cards():
    pass
