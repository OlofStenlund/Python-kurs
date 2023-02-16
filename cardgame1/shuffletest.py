from Deck import Deck, HalfDeck

lek1 = Deck()
halvlek1_var = HalfDeck([])
halvlek2_var = HalfDeck([])
played_cards_player1_var = HalfDeck([])
played_cards_player2_var = HalfDeck([])
pile1_var = []
pile2_var = []

def split_deck():
    while True:
        while len(halvlek1_var.cards) < 26: 
            card = lek1.pull_card()
            halvlek1_var.cards.append(card)
        while len(halvlek1_var.cards) == 26 and len(halvlek2_var.cards) < 26:
            card = lek1.pull_card()
            halvlek2_var.cards.append(card)
        else:
            break

split_deck()
print(len(halvlek1_var.cards))
print(len(halvlek2_var.cards))

kort1 = halvlek1_var.pull_card()
kort2 = halvlek2_var.pull_card()
pile1_var.insert(-1, kort1)
pile2_var.insert(-1, kort2)
print(kort1)
print(kort2)
for i in pile1_var, pile2_var:
    halvlek1_var.insert_card(-1, i)
    # halvlek2_var.insert_card(-1, i)
print(len(pile1_var))
print(len(pile2_var))
pile1_var.clear()
pile2_var.clear()
print(len(pile1_var))
print(len(pile2_var))
print(len(halvlek1_var.cards))
print(len(halvlek2_var.cards))

halvlek1_var.shuffle_deck()
halvlek2_var.shuffle_deck

kort1 = halvlek1_var.pull_card()
kort2 = halvlek2_var.pull_card()
pile1_var.insert(-1, kort1)
pile2_var.insert(-1, kort2)
print(kort1)
print(kort2)
for i in pile1_var, pile2_var:
    halvlek1_var.insert_card(-1, i)
    # halvlek2_var.insert_card(-1, i)
print(len(pile1_var))
print(len(pile2_var))
pile1_var.clear()
pile2_var.clear()
print(len(pile1_var))
print(len(pile2_var))
print(len(halvlek1_var.cards))
print(len(halvlek2_var.cards))
