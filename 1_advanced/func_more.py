# Default parameter b = 6
def area(a, b = 6):
    return a * b

# Non-keyword argument (Positional argument)
print(area(4, 5))
# Keyword argument: position doesn't matter!
print(area(a = 4, b = 5))
print(area(b = 5, a = 4)) 

# * Optional argument has to be after mandatory argument!
# The following will not work
# def area(b = 6, a):
    # return a * b
# SyntaxError: non-default argument follows default argument


# ----------- With Arbituary Number of arguments -----------

# NON-keyword arguments
# - "args" is a naming convention.
# - "args" here is a Tuple.
def mean(*args):
    return sum(args) / len(args)

# args = (1, 2, 3)
print(mean(1, 2, 3))

# Keyword arguments
# - "kwargs" is a naming convention.
# - "kwargs" here is a dict. 
def mean2(**kwargs):
    return sum(kwargs.values()) / len(kwargs)

# kwargs = { 'a': 1, 'b': 2, 'c': 3 }
print(mean2(a = 1, b = 2, c = 3)) 
