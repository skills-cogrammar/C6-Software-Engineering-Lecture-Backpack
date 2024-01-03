def function_call():
    last_function()


def last_function():
    another_function()


def another_function():
    return 3 * 12


result = function_call()

print(result)
