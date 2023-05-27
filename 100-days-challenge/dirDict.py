#in python there are three build in function dict dir and help
x=[1,3,4,5,6]
print(dir(x))
print(x.__add__)
#dict method
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    self.version=version=1
p=Person("john",30)
print(p.__dict__)
print(help(Person))