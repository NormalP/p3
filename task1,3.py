def s_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
print(s_div((int(input('Enter first number: '))), (int(input('Enter second number: ')))))