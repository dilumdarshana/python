"""
Magic/Dunder methods
"""
class Book():
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  
  # magic methods
  def __str__(self):
    return f'{self.title} by {self.author}, {self.pages} pages'

  def __len__(self):
    return self.pages

  def __del__(self):
    print(f'Book {self.title} deleted')

# instance of class Book
mybook = Book('Python', 'Dilum', 300)

# this will call __str__ behind the scenes
print(mybook)

print(len(mybook))

del mybook