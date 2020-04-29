# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac_clear = mac.replace(':','')
print(str(bin(int(mac_clear, 16))).lstrip('0b'))

'''
Long resolution of task step by step
'''

mac_clear = mac.replace(':','')
mac_bin = bin(int(mac_clear, 16))
print(mac_bin.lstrip('0b'))

