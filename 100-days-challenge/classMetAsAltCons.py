
class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  
  @classmethod
  #class method as alternate constructor to construct instance of a class from different format
  def fromstr(cls,string):
      name,salary =string.split(",")
      return cls(name,int(salary))
    
    
e=Employee("harry",12000) 
print(e.name)
print(e.salary)

e2=Employee.fromstr("john doe,30")

print(e2.name)
print(e2.salary)