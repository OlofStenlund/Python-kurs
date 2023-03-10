from typing import List
from Deck import Card, MemoryDeck
from random import shuffle
import os

# Next step: Controll input variables
    # Make sure they are int 
    # Make sure they are in range
    # Cannot be picked if removed


row1 = ['|  1 ', '|  2 ', '|  3 ', '|  4 ']
row2 = ['|  5 ', '|  6 ', '|  7 ', '|  8 ']
row3 = ['|  9 ', '|  10 ', '|  11 ', '|  12 ']

board = [row1, row2, row3] 

card_pairs_number = 6
kort_spelplan = MemoryDeck(card_pairs_number)
kort_spelplan.shuffle_deck()
removed_pairs = 0

def create_board():

    spelplan = []
    for i in kort_spelplan.cards:
        spelplan.append(i)

print(len(kort_spelplan.cards))
def print_board():
    for row in board:
        print(*row)

def first_guess():
        numberinp1 = int(input("Which card would you like to look at?"))
        firstchoice = kort_spelplan.choose_card(numberinp1)
        k1 = " " + str((firstchoice.suit + " " + str(firstchoice.value.value)))
        return firstchoice, k1, numberinp1

def second_guess():
    numberinp2 = int(input("Where do you think the corresponding card is?"))
    secondchoice = kort_spelplan.choose_card(numberinp2)
    k2 = " " + str((secondchoice.suit + " " + str(secondchoice.value.value)))
    return secondchoice, k2, numberinp2

def find_indexes(numberinp):
    guess: str = " " + str(numberinp) + " "
    os.system('cls')
    print(guess)
    for i in board:
        for x in i:
            if guess in x:
                indx = [a for a, j in enumerate(i) if guess in j]
                indexinrow = indx[0]
                boardindex = board.index(i)
    return boardindex, indexinrow

def main():
    create_board()
    print_board()
    removed_pairs = 0
    while removed_pairs < card_pairs_number:
    
        firstchoice, k1, numberinp1 = first_guess()
        print_board()
        boardindex, indexinrow = find_indexes(numberinp1)
        board[boardindex][indexinrow] = f"| {k1}"
        os.system('cls')
        print_board()
        secondchoice, k2, numberinp2= second_guess()
        boardindex2, indexinrow2 = find_indexes(numberinp2)
        board[boardindex2][indexinrow2] = f"| {k2}"
        os.system('cls')
        print_board()
        print("Here they are. (Press any key to continue)")
        input("")
        os.system('cls')
        print_board()

        if firstchoice.value.value == secondchoice.value.value:        
            print("Contratulations, the cards matched!")
            input("Press any key to contine")
            board[boardindex][indexinrow] = f"|   "
            board[boardindex2][indexinrow2] = f"|   "        
            removed_pairs += 1        
        else:
            print("No match.")
            input("Press any key to contine")
            board[boardindex][indexinrow] = f"|  {numberinp1} "
            board[boardindex2][indexinrow2] = f"|  {numberinp2} "
            for row in board:
                print(*row)    

        os.system('cls')
        print("Here is the board again")        
        for row in board:
            print(*row)


main()
print("That's all folks. Good night!")





















# Memory

# Kan man f?? likadana kort utspelade tv?? g??nger? Hur?
# Skriva ut en suit tv?? g??nger?
    # Hur
# Designa en egen lek?
# Skriv ut br??de med X * X antal kort
# Tv?? listor, en ??ppen och en dold?# J??mf??r med dem och se om de ??r samma
# Spelaren v??nder upp ett kort, det v??rdet sparasi x.
# V??ljer n??sta kort, om det har samma v??rde som x, avsl??ja det. Ge po??ng.

# Steg 1:
    # Skapa ett br??de och tilldela kort.
    # Se till att korten finns i en ??ppen och en dold lista f??r j??mf??relse.

# Steg 2:
    # Skapa po??ngsystem f??t tv?? spelare
    # Loop d??r spelare drar ett kort som visas direkt
        # V??lja ett till kort att visa. OM de matchar:
        # Is??fall ska de korten stanna ??ppna
            # Om de inte matchar ska b??da korten v??ndas bort men vara kvar.
        # Ge po??ng och forts??tt med samma spelare ELLER
        # ge inga po??ng och g?? ??ver till n??sta spelare


# Funktioner att skapa:
    # Funktion att skriva ut. Dynamisk som kan ta anv??ndar-input. Kan anv??ndas som argument i v??nd_kort-funktionen?
    # En som l??gger ut korten. Samma kort i tv?? listor
        # En lista skrivs aldrig ut, den andra skriver bara ut element som v??nds upp och/eller matchar    
    # Funktion som v??nder upp det valda kortet baserat p?? input??
        # Kan varje ruta ha en siffra? Anv??ndaren inputar siffran
        # Funktionen skriver ut br??det med exakt det itemet visat
        # formaterad lista med dynamiskt input. Anv??nd skriv_ut-funtionen som argument?
    # Funktion som j??mf??r korten och uppdaterar br??det om de st??mmer.
        # Kan man spara korten i en variabel (3e lista?) som j??mf??rs med n??r man ska skriva ut?
        # Eller kan man permanent ??ndra br??det?
        # Ers??tt index[i] med kortet x som just sparades i variabeln?
    # Funtion som tilldelar po??ng och kollar om vi har en vinnare

### KW, ta in positioner som keys och kort som args?