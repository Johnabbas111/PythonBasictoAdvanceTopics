questions=[
  [
    "which language is used to create fb?","Python","Frech","javascript","php","None"
  ],
  
  [
    "which language is used to create fb?","Python","Frech","javascript","php","None"
  ],
   [
    "which language is used to create fb?","Python","Frech","javascript","php","None"
  ],
  [
    "which language is used to create fb?","Python","Frech","javascript","php","None"
  ],
  [
    "which language is used to create fb?","Python","Frech","javascript","php","None"
  ],
  [
    "which language is used to create fb?","Python","Frech","javascript","php","None"
  ],
  [
    "which language is used to create fb?","Python","Frech","javascript","php","None"
  ],
  
  
]
levels=[1000,2000,3000,5000,20000,40000,8000,160000,320000,500000,600000,1200000]
i=0
money=0
for i in range(0,len(questions)):
  question=questions[i]
  print(f"questions for rupees.{levels[i]}");
  print(f"a.{question[1]}         b.{question[2]}")
  print(f"c.{question[4]}         d.{question[4]}")
  reply=int(input("Enter your answer 1-4"))
  if(reply==question[-1]):
    print(f"You won Rupees={levels[i]}")
  elif(i==4) :
    money=10000
    
  elif(i==9):
    money=10000000
  else:
    print("wrong answer")
    break

print(f'your take money is {money}')