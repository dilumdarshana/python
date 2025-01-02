class Animal():
  color = 'black'

  def __init__(self):
    print('Animal created')

  def set_color(self, color):
    self.color = color

  def get_color(self):
    return self.color

  def who_am_i(self):
    return f'I am an animal and my color is {self.color}'

  def say_hello(self):
    return 'Hello, I am an animal'

# inheritance Dog from Animal
class Dog(Animal):
  def __init__(self):
    super().__init__() # or Animal.__init__(self)
    print('Dog created')

  def bark(self):
    return 'Woof!'

  def who_am_i(self):
    return super().who_am_i() +' and I am a dog'

  # overwrite parent class method
  def say_hello(self):
    return 'Holla, I am a dog'

# create object of Dog class
my_dog = Dog()

# set color
# set color comming from parent class
my_dog.set_color('brown')

print(my_dog.who_am_i()) # output: I am an animal and my color is brown and I am a dog

# overwrite parent class method
print(my_dog.say_hello()) # output: Holla, I am a dog
