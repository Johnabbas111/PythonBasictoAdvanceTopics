#generator in python 
#it does not store the information but store the information from which we create the data or generate at the same movement when needed
#Example
def my_generator():
  for i in range(50000):
    #complex computation for yield data
    yield i
  
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for j in gen:
  print(j)
#benefits of generator 
#its allows to store information on fly and we does not need to store it like in list tuple and dict
#we save the memory because value created at instance 
