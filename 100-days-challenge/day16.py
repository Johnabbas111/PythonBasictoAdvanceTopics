#when we use *before passing an aruments in the function python takes it as a tuple or say somekind of list
def printn(*number):
  print(type(number))
  sum=1
  for i in number:
     sum+=sum*i
   
  print(sum)
printn(2,3,4,5,6,7)    

#to take an argument in the function as an dict we use ** before formal parameter
def name(**name):
  #print(type(name))
  print("hello",name["fname"],name["mname"],name["lname"])
  
name(mname="abbas" ,lname="zaidi",fname="john")
