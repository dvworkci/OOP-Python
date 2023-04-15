# Class Person
class Person:
    no_of_people = 0
    
    def __init__(self,name):
        self.name = name
        # Person.no_of_people += 1
        Person.add_person()
        
    # class methods
    @classmethod        # denotes that this is a class method
    def no_of_people_(cls):
        return cls.no_of_people
    
    @classmethod
    def add_person(cls):
        cls.no_of_people += 1