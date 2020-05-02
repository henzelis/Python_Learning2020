#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_mask = input('Введите адрес IP-сети в формате IP/mask: ')
ip = ip_mask.split('/')[0]
mask = ip_mask.split('/')[-1]
a, b, c, d = ip.split('.')
template_ip_decimal = "{:8} {:8} {:8} {:8}"
template_ip_binary = "{:08b} {:08b} {:08b} {:08b}"
print('Network:')
print(template_ip_decimal.format(a, b, c, d))
print(template_ip_binary.format(int(a), int(b), int(c), int(d)))
print('\t')

template_mask = "{:<032}"
mask_bin = (template_mask.format(int('1'*int(mask)))).strip()
mask_a = mask_bin[0:8]
mask_b = mask_bin[8:16]
mask_c = mask_bin[16:24]
mask_d = mask_bin[24:]
template_mask_decimal = "{:<8} {:<8} {:<8} {:<8}"

print('Mask: ')
print('/'+mask)
print(template_mask_decimal.format(int(mask_a, 2), int(mask_b, 2), int(mask_c, 2), int(mask_d, 2)))
print(template_mask_decimal.format(mask_a, mask_b, mask_c, mask_d))
