class Car:
    def drive(this):
        print("Більше газу. Менше ям")

bmw = Car()

bmw.drive()

class Animal:
    def speak(this):
        print("Даю голос")

class MiniPig(Animal):
    def speak(this):
        print("Хрю хрю ...")

class Dog(Animal):
    def speak(this):
        print("Гав гав ...")

pig = MiniPig()
pig.speak()

dog = Dog()
dog.speak()

myAnimals = [MiniPig(), Dog()]

for obj in myAnimals:
    obj.speak()

def talk(obj):
    obj.speak()

talk(MiniPig())
talk(Dog())

class Student:

    def __init__(self, name):
        self.name = name
        self._age = 18
        self.__hobby = "Хобіт хорсинг"
    def __str__(self):
        return f"Student name = {self.name} age = {self._age} hobby = {self.__hobby}"
    
    def get_hobby(self):
        return self.__hobby

ivan = Student("Підкаблучник Василь")

print("name = ", ivan.name)
print("age = ", ivan._age)
print("hobby = ", ivan.get_hobby())
print(ivan)