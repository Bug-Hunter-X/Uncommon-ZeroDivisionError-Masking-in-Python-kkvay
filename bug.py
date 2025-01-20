def function_with_uncommon_bug(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x / y

result = function_with_uncommon_bug(0, 0)  # This will return 0, which might be unexpected.
print(result)