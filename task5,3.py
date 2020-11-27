def my_func():
    res = 0
    while True:
        numbers = input('введите числа или q для выхода: ').split()
        for i in numbers:
            try:
                if i == 'q':
                    print(f'сумма = {res}.')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите текст или q')
        print(f'Sum is {res}')
print(my_func())