import pickle

my_big_data = {'a': [1,2,3], 'c': {1: 'a'}}

f = open('data.pkl', 'w')
pickle.dump(my_big_data, f)
f.close()

#read implied
f = open ('data.pkl')
obj = pickle.load(f)
f.close()
print obj