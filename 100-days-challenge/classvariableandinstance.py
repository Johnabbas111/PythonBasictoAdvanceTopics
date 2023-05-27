#instance variable and class variable in python
#we can cahnge the instance variable as we can access them and change them for an object of a class
#they may and may not be differnet for every object of a class
#class variable are the variable that are same for every object of a class 
#if there is not an instance variable then it look for class vaariable only
#and class variable value is given to the obj of class


class Employee:
  companyName="apple"
  def __init__(self,name):
    self.name = name
    self.raise_amount=0.02

  def showDetails(self):
    print(f"The name of the Employee is {self.name} and  {self.raise_amount} and comapny name is {self.companyName}")

#now understand what is self in the class
#lets explore it
emp1 = Employee("Harry")
emp1.name="john"

emp1.raise_amount=12
emp1.companyName="Apple India"
emp2 = Employee("Rohan")
emp1.showDetails()
emp2.showDetails()

    

#emp1.showDetails()
#Employee.showDetails(emp1)