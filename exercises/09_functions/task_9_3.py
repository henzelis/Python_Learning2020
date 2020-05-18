#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    dict_access = {}
    dict_trunk = {}
    with open(config_filename) as src:
        result = src.readlines()
        for line in result:
            if 'Fast' in line:
                intf = line.split()[1]
            elif 'trunk allowed' in line:
                trunk_vlan = line.split()[4]
                trunk_vlan = list(int(i) for i in trunk_vlan.split(','))
                dict_trunk[intf] = trunk_vlan
            elif 'access vlan' in line:
                access_vlan = line.split()[3]
                access_vlan = int(access_vlan)
                dict_access[intf] = access_vlan
    set_common = (dict_access, dict_trunk)
    return set_common

