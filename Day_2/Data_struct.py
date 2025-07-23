list = ["demo", "test", "example",1, 2, 3, 4, 5]
print(type(list))
print(len(list))

# tuple is immutable 
tuple = ("demo", "test", "example", 1, 2, 3, 4,2, 5)
print(type(tuple))
print(len(tuple))

dict = {"name": "demo", "age": 25, "city": "test"}
print(type(dict))
print(len(dict))


#duplicate values not allowed in set and in {} and unorderd
set = {3,34,87,4}
print(type(set))
print(len(set))

#String
str = "I Love Python Programming"
print(str[2:6]) #start indext,last index-1
print(str[3])
print(str[-1])

str = "easy software"
print(str.capitalize())#convert first word of string to capital
print(str.casefold()) #covert to small
print(str.center(60))
print(str.endswith("software"))#true
print(str.endswith("Software"))#false
print(str.index("software"))

str1="easy124"
str2='easy@557'
str5="easy"
print(str1.isalnum())#true return true if string contains alphabets and numbers
print(str2.isalnum())#false


str3 = "345"
print(str2.isdigit())
print(str3.isdigit())

print(str2.isdecimal())
print(str3.isdecimal())


print(str5.isalpha())
print(str2.isalpha())

print(str2.isidentifier())

str8=" "
str9="Pooja"
print(str8.isspace())
print(str9.isspace())

a = "Easy"
b = "pyTHon"
print(a.swapcase())
print(b.swapcase())

c = ' python '
print(c,"programming")
print(str.strip(),"Programming")#remove space of string 
print(str.lstrip(),"Programming")
print(str.rstrip(),"Programming")

u ="I love Java"
print("original string",u)
print(u.replace("Java" ,"Python"))


print(u)
mylist=u.split()
print(mylist)

#SET 
set = {"demo", "test", "example", 1, 2, 3, 4, 5}
print(type(set))
set.add("new_item")
print(set)

set.remove(1)  # removes the first occurrence of 1
print(set)




