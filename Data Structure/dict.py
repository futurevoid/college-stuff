# Create an empty dictionary
my_dict = {}

# Append items to the dictionary
my_dict["apple"] = 5
my_dict["banana"] = 2
my_dict["orange"] = 8
my_dict["grape"] = 3

# Display the original dictionary
print("Original Dictionary:", my_dict)

# Sorting the dictionary by keys
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted Dictionary by Keys:", sorted_dict)

# Sorting the dictionary by values
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary by Values:", sorted_dict_by_values)

# Search for an item in the dictionary
search_key = "banana"
if search_key in my_dict:
    print(f"{search_key} found in the dictionary. Value: {my_dict[search_key]}")
else:
    print(f"{search_key} not found in the dictionary.")

# Pop an item from the dictionary
pop_key = "orange"
if pop_key in my_dict:
    popped_value = my_dict.pop(pop_key)
    print(f"{pop_key} popped from the dictionary. Popped Value: {popped_value}")
else:
    print(f"{pop_key} not found in the dictionary.")

# Display the updated dictionary after popping
print("Updated Dictionary:", my_dict)
