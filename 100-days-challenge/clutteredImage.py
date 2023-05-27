
import os
files =os.listdir("pngImages")
i=1
for file in files:
  if file.endswith(".png"):
    print(file)
  
  

os.rename("pngImages/{file}","pngImages/{i}.png")
i=i+1