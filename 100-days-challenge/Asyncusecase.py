import time
import asyncio
import request

 async def func1():
   url = 'https://www.facebook.com/favicon.ico'
   r = requests.get(url, allow_redirects=True)
   open('facebook.ico', 'wb').write(r.content)
   print(func1)

   
async def func2():
   url = 'https://www.facebook.com/favicon.ico'
   r = requests.get(url, allow_redirects=True)
   open('facebook.ico', 'wb').write(r.content)
   print(func1)

   
async def func2():
   url = 'https://www.facebook.com/favicon.ico'
   r = requests.get(url, allow_redirects=True)
   open('facebook.ico', 'wb').write(r.content)
   print(func1)

async def main():
  l=await asyncio.gather(
    func1(),
    func2(),
    func3()

    
  )
