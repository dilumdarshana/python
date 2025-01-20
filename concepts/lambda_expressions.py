"""
Anonymous function which can be used one time 
"""

# assume we have this
def square(num):
  return num ** 2

# we can write this using lambda expressions
square = lambda num: num ** 2
print(square(3))


# example of using lambda with map function
nums = [1,2,3,4,5]
square_nums = list(map(lambda num: num ** 2, nums))
print(square_nums)

# example 03
cal = lambda num: 'Even' if num%2 == 0 else 'Odd'
print(cal(2))
