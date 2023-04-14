# Class Person
class Person:
    no_of_people = 0
    
    def __init__(self,name):
        self.name = name
        Person.no_of_people += 1
        
    # class methods
    @classmethod
    def no_of_people(cls):
        return cls.no_of_people