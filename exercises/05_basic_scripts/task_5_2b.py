#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ip = argv[1]
mask = argv[2]
a, b, c, d = ip.split('.')
template_bin_ip = "{:08b}"+"{:08b}"+"{:08b}"+"{:08b}"
template_network = "{:<032}"
bin_network = template_network.format(str(template_bin_ip.format(int(a), int(b), int(c), int(d)))[:int(mask)]) 
ip_a = bin_network[:8]
ip_b = bin_network[8:16]
ip_c = bin_network[16:24]
ip_d = bin_network[24:]

template_ip_decimal = "{:<8} {:<8} {:<8} {:<8}"
print('Network:')
print(template_ip_decimal.format(int(ip_a, 2), int(ip_b, 2), int(ip_c, 2), int(ip_d, 2)))
print(template_ip_decimal.format(ip_a, ip_b, ip_c, ip_d))
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
