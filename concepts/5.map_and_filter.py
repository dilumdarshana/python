##### map
def square(num):
  return num ** 2

nums = [1,2,3,4,5];

# apply square function for each element
square_nums = list(map(square, nums))
print(square_nums)

# just print out
for i in map(square, nums):
  print(i)

##### filter
def check_even(num):
  return num%2 == 0

even_nums = list(filter(check_even, nums))
print(even_nums)