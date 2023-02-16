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

# Kan man få likadana kort utspelade två gånger? Hur?
# Skriva ut en suit två gånger?
    # Hur
# Designa en egen lek?
# Skriv ut bräde med X * X antal kort
# Två listor, en öppen och en dold?# Jämför med dem och se om de är samma
# Spelaren vänder upp ett kort, det värdet sparasi x.
# Väljer nästa kort, om det har samma värde som x, avslöja det. Ge poäng.

# Steg 1:
    # Skapa ett bräde och tilldela kort.
    # Se till att korten finns i en öppen och en dold lista för jämförelse.

# Steg 2:
    # Skapa poängsystem föt två spelare
    # Loop där spelare drar ett kort som visas direkt
        # Välja ett till kort att visa. OM de matchar:
        # Isåfall ska de korten stanna öppna
            # Om de inte matchar ska båda korten vändas bort men vara kvar.
        # Ge poäng och fortsätt med samma spelare ELLER
        # ge inga poäng och gå över till nästa spelare


# Funktioner att skapa:
    # Funktion att skriva ut. Dynamisk som kan ta användar-input. Kan användas som argument i vänd_kort-funktionen?
    # En som lägger ut korten. Samma kort i två listor
        # En lista skrivs aldrig ut, den andra skriver bara ut element som vänds upp och/eller matchar    
    # Funktion som vänder upp det valda kortet baserat på input??
        # Kan varje ruta ha en siffra? Användaren inputar siffran
        # Funktionen skriver ut brädet med exakt det itemet visat
        # formaterad lista med dynamiskt input. Använd skriv_ut-funtionen som argument?
    # Funktion som jämför korten och uppdaterar brädet om de stämmer.
        # Kan man spara korten i en variabel (3e lista?) som jämförs med när man ska skriva ut?
        # Eller kan man permanent ändra brädet?
        # Ersätt index[i] med kortet x som just sparades i variabeln?
    # Funtion som tilldelar poäng och kollar om vi har en vinnare

### KW, ta in positioner som keys och kort som args?