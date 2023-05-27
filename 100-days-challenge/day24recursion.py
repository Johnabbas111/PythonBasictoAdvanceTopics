#recursion
#factorial of a number
def funFactorial(n):
  if(n==1 or n==0):
    return 1
  else:
    return n* funFactorial(n-1)

print(funFactorial(5))