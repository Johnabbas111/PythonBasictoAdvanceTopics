#regular expressions
import re
pattern =r"[A-Z]yclone"
text='''y of the senses may directly observe patterns. Conversely, abstract Cyclone patterns in science, mathematics, or language may be observable only by analysis. Direct observation in practice means seeing visual patterns, which are widespread in nature and in art. Visual patterns in nature are often chaotic, rarely exactly repeating, and often involve fractals. Natural patterns include spirals, meanders, waves, foams, tilings, cracks, and those Hyclone created Dyclone by symmetries of rotation and reflection. Patterns have an underlying hyclone mathematical structure;[2]: 6  indeed, mathematics can be seen as the search for regularities, and the output of any function is a mathematical pattern. Similarly in the sciences, theories explain and predict regularities in the world.'''
#match =re.search(pattern,text) #only for first occurance]
matches=re.finditer(pattern,text)# for all match values
for match in matches:
  print(match.span())
  print(text[])
#to learn more undarstand meta characters
#learn from regexr.com refernece
