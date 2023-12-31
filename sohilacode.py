#For the input 30, 20, 56, 75, 31, 19 and hash function h(K) = K mod 11
# construct the closed hash table.
# Search for value 31



hash_table = [None] * 11

def hash_function(key):
    return key % 11

def insert(table, key, value):
    index = hash_function(key)
    while table[index] is not None:
        index = (index + 1) % len(table)

    table[index] = (key, value)

def search(table, key):
    index = hash_function(key)
    initial_index = index

    while table[index] is not None:
        if table[index][0] == key:
            return index
        index = (index + 1) % len(table)
        if index == initial_index:
            break

    return None

# Given input
input_values = [30, 20, 56, 75, 31, 19]

# Initialize a hash table with None values
hash_table = [None] * 11

# Insert values into the hash table
for value in input_values:
    insert(hash_table, value, value)

# Display the constructed hash table
display(hash_table)

# Search for value 31
search_result = search(hash_table, 31)
if search_result is not None:
    print(f"Value 31 found at index {search_result}")
else:
    print("Value 31 not found in the hash table.")