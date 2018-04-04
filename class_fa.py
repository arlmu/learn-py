class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly")

def run_twice(animal):
    animal.run()
    animal.run()



run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

a = Animal()
b = Dog()
c = Cat()
d = Animal()
print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?',isinstance(d, Animal))
print('d is dog?', isinstance(d, Dog))
print('d is cat?', isinstance(d, Cat))
#dog = Dog()
#dog.run()

#cat = Cat()
#cat.run()

