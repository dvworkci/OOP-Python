# Pet Class
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        
    def speak(self):
        print("I Don't know what to say")