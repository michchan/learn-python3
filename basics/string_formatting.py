# ---------- Single variable ---------

user_input = input('Enter your name: ')

# For python 2 or 3
message = 'Hello %s' % user_input
print(message)

# For python 3.6+
message = f'Hello {user_input}'
print(message)

# ---------- Multiple variables ---------

firstname = input('Enter your first name: ')
surname = input('Enter your surname: ')

# For python 2 or 3
message = 'Hello %s %s' % (firstname, surname)
print(message)
# or store in a Tuple first
names = (firstname, surname)
message = 'Hello %s %s' % names
print(message)

# For python 3.6+
message = f'Hello {firstname} {surname}'
print(message)