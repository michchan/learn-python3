monday_temps = [9.1, 8.8, 7.5]

# Append item
monday_temps.append(12)

# Clear all items
monday_temps.clear()

# Get index of by value of an item
monday_temps.index(8.8) # => 1

# ----------- Accessing item -----------
monday_temps[0] # identical to : monday_temps.__getitem__(0)

# --- Slice a portion of the list / Accessing list Slices ---
# Slice from index 0 to index 2 (end-index 3 is exclusive)
monday_temps[0:2] # => [9.1, 8.8]
# Slice from the first one to index 2
monday_temps[:2] # => [9.1, 8.8]
# Slice from index 2 to the last one
monday_temps[1:] # => [8.8, 7.5]


# Negative indexing
monday_temps[-1] # => 7.5 (last item)
monday_temps[-2:] # => [8.8, 7.5]
monday_temps[-3:-1] # => [9.1, 8.8]

# String indexing
my_name = 'Michael'
my_name[0] # => 'M'
my_name[0:4] # => 'Mich'