john=True
print(john:=False)
#without walrus operator
foods=list()
food=input("What food do you like")
while(True):
  if(food=='quit'):
    break;

  foods.append(food)

#with the use of walrus operator
foods=list()
while(food:=input("what food do you like"))!='quit':
  foods.append(food)