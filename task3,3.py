def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)
def my_func_use():
    print(my_func(a = int(input()), b = int(input()), c = int(input())))
print(my_func_use())