def factorial_recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        factorial = number * factorial_recursive(number-1)
        return factorial

test_no = 7
print("The factorial of {0} is {1}".format(test_no, factorial_recursive(test_no)))