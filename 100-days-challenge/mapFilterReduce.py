from functools import reduce


def cube(x):
  return x*x*x
print(cube(2))

#this is how we write if we want to make a list of item by make a cube of every list number
#l=[1,3,4,5,6,7]
#newl=[]
#for item in l:
  #newl.append(cube(item))
#print(newl)
#map filter are higher order function because they take an function inside it

#map
l=[1,2,3,4,5,6]
newl=list(map(cube,l))
print(newl)
#filter
#filter take a function inside it which either return true or False
def filter_function(a):
  return a>4
newlist=list(filter(filter_function,l))
print(newlist)
#reduce is also a higher order function but we have to import it first\
#reduce
#it reduce a list to a single object 
number = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,number)
print(sum)