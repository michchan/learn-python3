# FUNCTION NAMING:
# - Cannot start with a number
# - Cannot start with an operator


# Defintion of a mean function
def mean(list):
    result = sum(list) / len(list)
    return result

# Invocation of the mean function
mean_result = mean([1, 4, 6])
print(mean_result)

# 'function' vs 'builtin_function_or_method'
print(type(mean), type(sum))


# Without return (void)
def voidFunc():
    return None 
# or return print()
def printFunc():
    print('No return statement')