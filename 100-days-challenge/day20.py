#tuple method in python
#we can not directly change the tuple but on changing tuple to list then append we can change tuple
#countries is an tuple
#temp=list(countries)
#countries=tuple(temp)
tuple1=(0,3,4,6,2,3,5)
res=tuple1.count(3)
print('count of 3 in tuple1 is',res)
res=tuple1.index(3)
print('the index  of 3 is',res)
# occurance of element in between the   some indx
res=tuple1.index(3,4,6)

print("the index of 3 in between is",res)
res=len(tuple1)
print(res)