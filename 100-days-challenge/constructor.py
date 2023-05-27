#constuctor in python    
class Person:
  #name="harry"
 # occ="Developer"
  def __init__(self,name,occ):
    self.name=  name
    self.occ = occ
    print("hey i am a constructor")
  def info(self):
    print(f"{self.name} is a {self.occ}")   
    
a=Person("harry","developer")
b=Person("Divya","Hr")
print(a.name)
a.info()
b.info()
#a.name="Divya"
#a.occ="HR"
#a.info()