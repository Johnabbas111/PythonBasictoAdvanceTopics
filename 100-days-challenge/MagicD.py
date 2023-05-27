#magic method 
class Employee:
  def __init__(self,name):
    self.name=name
  #name='harry'
  def __len__(self):
    return(self.name)
    i=0
    for c in self.name:
      i=i+1
      return i

  def __str__(self):
    return f"The name of Employee is {self.name}"
  def __repr__(self):
    return f"The name of employee is {self.name} repr"

  def __call__(self):
    print("hey i am good")

e=Employee('harry')
print(e)
e()
#print(e.name)
#print(len(e))
