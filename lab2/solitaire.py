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

def solitaire(cards, n):
    i = 0
    while i < n:
        white_joker_index = white_joker(cards)
        black_joker_index = black_joker(cards)
        cards = switch(cards, white_joker_index, black_joker_index)

        i += 1

