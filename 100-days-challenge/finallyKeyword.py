#in a function if a function return from a point then finally  is executed if a function return
def func1():
  try:
    l=[1,5,6,7];
    i=int(input("Enter the index :"));
    print[l[i]]
    return 1

  except:
    print("i am always executed")
    return 0;

  finally:
    print("Am always executed")
