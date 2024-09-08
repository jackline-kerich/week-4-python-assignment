# Define a class named person
class Person:
# This is the constructor method, which is called when we create a new instance of Person
    def __init__(self, name, age, gender):
# Initialize the attributes of the Person class
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I am {self.gender}.")
        
# Create an instance of Person
person_instance = Person(name="Jackie", age=28, gender="Female")

# Call the introduce method
person_instance.introduce()
