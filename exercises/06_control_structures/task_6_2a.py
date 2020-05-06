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

for octet in ip_list:
    if int(octet) < 0 or int(octet) > 255:
        octets = False
        break
    else:
        octets = True

if ip.count('.') != 3 or len(ip.split('.')) != 4 or ip.replace('.', '').isnumeric() == False or octets == False:
    print('Неправильный IP-адрес')

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
