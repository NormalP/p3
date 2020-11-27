def my_func(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)
def my_func_use():
    print(my_func(input('Введите текст: ').split()))
print(my_func_use())