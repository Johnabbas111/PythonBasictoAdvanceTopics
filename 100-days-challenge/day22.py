letter = "hey my name is {1} and i am from{0}"

country = "india"
name = "harry"
print(letter.format(country, name))
#the above method we use before the introduce of the f string
#know we use  f string 
print(f"hey my name is {name} and i belong to {country}")
txt="FOR ONLY {price:.2f} dollers!"
print(txt.format(price=49.09999))
#with f string
price=49.09999
txt=f"for only price{price:.2f} dollers"
print(txt)
