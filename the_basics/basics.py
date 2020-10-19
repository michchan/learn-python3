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

# Convert to lowercase
username = 'Python3'
print(username.lower())