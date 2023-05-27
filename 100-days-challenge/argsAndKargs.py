#args and Kwargs
#its not matter to use args and kwargs but the use of * and ** is must
#we can also write its as *ab and **jndak
def function1(*args):
    print(type(args))
    if(len(args)==3):
        print(f"name is{args[0]}and the age is{args[1]}and the rollno is{args[2]}")
    else:
        print(f"the name of the studnet is {args[0]},and age is{args[1]}" )


#function1("harry",22,423)
#l1=["gajhcda",23]
#function1(*l1)
def printMarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
    pass
marks={"harry":100,"john":120,"aryan":30,"rahul":2}
printMarks(**marks)

