#library management system in python
#the adding book in the library
class Library:
  def __init__(self):
    self.noBooks=0
    self.books=[]
  def addBook(self,book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"the library has {self.noBooks} books and books are ")
    for book in self.books:
      print(book)
      
l1=Library()
l1.addBook("harry Poter")
l1.addBook("john carter")
l1.showInfo()