'''
Abracadabra
'''

from os import name, system
from random import shuffle
from time import sleep

CardNum = {1: " A", 2: " 2", 3: " 3", 4: " 4", 5: " 5", 6: " 6",
           7: " 7", 8: " 8", 9: " 9", 10: "10", 11: " J", 12: " Q", 13: " K"}
Suits = {"Spades": "S", "Clubs": "C", "Diamonds": "D", "Hearts": "H"}


def clear():                    # Clears the screen
    if name == "nt":            # for windows
        _ = system("cls")
    else:                       # for mac/linux
        _ = system("clear")
    print()


def FullDeck():
    Deck52 = []
    for y in Suits.values():
        for x in CardNum.values():
            Deck52.append(x+y)
    return Deck52


def RandomCards(x):
    DeckX = FullDeck()
    shuffle(DeckX)
    RandCards = []
    for d in range(x):
        RandCards.append(DeckX[d])
    return RandCards


def SortColumns(deck, col):
    clear()
    print("   Magic Card Trick\n")
    print("\nShuffling cards...")
    sleep(2)
    col1 = []
    col2 = []
    col3 = []
    NewDeck = []
    for x in range(len(deck)):
        if x == 0 or x % 3 == 0:
            col1.append(deck[x])
    for x in range(len(deck)):
        if x == 1 or (x-1) % 3 == 0:
            col2.append(deck[x])
    for x in range(len(deck)):
        if x == 2 or (x-2) % 3 == 0:
            col3.append(deck[x])
    if col == 1:
        for x in range(len(col2)):
            NewDeck.append(col2[x])
        for x in range(len(col1)):
            NewDeck.append(col1[x])
        for x in range(len(col3)):
            NewDeck.append(col3[x])
    elif col == 2:
        for x in range(len(col1)):
            NewDeck.append(col1[x])
        for x in range(len(col2)):
            NewDeck.append(col2[x])
        for x in range(len(col3)):
            NewDeck.append(col3[x])
    else:
        for x in range(len(col1)):
            NewDeck.append(col1[x])
        for x in range(len(col3)):
            NewDeck.append(col3[x])
        for x in range(len(col2)):
            NewDeck.append(col2[x])
    return NewDeck


def printColumns(cards):
    clear()
    print("   Magic Card Trick\n")
    for x in range(len(cards)):
        if (x+1) % 3 == 0:
            print("{:>6}".format(cards[x]))
        else:
            print("{:>6}".format(cards[x]), end="")
    print(" ____________________")
    print("    1     2     3      <-- Columns")


def ColumnSelect():
    while True:
        try:
            col = int(input("\nSelect the column your card is in: "))
        except ValueError:
            print("Not a valid input. Try again.")
            continue
        if col > 0 and col < 4:
            return col
        else:
            print("Not a valid input. Try again.")
            continue


def main():
    gameOver = False
    while not gameOver:
        Deck1 = RandomCards(21)
        printColumns(Deck1)
        print("\nPick a card... Shhh. don't tell me what it is!")
        col1 = ColumnSelect()
        Deck2 = SortColumns(Deck1, col1)
        printColumns(Deck2)
        print("\nUsing the same card you picked before...")
        col2 = ColumnSelect()
        Deck3 = SortColumns(Deck2, col2)
        printColumns(Deck3)
        print("\nUsing the same card you picked before...")
        col3 = ColumnSelect()
        Deck4 = SortColumns(Deck3, col3)
        PickedCard = Deck4[10]
        shuffle(Deck4)
        printColumns(Deck4)
        print("\nYour card was:", end=" ")
        sleep(2)
        print(PickedCard, "\n")
        sleep(1)
        if input("Play again? (Y/N): ").upper() != "Y":
            gameOver = True


if __name__ == "__main__":
    main()
