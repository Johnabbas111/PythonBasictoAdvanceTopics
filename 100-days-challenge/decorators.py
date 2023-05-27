#Decorators in python let analyse it
def hello():
  print("Hello world")
hello()  

def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args,**kwargs)
    print("thanks for using this function")
  return mfx
    
#@greet
def add(a,b):
  
  print(a+b)
  
greet(hello())
greet(add)(1,2)
  

