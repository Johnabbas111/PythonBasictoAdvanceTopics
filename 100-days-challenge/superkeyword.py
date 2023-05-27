class ParentClass:
  def parent_method(self):
    print("This is the parent method.")

class ChildClass(ParentClass):
  def parent_method(self):
    print("harry")
    super().parent_method()
  def child_method(self):
    print("this is the child method.")

obj=ChildClass()
obj.parent_method()

#super constructor inheritance in programmer class
    
class Employee:
  def __init__(self,name,id):
    self.name=name
    self.id=id

class Programmer(Employee):
  def __init__(self,name,id,lang):
    
    super().__init__(name,id)
    self.lang=lang
  

rohan=Employee("rohan",420)
john=Programmer("harry",2323,"python")
