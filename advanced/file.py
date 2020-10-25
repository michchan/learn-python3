# -------------- Open and read a file --------------

# Open a file object
myfile = open('assets/fruits.txt')
# Read the file as string.
# Before the read() invoked, the cursor is at the start of the file object.
content = myfile.read()
print(content)
# After the .read() invoked, the cursor has gone to the end of the file object.
# Now if we call .read() again, it should read nothing / an empty string.
print(myfile.read())
# Close the file
myfile.close()

# -------------- ...in a Better/Recommended way --------------

# Open the file with the "with" context manager.
# It will be more organized and safer to do any file object operation,
# as everything has to be done within the scope/block after the "with" statement.
with open('assets/fruits.txt') as myfile:
    content = myfile.read()
    
# This statement is out of the scope of the above "with" context
print(content)

# -------------- mode of read/write --------------

# Read mode: r
with open('assets/fruits.txt', 'r') as myfile:
    content = myfile.read()

# See help(open) for different modes!

# Write/replace content to a file:
# Write mode: w
# It "create one if the file doesn't exists"
with open('assets/vegetables.txt', 'w') as myfile:
    num_chars_written = myfile.write('Tomato\nCucumber\nOnion')
    print(num_chars_written)

# Append: a
with open('assets/vegetables.txt', 'a') as myfile:
    myfile.write('\nOkra')

# Append and read: a+
with open('assets/vegetables.txt', 'a+') as myfile:
    myfile.write('\nOkra')
    # Move the cursor to the start
    myfile.seek(0)
    print('--- Updated content:')
    print(myfile.read())

# Create, or throw an error if the file exists: x
# It should throw something like: 
# FileExistsError: [Errno 17] File exists: 'vegetables.txt'
with open('assets/vegetables.txt', 'x') as myfile:
    myfile.write('\nOkra')