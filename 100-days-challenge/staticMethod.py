#if we use staticmethod then we does not need to pass the self keyword with the method hence we just pass the variable and then we do what we want 
#static method is not a method of a class or not a instance method of class 
class Math:
  def __init__(self,num):
    self.num = num
  def addtonum(self,n):
    self.num=self.num +n
  @staticmethod
  def add(a,b):
    return a+b

a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(4,5))
print(Math.add(3,4))
