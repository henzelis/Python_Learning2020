#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv

src = argv[1]
dst = argv[2]

ignore = ["duplex", "alias", "Current configuration"]

with open(src) as cfg, open(dst, 'w') as clear_cfg: 
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