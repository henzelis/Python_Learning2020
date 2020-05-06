#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес в формате 10.0.1.1: ')
ip_list = ip.split('.')

while True:
    for octet in ip_list:
        if int(octet) < 0 or int(octet) > 255:
            octets = False
            break
        else:
            octets = True
    if ip.count('.') != 3 or len(ip.split('.')) != 4 or ip.replace('.', '').isnumeric() == False or octets == False:
        print('Неправильный IP-адрес')
        
    else:
        break
    ip = input('Попробуйте еще раз ввести IP-адрес в формате 10.0.1.1: ')
    ip_list = ip.split('.')

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
