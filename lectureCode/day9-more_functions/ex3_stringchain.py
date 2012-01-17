mystr = """Hugh Laurie: A good wife, or a good business partner?
Stephen Fry: Is there a difference, Peter?
Hugh Laurie: I hope so, John."""

def actor(s):
    return s.split(":")[0]

def tone(s):
    punct = s[-1]
    if punct == "?":
        return "Question"
    elif punct == ".":
        return "Statement"

print actor(mystr.splitlines()[0])

if tone(mystr.splitlines()[1]) is "Question":
    print actor(mystr.splitlines()[1])