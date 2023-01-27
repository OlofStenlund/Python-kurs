from enum import Enum
from typing import List
from random import shuffle
from cards import CardSuit, CardValue, Card, Deck

game = Deck()
game.shuffle_deck()


# print(nyttkort.value.value)
# print(type(nyttkort.value.value))

# Draw one card, put in a list
# Draw 2 cards, put in a list
# Draw 3 cards, put in a list
# Draw 4 cards, put in a list
# Draw 5 cards, put in a list
# Draw 6 cards, put in a list
# Draw 7 cards, put in a list



# layer6 kort 5 och 6 borta, öppnar kort 5
# kort 4 och 5 borta öppnar 4
# kort 3 och 4 borta öppnar kort 3
# kort kort 2 och 3 borta öppnar kort 2
# kort 1 och 2 borta öpnar kort 1


# Ta in input
# Om de korten summar till 13, ta bort dem
# detta ska låsa upp korten under enligt ovan

row1 = ["X"]
row2 = ["X", "X"]
row3 = ["X", "X", "X"]
row4 = ["X", "X", "X", "X"]
row5 = ["X", "X", "X", "X", "X"]
row6 = ["X", "X", "X", "X", "X", "X"]
row7 = []

secretrow1 = []
secretrow2 = []
secretrow3 = []
secretrow4 = []
secretrow5 = []
secretrow6 = []
secretrow7 = []

trash = []

while len(row7) < 7:
    card = game.pull_card()
    cardvalue = card.value.value
    cardsuit = card.suit.value
    row7.append(card)
    if card.value.value == "King":
        secretrow7.append(13)
    elif card.value.value == "Queen":
        secretrow7.append(12)
    elif card.value.value == "Knight":
        secretrow7.append(11)
    else:
        secretrow7.append(int(card.value.value))


def print_board():
    print(f"X")
    print(f"X   X")
    print(f"X   X   X")
    print(f"X   X   X   X")
    print(f"X   X   X   X   X")
    print(f"X   X   X   X   X   X")
    print(f"{row7[0]}  {row7[1]}  {row7[2]}  {row7[3]}  {row7[4]}  {row7[5]}  {row7[6]}")




# From stackoverflow'
def check_for_13():
    for i, number in enumerate(secretrow7[:-1]):  
        complementary = 13 - number
        if complementary in secretrow7[i+1:]:
            for i in secretrow7:
                if i == number:
                    print(f"Yesss, detta är {i}, number")
                    ind1 = secretrow7.index(i)
                    # print(f"index {ind}, number")
                    row7[ind1] = 'X'
                    break
            for i in secretrow7:
                if i == complementary:
                    print(f"Yesss, detta är {i}, complementary")
                    ind2 = secretrow7.index(i)
                    # print(f"index {ind}, complementary")
                    row7[ind2] = 'X'
                    break
            break
        else:
            print("There is no solution. Start the game again.")
            break
    return [number, complementary]


# stop = False
# while stop == False:
print_board()
retur = check_for_13()
print(retur)
ret1 = retur[0]
ret2 = retur[1]
print(ret1)
print(ret2)

# for i in row6:
#     if retur[0] == row6.index(i) and retur[1] == row6.index(i+1):
#         print("Funkar det?")
print_board()
# print_board()
# check_for_13()
# print_board()

        # for i in row7:
        #     if i == number:
        #         print(f"yes this is {i} number")
        #         ind = row7.index(i) 
        #         print(ind)
        #         # row7[ind] = 'X'
        #         break
        #     elif i == complementary:
        #         print(f"yes this is {i} complementar")
        #         ind = row7.index(i)
        #         print(ind)
        #         # row7[ind] = 'X'
        #         break

#-----------------------------------------------


# layer1 = [0]
# layer2 = [0,0]
# layer3 = [0,0,0]
# layer4 = [0,0,0,0]
# layer5 = [0,0,0,0,0]
# layer6 = [0,0,0,0,0,0]
# layer7 = [0,0,0,0,0,0,0]


# layerlist = [layer1, layer2, layer3, layer4, layer5, layer6, layer7]

# def populate_board():
#     for i in layerlist: 
#         upp = 0 
#         while i.count(0) > 0:
#             kort = game.pull_card()
#             i[upp] = kort
#             upp += 1


# populate_board()

# def print_board():
#     print(f"{layer1[0]}")
#     print(f"{layer2[0]}  {layer2[1]}")
#     print(f"{layer3[0]}  {layer3[1]}  {layer3[2]}")
#     print(f"{layer4[0]}  {layer4[1]}  {layer4[2]}  {layer4[3]}")
#     print(f"{layer5[0]}  {layer5[1]}  {layer5[2]}  {layer5[3]}  {layer5[4]}")
#     print(f"{layer6[0]}  {layer6[1]}  {layer6[2]}  {layer6[3]}  {layer6[4]}  {layer6[5]}")
#     print(f"{layer7[0]}  {layer7[1]}  {layer7[2]}  {layer7[3]}  {layer7[4]}  {layer7[5]}  {layer7[6]}")

# print_board()
# print("The game will run. Press enter to see the next move!")
# layer7[6] = "X"


# print_board()