# List and Tuple examples

_list = [1, 2, 3]            # A list with integer elements
_tuple = (1, "two", True)   # A tuple with mixed types: integer, string, boolean
_tuple2 = (3, "four", True) # Another tuple with mixed types

# Print types of list and tuple
print(type(_list))  # Output: <class 'list'>
print(type(_tuple)) # Output: <class 'tuple'>

# Accessing elements
print(_list[1])     # Output: 2
print(_tuple[1])    # Output: "two"

# Getting the length of list and tuple
print(len(_list))   # Output: 3
print(len(_tuple))  # Output: 3

# Modifying list and tuple
_list[0] = 5       # Lists are mutable, so you can change elements
# _tuple[0] = 5    # Tuples are immutable, so you cannot change elements

# Adding elements to list and tuple
_list.append(3)    # Appends 3 to the end of the list
# _tuple.append(5) # Tuples do not have an append method

# Count occurrences of an element in tuple
print(_tuple.count('two')) # Output: 1

# Concatenate tuples
print(_tuple + _tuple2) # Output: (1, "two", True, 3, "four", True)

# Convert a list to a tuple
_t = tuple([3, 4, 5])

# Print the type and contents of the new tuple
print(type(_t))    # Output: <class 'tuple'>
print(_t)          # Output: (3, 4, 5)

# Print final values of list and tuple
print(_list)       # Output: [5, 2, 3, 3]
print(_tuple)      # Output: (1, "two", True)
