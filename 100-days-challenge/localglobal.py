x=4
print(x)
def hello():
  x=5
  print(f" the local x is {x}")
  print("hello harry")
  
print(f"The global x is {x}")
hello()
print(f"the global x is {x}")