class Dog():
  # class object attributes
  species = 'mammal'

  # constructor
  # self is mandatory here
  def __init__(self, name, age=20):
    # by convention, name should be used in all 3 places
    self.name = name
    self.age = age
    self.is_mammal = Dog.species == 'mammal' # class object attributes can call by class name

  # instance method
  def bark(self): # passing a self is mandatory
    return f"Woof!. My name is {self.name}"

# instance of class
# can pass the variables in arbitrary order. But, should use the argument names
# if don't pass the name of the argument, then should use the order of the arguments
# defined in the constructor
dog = Dog(age=23, name='Blackie')

# print object attributes
print(dog.name)  # Output: Blackie
print(dog.species)  # Output: mammal

# call method
print(dog.bark()) # Output: Woof!. My name is Blackie
