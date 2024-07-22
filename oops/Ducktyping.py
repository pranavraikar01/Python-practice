# "Duck typing" = Concept where the class of an object is less important than the methods/attributes .It is Another way to achieve polymorphism besides Inheritance
#                            Object must have the minimum necessary attributes/methods
#                            "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog():
    def speak(self):
        print("WOOF!")

class Cat():
    def speak(self):
        print("MEOW!")

# class Car:
#     alive = True

#     def speak(self):
#         print("HONK!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)


class Person:
    alive = True

    def catch(self,animal):
        animal.speak()
        print("Animal caught")
dog=Dog()
cat=Cat()
person=Person()
person.catch(dog)
person.catch(cat)
print(person.alive)



