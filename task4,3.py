def my_func(x, y):
    return 1 / x ** abs(y)
def my_func_use():
    print(my_func(x = int(input()), y = int(input())))
print(my_func_use())
