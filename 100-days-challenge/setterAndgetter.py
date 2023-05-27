#Getter and Setters


class MyClass:
  def __init__(self,value):
    self._value=value
  def show(self):
    print(f" the value is {self._value}")
  #this is what we called Getter 
    
  @Property 
  def ten_value(self):
    return 10*self._value
  #this is a setter now a fun or method behaves as a property which we can set  
  @ten_value.setter  
  def ten_value(self,new_value):
    self_value = new_value/10
   


obj=MyClass(10)
obj.show()
obj.ten_value=66

print(obj.ten_value)
    
