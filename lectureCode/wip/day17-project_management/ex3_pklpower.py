import pickle
class Animal(object):
    says = "<undefinable>"

    def get_name(self):
        return self.__class__.__name__

    def get_phrase(self):
        word = self.says.capitalize()
        return "%s, %s!" % (word, word)

    def speak(self):
        print '"%s", says the %s' % (self.get_phrase(), self.get_name())

class Dog(Animal):
    says = "woof"

class Cat(Animal):
    says = "meow"

l = [Cat(), Dog(), Animal()]

f = open('animals.pkl', 'w')
pickle.dump(l, f)
f.close()
f = open ('animals.pkl')
obj = pickle.load(f)
f.close()

print obj
#Don't do this with JSON!