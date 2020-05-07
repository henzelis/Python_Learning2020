#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ignore = ["duplex", "alias", "Current configuration"]

with open('config_sw1.txt') as cfg: 
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

