#1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound"


class Dog(Animal):
    def speak(self):
        return "Dog barks"  # [cite: 12]

animal = Animal("Зверь")
dog = Dog("Бобик")
print(animal.speak())
print(dog.speak())


#2
class Flyable:
    def fly(self):
        print("Duck can fly")

class Swimmable:
    def swim(self):
        print("Duck can swim")

class Duck(Flyable, Swimmable): # [cite: 25]
    pass

duck = Duck()
duck.fly()
duck.swim()

#3
class Person: # [cite: 32]
    def __init__(self, name, age): # [cite: 33, 34, 35]
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age) # [cite: 40]
        self.major = major

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")

student = Student("Alice", 20, "Computer Science")
student.display_info()