def welcome():
  print("May you are welcome from harry")
  print(__name__)
  if __name__=='__main__':
       welcome()


#we put name==main to ensure that the function or module import to other module but doesnt run it until the name is main 
#when we call it from the other file if we call it it doesnt eun from the main but run from that file