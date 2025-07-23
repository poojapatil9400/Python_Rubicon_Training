 #tuple is immutable 
tuple = ("demo", "test", "example", 1, 2, 3, 4, 2, 5)
fruits = ("apple", "banana", "cherry")
print(type(fruits))

for i in fruits:
    print("I like ",i)
list_from_tuple = list(fruits)
list_from_tuple.append( "orange")  # Adding an element to the list
print(list_from_tuple)  # Displaying the updated list

print(fruits[1])  # Accessing an element by index
del tuple  # Deleting the tuple
print("Tuple deleted")
    


#search particular element in a tuple
print("select value from tuple to check if it is present or not", tuple)    
str2 = input("Enter a value to check in tuple: ")
if str2.isdigit():
    str2 = int(str2)
if str2 in tuple:
    print(" value is present in the tuple")
else:
    print(" value is not present in the tuple")

#operations on tuple
tuple1 = tuple + ("new_value",)  # Adding a new value (note the comma to make it a tuple)
print("Updated tuple:", tuple1)

print(len(tuple1))  # Length of the tuple
print(tuple1[0])  # Accessing the first element 

tuple2 = tuple1[:5]  # Slicing the tuple
print("Sliced tuple:", tuple2)

tuple3 = tuple1 * 2  # Repeating the tuple
print("Repeated tuple:", tuple3)
print("Index of 'demo' in tuple:", tuple.index("demo"))  # Finding the index of an element
tuple4 = tuple1.count(2)  # Counting occurrences of an element
print("Count of 2 in tuple:", tuple4)
print("  ")
#convert tuple to list
list_from_tuple = list(tuple1)