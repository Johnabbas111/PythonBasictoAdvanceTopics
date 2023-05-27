#program to print fibnocci series
def funFibnocci(n):
  if(n==0):
    return 0
  if(n==1):
    return 1
  else:
    return funFibnocci(n-1)+funFibnocci(n-2)
    
for i in range(7):
  print(funFibnocci(i))