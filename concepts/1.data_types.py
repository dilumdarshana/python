# simple variable
age = 23
name = "Apache"

# list
numbers = [1, 2, 3, 4, 5]

# dictionary
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# tuple
coordinates = (40.7128, -74.0060)

# tuple inside a list
my_list = [(1,2), (3,4), (5,6), (7,8), (9,10)]

# tuple unpacking
x, y = my_list[0]
print(x, y)  # output: (1, 2)

for (x, y) in my_list:
  print(x, y)  # output: 1 2 3 4 5 6 7 8 9 10

# boolean
is_true = True
is_false = False

# complex number
complex_number = 1 + 2j

# string
message = "Hello, World!"

# None
nothing = None

# type checking
print(type(age))  # output: <class 'int'>
print(type(name))  # output: <class 'str'>
print(type(numbers))  # output: <class 'list'>
print(type(person))  # output: <class 'dict'>
print(type(coordinates))  # output: <class 'tuple'>
print(type(is_true))  # output: <class 'bool'>
