import random
from sympy import nextprime

# solitaire algorithm
# white joker = 53, balck joker = -53 <- csak a megkulomboztetes kedveert

# a.
def white_joker(cards):
    nn = len(cards)
    found_joker = False
    j = 0
    while not found_joker and j < nn-1:
        if cards[j] == 53:
            cards[j], cards[j+1] = cards[j+1], cards[j]
            found_joker = True
        j += 1

    if not found_joker:
        cards.insert(1, 53) # inserting joker to the second place 
        del cards[nn] # removing joker from the end of the card pack

    return j

# b.
def black_joker(cards):
    nn = len(cards)
    found_joker = False
    j = 0
    while not found_joker and j < nn-2:
        if cards[j] == -53:
            cards[j], cards[j+2] = cards[j+2], cards[j]
            found_joker = True
        j += 1

    if not found_joker:
        if cards[j] == -53:
            cards.insert(1, -53)
            del cards[nn]
        else:
            j += 1
            cards.insert(2, -53)
            del cards[nn]

    return j

# c.
def switch(cards, joker1, joker2):
    if joker2 < joker1:
        joker1, joker2 = joker2, joker1

    nn = len(cards)
    new_order = cards[0:joker1] + cards[joker1:(joker2+1)] + cards[(joker2+1):(nn+1)]

    return new_order

# d.
# az utolso kartyalapot megnezzuk, majd elolrol annyit rakunk az utolso kartyalap ele, amennyi az erteke
def last_card(cards):
    nn = len(cards)
    value = abs(cards[nn-1])
    new_cards = cards[value:(nn-1)] + cards[0:value] + cards[(nn-1):nn]

    return new_cards

# e.
def key_member(cards):
    value = abs(cards[0])
    if value == 53:
        return -1
    else:
        return abs(cards[value])

def solitaire(cards, n):
    i = 0
    key = []
    while i < n:
        white_joker_index = white_joker(cards)
        black_joker_index = black_joker(cards)
        cards = switch(cards, white_joker_index, black_joker_index)
        cards = last_card(cards)

        keym = key_member(cards)
        if keym != -1:
            i += 1
            key.append(keym)

    return key

def blum_blum_shub(seed, n):
    p = nextprime(4568456)
    while p%4 != 3:
        p = nextprime(p)

    q = nextprime(4569000)
    while q%4 != 3:
        q = nextprime(q)

    M = p*q
    key = bytearray(b'')
    x = (seed**2)%M
    for i in range(n):
        st = ''
        for j in range(8):
            st += str((x**2)%M%2)
            x = (x**2)%M
        key.append(chr(int(st, 2)).encode())

    return key

def main():
    n = 200
    cards = [42, 46, 26, 28, 38, 16, 19, 20, 9, 53, 37, 33, 35, -53, 1, 7, 13, 41, 34, 32, 11, 48, 40, 29, 25, 50, 45, 5, 44, 49, 36, 8, 43, 51, 2, 14, 18, 27, 12, 21, 17, 23, 4, 30, 24, 6, 39, 52, 47, 22, 10, 15, 3, 31]
    key = solitaire(cards, n)
    print(key)
