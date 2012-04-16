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


class Pet(Animal):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class PetDog(Pet, Dog):
    pass

class PetCat(Pet, Cat):
    def get_phrase(self):
        return "..."


class Abra(Animal):
    says = "abra"

    def capture(self):
        print "%s uses teleport" % self.get_name()

class Kadabra(Abra):
    def get_phrase(self):
        return "Kaaadaaabraaaa!"


Animal().speak()
Dog().speak()
Cat().speak()

PetDog("Bandit").speak()
cat = PetCat("Mrs. Pretty")
cat.speak()

Abra().speak()
Abra().capture()

Kadabra().speak()
Kadabra().capture()
