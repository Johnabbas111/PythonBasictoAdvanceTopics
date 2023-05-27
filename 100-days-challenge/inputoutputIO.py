f=open("myfile.txt",'r')
text=f.read()
print(text)
f.close()
#we can also open file in write mode by 'w'
#we can also open it in append mode 'a'
#we can also do it like that in that case we are free to not write the f.close() statement
with open("myfile.txt",'w'):
  f.write("hey i am inside again")
