#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Введите IP-адрес в формате 10.0.1.1: ')
ip_list = ip.split('.')
ip_correct = False
while not ip_correct:
    if ip.count('.') != 3:
        print('Количество точек не равно 3')
    elif ip.replace('.', '').isnumeric() == False:
        print('IP-адрес не должен содержать букв')
    elif len(ip.split('.')) != 4:
        print('IP-адрес должен состоять из 4 октетов')
    for octet in ip_list:
        if int(octet) < 0 and int(octet) > 255:
            print('Октеты в IP-адресе должны быть в диапазоне от 0 до 255:')
    else:
        print('IP-адрес введен в верном формате')
        ip_correct = True

octet = int(ip.split('.')[0])

if octet <= 223 and octet != 0:
    print('unicast')
elif octet >=224 and octet <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
     print('unused')
