def greeter(name):
    name = str(name)
    print "hello,", name.lower()

def box(w,h):
    if type(w) != int or type(h) != int or w <= 0 or h<=0:
        print "Error: Invalid Dimensions"
        return

    # start values
    if w > 1:
        cap = "+" + "-" * (w-2) + "+"
        row = "|" + " " * (w-2) + "|"
    else:
        cap = "+"
        row = "|"

    print cap 
    for i in range(h-2):
        print row
    
    if h >= 2:
        print cap


def tree(rows=5, ntrunk=2, ornament="-", leaf="^", star="*"):
    result = ""
    if star:
        result += " " * (rows-1) + star + "\n"

    if not leaf:
        leaf = " "
    if not ornament:
        ornament = " "

    chunk = leaf + ornament
    for i in range(rows):
        result += (" " * (rows-1-i)) + (chunk * i) + leaf + "\n"

    if rows > 3:
        trunk = " "*(rows-2) + "| |"
    else:
        trunk = " "*(rows-1) + "|"

    for i in range(ntrunk):
        result += trunk + "\n"

    return result[:-1]

