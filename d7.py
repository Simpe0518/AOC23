from collections import Counter
file = open("d7.txt", "r")
file = [line for line in file]

rank = 0
tot = 0
ranked = []
#print(Counter(list(ranked[0])))

card_values = {"2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "T": 10,
               "J": 11,
               "Q": 12,
               "K": 13,
               "A": 14}

def is_higher(hand1, hand2):
    return False

def rank_hand(hand, deck, pos):
    if len(deck) == 0:
        return pos
    if is_higher(hand, deck[len(deck)//2]):
        pos += len(deck)//2+1
        if len(deck) == 1:
            return pos
        return rank_hand(hand, deck[len(deck)//2:], pos )   #higher half of deck
    else:
        pos -= len(deck)//2
        if len(deck) == 1:
            return pos
        return rank_hand(hand, deck[:len(deck)//2], pos)     #lower half of deck
    
for line in file:
    line = line.split()
    ranked.insert(rank_hand(line[0], ranked, len(ranked)//2), line)

