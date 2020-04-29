# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1_vlan_list = command1.split()[-1].split(',')
command2_vlan_list = command2.split()[-1].split(',')
vlan_intersection_list = list(set(command1_vlan_list).intersection(set(command2_vlan_list)))
vlan_intersection_list.sort
print(vlan_intersection_list)

"""
Long resolution step by step

"""
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1_vlan_list = command1.split()[-1].split(',')
command2_vlan_list = command2.split()[-1].split(',')
vlan_set1 = set(command1_vlan_list)
vlan_set2 = set(command2_vlan_list)
vlan_intersection = vlan_set1.intersection(vlan_set2)
vlan_intersection_list = list(vlan_intersection)
vlan_intersection_list.sort()
print(vlan_intersection_list)

