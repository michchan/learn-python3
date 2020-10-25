# From tuple to list:
data = (1, 2, 3)
list(data) # => [1, 2, 3]

# From list to tuple:
data = [1, 2, 3]
tuple(data) # => (1, 2, 3)

# From list to dictionary: 
data = [["name", "John"], ["surname", "smith"]]
dict(data) # => {'name': 'John', 'surname': 'smith'}

# NOT WORK:
data = ['a', 'b']
dict(data)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

# NOT WORK: 
data = [1, 2, 3]
dict(data)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
# That's because a dictionary is made of key and value pairs, but the list was not constructed that way, so the above would generate an error.