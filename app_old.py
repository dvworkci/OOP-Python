# Object Oriented Programming in Python
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def add_one(self,num):
        return num + 1
    
    def bark(self):
        print("Bhow")

dog1 = Dog("Tommy",7)
dog1.set_name("Tylon")
dog1.set_age(6)
print(dog1.get_name())
print(dog1.get_age())

# dog2 = Dog("Rambo",5)
# print(dog2.get_name())
# print(dog2.get_age())

# d.bark()
# print(d.add_one(10))
# print(type(d))