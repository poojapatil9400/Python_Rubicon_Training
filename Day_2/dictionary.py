dict={"name":'John', "age":30, "city":'New York'}
print(dict)
print(dict["name"])  # Accessing value by key
print(dict.get("age"))  # Accessing value using get method  

for key in dict:
    print(key, ":", dict[key])  # Iterating through keys
print("Keys:", dict.keys())  # Getting all keys
print("Values:", dict.values())  # Getting all values   
print("Items:", dict.items())  # Getting all key-value pairs
