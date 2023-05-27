class Employee:
  company="apple"
  def show(self):
    print(f"the name is {self.name} and comapny is {self.comapny}")
  #if we use classmethod then instead of class instance class is avialable and we can change the class variable with the function .....
  @classmethod  
  def changeComany(cls,newCompany):
    cls.company=newCompany


e1=Employee() 
e1.name="harry"
e1.show()
e1.changeComany("Tesla")
e1.show()
print(Employee.company)
    