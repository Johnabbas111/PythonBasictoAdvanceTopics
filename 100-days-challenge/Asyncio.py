#Asycn IO in python
import time
import asyncio
async def function1():
  await asyncio.sleep(1)
  print("func1")
  return "harry"

  
async def function2():
  await asyncio.sleep(1)
  print("func2")

async def function3():
  await asyncio.sleep(4)
  print("func3")

async def main():
  #task=asyncio.create_task(function1())
  #await function1()
  #await function2()
  #await function3()
  l=await asyncio.gather(
    function1(),
    function2(),
    function3()
  )
  print(l)



asyncio.run(main())


#import time
#import asyncio
#import request
#
#a#sync def func1():
# #  url = 'https://www.facebook.com/favicon.ico'
# #  r = requests.get(url, allow_redirects=True)
# #  open('facebook.ico', 'wb').write(r.content)
# #  print(func1)
#
#  
#   
#async def func2():
#   url = 'https://www.facebook.com/favicon.ico'
#   r = requests.get(url, allow_redirects=True)
#   open('facebook.ico', 'wb').write(r.content)
#   print(func1)
#
#   
#async def func2():
#   url = 'https://www.facebook.com/favicon.ico'
#   r = requests.get(url, allow_redirects=True)
#   open('facebook.ico', 'wb').write(r.content)
#   print(func1)
#
#a#sync def main():
# # l=await asyncio.gather(
# #   func1(),
# #   func2(),
#    func3()
#
#    
  )
  
asyncio.run(main)