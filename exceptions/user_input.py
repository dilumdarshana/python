# Get user input until it is a number

def get_user_input():
  while True:
    try:
      age = int(input('Please enter your age '))
    except:
      print('Please enter valid age')
      continue
    else:
      break

  print(f'Your age is {age}')

get_user_input()
