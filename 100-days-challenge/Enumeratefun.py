
marks=[12,50,32,98,45,1,4]
#index=0
#for mark in marks:
#  print(mark)
#  if(index==3):
#    print('harry awesome')
#  index+=1
#the enumerate function gives index and value if an element in array ,list at the same time
#by default index start from 0 in enumerate function also
for index ,mark in enumerate(marks):
  print(mark)
  if(index==3):
    print("John awesome")