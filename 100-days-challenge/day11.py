#strings are immutable
#strings are not changeable hence when strings methods apply it return new string but not the previous one
a="Harry"
b="Harry!!!!!!!!!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(b.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))
blogHeading="introduction to jS"

print(blogHeading.capitalize())
str1="Welcome to the Console!!!"
print(len(str1))

print(len(str1.center(50)))
print(a.count("harry"))
print(str1.endswith("!!!"))
print(a.find("y"))
print(a.index('r'))
print(str1.isalnum())
str2="we wish you a Marry Chrismas\n"


print(str2.isprintable())
