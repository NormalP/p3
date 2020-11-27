def func(**kwargs):
    return list(kwargs.values())


def func_use():
    print(func(name=input('Имя: '),
                s_name=input('Фамилия: '),
                date=input('Дата рождения: '),
                town=input('Город проживания: '),
                email=input('email: '),
                tel=input('Номер телефона: ')))
print(func_use())