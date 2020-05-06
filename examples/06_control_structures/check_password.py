# -*- coding: utf-8 -*-

username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

password_ok = False

while not password_ok:
    if len(password) < 8:
        print('Пароль слишком короткий')
    elif username.lower() in password.lower():
        print("Пароль содержит имя пользователя")
    elif not '@' in password:
        pass
        #print('В пароле должна быть собака')
    else:
        print("Пароль для пользователя {} установлен".format(username))
        password_ok = True
        continue
    password = input('Введите пароль еще раз:')


"""
Usage example:

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: nata1234
Пароль содержит имя пользователя

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 123nata123
Пароль содержит имя пользователя

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 1234
Пароль слишком короткий

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 123456789
Пароль для пользователя nata установлен
"""
