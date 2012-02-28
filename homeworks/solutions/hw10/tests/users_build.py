#!/usr/bin/env python

import pickle

f = open("users.pkl", "rb")
users = pickle.load(f)
f.close()

def followers(users, *names):
    if len(names) == 0:
        return []

    elif len(names) == 1:
        name = names[0]
        return [ n for n in users.keys() if name in users[n]["follows"] ]

    else:
        ll = []
        for name in names:
            ll += followers(users, name)
        
        return set(ll)



followers(users, "Theo")
followers(users, "Zeek")
followers(users, "Zeek","Jansen")


def underage_follows(users):
    underage = [ name for name, data in users.items() if data["age"] <= 12 ]
    follows = []
    for name in underage:
        follows += users[name]["follows"]

    follows = set(follows)
    return follows.difference( set(underage) )


def foaf(user, name):
    follows = []
    for name in followers(users, name):
        follows += users[name]["follows"]
    follows = set(follows)
    follows.remove(name)
    return follows


def age_demographics(users):
    ages = {}
    
    for name, data in users.items():
        age = data["age"]
        if age not in ages:
            ages[age] = []
        ages[age].append(name)

    for age, names in ages.items():
        flwrs = followers(users, *names)
        flwrs_age = [ users[name]["age"] for name in flwrs ]
        ages[age] = sum(flwrs_age) / float(len(flwrs))

    return ages

# from random import randint, shuffle
# 
# names = [
#     "Alice",
#     "Bob",
#     "Carol",
#     "Damien",
#     "Everett",
#     "Frank",
#     "George",
#     "Igor",
#     "Jansen",
#     "Karl",
#     "Lola",
#     "Max",
#     "Ned",
#     "Opie",
#     "Paul",
#     "Ralph",
#     "Sally",
#     "Theo",
#     "Uma",
#     "Vera",
#     "Wally",
#     "Xander",
#     "Yolanda",
#     "Zeek"
# ]    
# 
# shuffle(names)
# 
# ages = [ randint(13, 33) for _ in names ]
# ages[:5] = [ randint(8,12) for _ in range(5) ]
# 
# print ages
# 
# people = {}
# for name, age in zip(names, ages):
#     people[name] = {"age": age}
# 
# for i, name in enumerate(names):
#     count = randint(2, 7)
#     
#     idxs = range(len(names))
#     idxs.remove(i)
#     shuffle(idxs)
# 
#     people[name]["follows"] = [ names[j] for j in idxs[:count] ]
#     print people[name]
# 
# f = open("users.pkl", "w")
# pickle.dump(people, f)
# f.close()
