f=open('myfile.txt','r')
while True:
  line=f.readline()
  print(line)
  if not line:
    print(line,type(line))
    break

f=open('myfile.txt','w')
lines=['line 1\n','line2\n','line3\n']
f.writelines(lines)
f.close()