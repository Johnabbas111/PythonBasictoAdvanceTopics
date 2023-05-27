#a function without name in python is called lamda function means its an anonimous function
#Syntax
#we can also pass a function inside a function 
#basically when we pass a function we pass a function by creating through lambda 
#to reeduce our line of syntax
double = lambda x: x*2
print(double(5))
average= lambda x,y :(x+y)/2
print(average(3,3))
def appl(fx,value):
  return 6+fx(value)


print(appl(double,4))
