def function_with_uncommon_bug_fixed(x, y):
    if x == 0 and y == 0:
        raise ZeroDivisionError("Both x and y cannot be zero.")
    elif x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x / y

result = function_with_uncommon_bug_fixed(0, 0)  # This will now raise a ZeroDivisionError
print(result)