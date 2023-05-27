#tuples are immutable
#enclosed in ()
tup=(1,5,6,7)
print(type(tup))
tupp=(1,)
print(type(tupp))
#if we want tuple of one element we use , with that element
#tuple can have multiple datatypes 
if 5 in tup:
    print("Yes")
else:
  print("Not present")
  