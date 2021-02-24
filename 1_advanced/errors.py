def divide(a, b):
    try:
        return a / b
    # except:
    except ZeroDivisionError:
        return 'Zero division is meaningless'

print(divide(1, 0))