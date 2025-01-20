# example 01: loop list elements
nums = [1,2,3,4,5]

for num in nums:
  print(num)

# example 02: loop with steps
for i in range(0, len(nums)):
  print(i)

# example 03: loop with string
for char in "Hello, World!":
  print(char)

# example 04: loop disctionary
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

for item in person:
  print(item) # this will print only the keys

for key, val in person.items():
  print(key, val) # this will print both key and value

for val in person.values():
  print(val) # this will print only the values

# example 05: loop with tuple
coordinates = (40.7128, -74.0060)

for coord in coordinates:
  print(coord)

# example 06: loop with set
my_set = { 1,2,3,4,5 }

for num in my_set:
  print(num)

# example 07: nested loop
for i in range(5):
  for j in range(5):
    print(i, j)

# example 08: loop with by convert to tuple
for item in enumerate('item'):
  print(item)
# output:
# (0, 'i')
# (1, 't')
# (2, 'e')
# (3, 'm')
# (4, 's')

# example 08: break statement
for num in nums:
  if num == 3:
    break # exit the loop from here
  print(num)

# example 09: continue statement
for num in nums:
  if num == 3:
    continue # from this point code will pointing to the top, doesn't execute bellow anything
  print(num)

# example 10: while loop
i = 0
while i < 5:
  print(i)
  i += 1

# example 11: infinite loop
# while True:
#   print("Hello, World!")
