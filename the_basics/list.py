
# Data type: list (mutable)
marks_list = [45, 63, 87]
print(marks_list, type(marks_list))

# Create list with range
ranged_list = list(range(1, 10, 2))
print(ranged_list)

# Calculate Average
sum_mark = sum(marks_list)
marks_length = len(marks_list)
mean = sum_mark / marks_length
print(sum_mark, mean)

# Calculate Max
max_mark = max(marks_list)
print(max_mark)

# Count a repeated item in a list
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))
monday_temps = [9.1, 8.8, 7.5]

# ----------- List operations -----------

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