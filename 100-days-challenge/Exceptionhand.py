#Exceptional handling in python
a = input("Enter the number:")
print(f"Multiplication Table of {a} is:")
try:
for i in range(1, 11):
  print(f"int{a} X{i} ={int(a)*i}")
except Exception as e:
   print(e)

print("some imp lines of code")
print("End of program")
