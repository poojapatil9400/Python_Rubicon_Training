#search perticular element in a list
list1 = ["demo", "test", "example", 1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = [5.6,3,9,3.6,0,]
print("type of list1 is", type(list1))

print("select value from list to check if it is present or not",list1)

str3 = input("Enter a value to check in list: ")

if str3.isdigit():
    str3 = int(str3)
if str3 in list1:
    print( " value is present in the list")
else:
    print( " value is not present in the list")
#operations on list
list1.append("new_value")  # Adding a new value
print("Updated list:", list1)

list1.remove(1)  # Removing a value
print("List after removing 1:", list1)

list1.append("Pooja")  # Adding multiple values
print("List after adding multiple values:", list1)

#list1.sort()    it generte the error 
list3.sort()  
#print("Sorted list:", list1)    
print("Sorted list3:", list3)

list2.remove(2)
list2.clear()  # Clearing the list
print("List after clearing:", list2)

print(list1.index("demo")) # Finding the index of an element
list1.insert(0, "first")  # Inserting a value at a specific index
print("List after inserting a value:", list1)


