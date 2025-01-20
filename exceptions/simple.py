# declare function
def add(num1, num2):
  return num1 + num2

try:
  add(1, '2')
except TypeError as e:
  print(f"An error occurred: {e}")
except:
  print("An unexpected error occurred")
finally:
  print("This code block always executes")
