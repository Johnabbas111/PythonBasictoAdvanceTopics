import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
if(hour>0 and hour<12):
  print("good morning sir")
elif(hour>12 and hour<17):
  print('Good afternoon sir')
if(hour>17 and hour<0):
  print('Good night sir')

