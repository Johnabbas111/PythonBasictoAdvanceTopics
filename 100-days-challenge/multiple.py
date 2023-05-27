#multiple inheritance in python
class Employee:
  def __init__(self,name):
    self.name=name

  def show(self):
    print(f"the name of Employee is {self.name}")
    



class Dancer:
  def __init__(self,dance):
    self.dance=dance

  def show(self):
    print(f"the name of Employee is {self.dance}")  


class DancerEmployee(Dancer,Employee):
  def __init__(self,name,dance):
    self.dance=dance
    self.name=name

obj=DancerEmployee("khatak","harry")
print(obj.name)
print(obj.dance)
obj.show()
    

