#list is a collection of data 
#lists are mutable
#enclosed in []
#list can be of different datatypes
l=[2,4,5,6,7]
print(l)
print(type(l))

print(l[0])
print(l[1])
print(l[-2])
print(l[len(l)-2])
if 7 in l:
  print("yes")
else:
  print("No")
for number in l:
  print(number)
print(l[1:])  
#list comprehension
lst=[i*i for i in range(4)]
print(lst)
#lsit comprehension with conditions
list=[i*i for i in range(10) if i%2==0]
print(list)