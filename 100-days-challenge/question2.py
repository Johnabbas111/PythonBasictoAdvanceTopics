#encode and decode of a sentance in the giving sentence this is aprogram of send word which we want to decodeor encode
st=input("Enter message")
words=st.split(" ")
coding=input("1 for coding and 0 for decoding")
coding==True if coding=="1"else False

if(coding):
  nwords=[]
  for word in words:
    if(len(word>=3)):
      r1="dsf"
      r2="jkr"
      stnew=r1+word[1:]+word[0]+r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
      
  print("".join(nwords)) 
    
else:
  nwords=[]
  for word in words:
    if(len(word>=3)):
      stnew=word[3:-3]
      stnew=stnew[-1]+stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))    