#find min  and max ele in list 
list1 = [12,34,67,56,65]
print(min(list1))  # Output: 12
print (max(list1))  # Output: 67

#common element in two sets 
set1 = {3,4,2,5,6}
set2 = {1,2,3,4,5}
common_elements = set1.intersection(set2)  # Finding common elements
print("Common elements:", common_elements)  # Output: {2, 3, 4, 5}

#unique elements in two sets
unique_elements = set1.symmetric_difference(set2)  # Finding unique elements
print("Unique elements:", unique_elements)  # Output: {1, 6}
print("Length of set1:", len(set1))  # Output: 5    

#max element in max element in tuple
tuple1 = (10, 20, 30, 40, 50)
max_element = max(tuple1)  # Finding maximum element
print("Max element in tuple:", max_element)  # Output: 50

#merege two dictionaries
dict1 = {"name": "Pooja", "age": 25}    
dict2 = {"city": "Pune", "country": "India"}
merged_dict = {**dict1, **dict2}  # Merging two dictionaries
print("Merged Dictionary:", merged_dict) 


#maxiumum value in dictionary
dict3 = {"a": 10, "b": 20, "c": 30}
max_value = max(dict3.values())  # Finding maximum value in dictionary
print("Maximum value in dictionary:", max_value)  # Output: 30
