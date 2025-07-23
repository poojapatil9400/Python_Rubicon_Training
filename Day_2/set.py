#search particular element in a set

set1 = {"demo", "test", "example", 1, 2, 3, 4, 5}
print("select value from set to check if it is present or not",set)
str2 = input("Enter a value to check in set: ")
if str2.isdigit():
    str3 = int(str2)
if str2 in set:
    print( " value is present in the set")
else:   
    print( " value is not present in the set")
 
#operations on set
set1.add("new_value")  # Adding a new value  
print("Updated set:", set)
set1.remove(1)  # Removing a value
print("Set after removing 1:", set)
set1.add("Pooja")  # Adding multiple values
print("Set after adding multiple values:", set)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)  # Combining two sets
print("Union of set1 and set2:", set3)

set = {"demo", "test", "example", 1, 2, 3, 4, 5}
print(type(set))
set.add("new_item")
print(set)

set.remove(1)  # removes the first occurrence of 1

set.update([6, 7, 8])  # adds multiple elements
print(set)

set.discard(2)  # removes 2 if it exists, does nothing if it doesn't
print(set)
set1 = {1, 2, 3}
set2 = {3, 4, 5}        

set3 = set1.union(set2)  # combines two sets
print(set3)

del set3  # deletes the set
print("Set3 deleted")

print(len(set))
print(set.pop())  # removes and returns an arbitrary element from the set
set.clear()  # removes all elements from the set    
print(set)

num = 5
if num in set:
    print(num, "is present in the set")
else:
    print(num, "is not present in the set")
