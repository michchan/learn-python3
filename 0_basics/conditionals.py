# if-else conditional
def mean(value):
    # Check the type of value
    if type(value) == dict:
        result = sum(value.values()) / len(value)
    else:
        result = sum(value) / len(value)
    return result


student_grades = { 'mary': 30, 'Sim': 60, 'John': 12 }
print(mean(student_grades))

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(mean(student_grades))


# and / or operator,
# elif
def check_multiple_conditions(value):
    if value == 1 or value == 2:
        return 3
    elif value > 3 and value <= 10:
        return 4   
    return 1

print(check_multiple_conditions(1))
print(check_multiple_conditions(5))