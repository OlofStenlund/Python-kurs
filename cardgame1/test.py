from Deck import Deck

test1 = Deck()
test1.shuffle_deck()
print(len(test1.cards))
kort = test1.pull_card()
print(type(kort.value.value))
print(kort.value.value)

print(len(test1.cards))
