#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

with open('config_sw1.txt') as cfg, open('config_sw1_cleared.txt', 'w') as clear_cfg: 
    for line in cfg:
        if line.startswith('!'):
             pass
        else:      
            for word in ignore:
                if word not in line:
                    flag = 1 
                else:
                    flag = 0
                    break
            if(flag == 1):
                print(line.rstrip())
                clear_cfg.write(line)
