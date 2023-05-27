#inheritance single inheritance
#single inheritance
class Animal:
  def __init__(self,name,species):
    self.name=name
    self.species=species

  def make_sound(self):
    print("sound made by the animal")


class Dog(Animal):
  def __init__(self,name,breed):
    Animal.__init__(self,name,species="Dog")
    self.breed=breed
  def make_sound(self):
     print("bark!")


d=Dog("Dog","Doggerman")

d.make_sound()
a=Animal("Dog","dog")
a.make_sound()
#THE DOG class inherited from animal which have its own constructor and we also do an method overloading in child class thats call single inheritance
    
    

