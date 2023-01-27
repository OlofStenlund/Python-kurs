# ----- Imports -----
from Deck import Deck, HalfDeck

# ----- Variables -----
lek1 = Deck()
halvlek1_var = HalfDeck([])
halvlek2_var = HalfDeck([])
played_cards_player1_var = HalfDeck([])
played_cards_player2_var = HalfDeck([])
pile1_var = []
pile2_var = []

# ----- Functions -----
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

def draw_cards(playerno_arg, halvlek_arg, pile_arg):
    kort = halvlek_arg.pull_card()
    pile_arg.insert(-1, kort)
    print(f"Player {playerno_arg} card is: {kort}")
    return kort, pile_arg

def shuffle_drawn_cards(played_cards_arg, halvlek_arg):
    if len(halvlek_arg.cards) > 0:
        if len(played_cards_arg.cards) > 1:
            if halvlek_arg.cards[-1] == played_cards_arg.cards[0]:
                return True, halvlek_arg, played_cards_arg
            else:
                pass

    else:
        return 0

def check_drawn_cards(kort1, kort2, pile1, pile2):
    if kort1.value.value != kort2.value.value:
        if kort1.value.value > kort2.value.value:
            for i in pile1:
                halvlek1_var.insert_card(0, i)
                played_cards_player1_var.append_card(i)
            for i in pile2: 
                halvlek1_var.insert_card(0, i)
                played_cards_player1_var.append_card(i)
            print(f"Player 1 gets the cards.")   
            pile1.clear()
            pile2.clear()

        elif kort2.value.value > kort1.value.value:
            for i in pile1:
                halvlek2_var.insert_card(0, i)
                played_cards_player2_var.append_card(i)
            for i in pile2:
                halvlek2_var.insert_card(0, i)
                played_cards_player2_var.append_card(i)
            print(f"Player 2 gets the cards.")    
            pile1.clear()
            pile2.clear()            

    else: 
        print("Cards were the same value, draw again.")

def shuffle_func(halvlek_arg, played_cards_arg):    
        halvlek_arg.shuffle_deck()
        played_cards_arg = ([]) 
        return halvlek_arg, played_cards_arg
        
def check_for_winner():
    if len(halvlek1_var.cards) == 0:
        print("Player 1 has lost. Contratulations, player 2!")
        return True
    elif len(halvlek2_var.cards) == 0:
        print("Player 2 has lost. Contratulations, player 1!")
        return True
    else:
        pass

def main():
    split_deck()
    halvlek1_var.shuffle_deck()
    halvlek2_var.shuffle_deck()

    while True:
        a = shuffle_drawn_cards(played_cards_player1_var, halvlek1_var)
        b = shuffle_drawn_cards(played_cards_player2_var, halvlek2_var)
        if a == 0 or b == 0:
            check_for_winner()
            exit()        
        elif a == True: 
            halvlek1_var, played_cards_player1_var == shuffle_func(halvlek1_var, played_cards_player1_var)
        elif b == True:
            halvlek2_var, played_cards_player2_var == shuffle_func(halvlek2_var, played_cards_player2_var)
        else:
            pass
        kort1, pile1 = draw_cards(1, halvlek1_var, pile1_var)
        kort2, pile2 = draw_cards(2, halvlek2_var, pile2_var)
        check_drawn_cards(kort1, kort2, pile1, pile2)

        print(f"Player 1 now has a deck of {len(halvlek1_var.cards)} cards")
        print(f"Player 2 now has a deck of {len(halvlek2_var.cards)} cards")

# ----- Run! -----
main()