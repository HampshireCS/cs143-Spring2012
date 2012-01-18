import json
#big difference so far!
my_big_data = {'a': [1,2,3], 'c': {1: 'a'}}

f = open('data.json', 'w')
json.dump(my_big_data, f)
f.close()

#read implied
f = open ('data.json')
obj = json.load(f)
f.close()
print obj