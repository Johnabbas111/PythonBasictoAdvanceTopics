class Employee:
  def __init__(self,name,id):
    self.name = name;
    self.id = id;
  def showDetails(self):
    print(f"The name of employee:{self.id} is {self.name}" )
          
  
class Programmer(Employee):
  def showLanguage(self):
    print(f"The Default language is python")
    
e =Employee("harry",12)
e.showDetails()
e1=Employee("John",14)
e1.showDetails()
e2 = Programmer("shah " ,13)
e2.showDetails()
e2.showLanguage()