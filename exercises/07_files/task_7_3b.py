#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_input = input('Введите номер VLAN: ')
vlan_input = int(vlan_input)

with open('CAM_table.txt') as mac:
    mac_table = []
    for line in mac:
        if 'DYNAMIC' in line:
           mac_list = line.rstrip('\n').split()
           mac_list.remove('DYNAMIC')
           mac_list[0] = int(mac_list[0])
           mac_table.append(mac_list)
    mac_table.sort()
    for string in mac_table:
        template_mac_out = "{:<8} {:17} {:10}"
        vlan, mac_addr, intf = string
        if vlan_input in string:
            print(template_mac_out.format(vlan, mac_addr, intf))