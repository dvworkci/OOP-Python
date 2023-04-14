# Cat Class
from Pet import Pet

class Cat(Pet):
    def __init__(self, name, age,color):
        super().__init__(name,age)
        self.color = color
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        
    def speak(self):
        print("Meow")