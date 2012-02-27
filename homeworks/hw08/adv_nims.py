#!/usr/bin/env python

###################### 
#  Helper Functions
######################
def splitparts(s):
    "split_ints takes a string and returns all chunks.  Chunks are any space separated or comma separated values"

    if s.find(',') != -1:
        result = [ a.strip() for a in s.split(',') ]
    else:
        result = [ a.strip() for a in s.split(' ') ]
    return [ a for a in result if a ]
    
def a2idx(c):
    "converts a letter to it's index value"
    return ord(c.upper()) - 65

def idx2a(i):
    "converts an index to it's letter value"
    return chr(i+65)


def parse_stones(s):
    stones = [ int(i) for i in splitparts(s) ]
    stones = [ min(i, 99) for i in stones if i > 0 ]
    return stones


def parse_move(s):
    move = splitparts(s)
    
    if len(move) != 2:
        return None

    pile = a2idx(move[0])
    if pile < 0 or pile > 25:
        return None

    num = move[1]
    if not num.isdigit():
        return None

    return pile, int(num)


def valid_move(inp, piles):
    if inp is None:
        return False

    pile, amt = inp
    if pile > len(piles):
        return False
    
    if amt > 0 and amt <= piles[pile]:
        return True


def move(inp, piles):
    i, amt = inp
    piles[i] -= amt

###################### 
#  Output Functions
######################
def header(piles):
    header = " "
    header += "  ".join(idx2a(i) for i in range(len(piles)))
    header += " | Move"
    return header

def separater(piles):
    "creates a separater under the header, long enough to cover all the piles"
    total = 21 + len(piles)
    total += (len(piles) - 1) * 2
    return "-" * total

def prompt(piles, player):
    output = " ".join("%2d" % i for i in piles)
    output += " | Player %d:  " % (player + 1)
    return output

#########
#  MAIN
#########
def main():
    piles = parse_stones(raw_input("Number of stones in each pile:  "))
    print ""

    print header(piles)
    print separater(piles)

    # init 
    player = 0      # player will be 0 or 1

    # loop as long as any value in piles != 0
    while any(piles): 
        inp = parse_move( raw_input(prompt(piles, player)) )

        # check for valid input
        if not valid_move(inp, piles):
            print "*Error*  Invalid Move"
            continue

        move(inp, piles)
        player = (player + 1) % 2

    # declare winner
    print "Player %d wins!!!" % (player + 1)

if __name__ == "__main__":
    main()
