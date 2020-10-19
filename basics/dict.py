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

# Accessing item
student_grades['Marry'] # => 9.1



