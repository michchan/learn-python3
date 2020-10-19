monday_temperatures = [9.1, 8.8, 7.6]

# Loop through a list
for temperature in monday_temperatures:
    print(round(temperature))

# Loop every character of a string
for letter in 'hello':
    print(letter.title())


student_grades = { 'mary': 30, 'Sim': 60, 'John': 12 }
# Loop through a dictionary
# items
for grades in student_grades.items():
    print(grades) # => Tuple: (key, value)
# value
for value in student_grades.values():
    print(value)
# key
for key in student_grades.keys():
    print(key)