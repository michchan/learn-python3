import datetime

# Printing
time_now = datetime.datetime.now()
print('The date and time is', time_now)

my_num = 10
my_text = 'Hello'
print(my_num, my_text)

# Data types: int, str, float
x = 10 # type: int
y = '10' # type: str
z = 10.1 # type: float
sum1 = x + x
sum2 = y + y
print(sum1, sum2)
print(type(x), type(y), type(z))

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

# Convert to lowercase
username = 'Python3'
print(username.lower())

# Dictionary types
student_grades = { 'mary': 30, 'Sim': 60, 'John': 12 }
test_num_as_key = { 123: 1321 }
print(student_grades, test_num_as_key)

# Complex dictionary
day_temperatures = {
    'morning': (24, 26, 25, 23, 22, 23, 25),
    'noon': (24, 26, 25, 23, 22, 23, 25),
    'evening': (24, 26, 25, 23, 22, 23, 25),
}
print({ 'day_temperatures': day_temperatures })

# Dictionary to list
student_grades_values = student_grades.values()
student_grades_keys = student_grades.keys()
print(student_grades_values, student_grades_keys)

# Tuple type (Immutable)
monday_temperatures = (1, 4, 5)
print({ 'monday_temperatures': monday_temperatures })

# Nested tuple
color_codes = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# List vs Tuple
# List is MUTABLE!
num_list = [1, 2, 3, 4, 5]
num_list.append(6)
num_list.remove(2)
print({ 'num_list': num_list })