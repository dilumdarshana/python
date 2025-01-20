# Read file with exception

try:
  with open('./testfile.txt', 'w') as f:
    f.write('Another new line')
except FileNotFoundError:
  print('File not found')
except IOError:
  print('An error occurred while reading the file')
except:
  print('An uknown error occurred while reading the file')
finally:
  print('File closed')
