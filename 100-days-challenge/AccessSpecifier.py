#public private protected in python
#All the variable and method in pyhon is by Default public we can access them outside the class and inside other class 
class Employee:
  def __init__(self):
    self.name = "Harry"

a = Employee()
print(a.name)
#private 
class Employee2:
  def __init__(self):
    self.__name = "john"


    
a1 = Employee2()
#cannot be access directly 
#print(a.__name)
#can be access indirectly this is called name mangling in python 
print(a1._Employee2__name)
print(a1.__dir__())

