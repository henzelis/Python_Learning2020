# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""

def print_ip_table(list1, list2):
    if len(list1) != len(list2):
        list1_new = list1[:]
        list2_new = list2[:]
        len_dif = len(list1_new) - len(list2_new)
        if len_dif < 0:
            while len_dif != 0:
                list1_new.append(' ')
                len_dif = abs(len_dif-1)
            result = zip(list1_new, list2_new)
            #print(tabulate(result, headers=['Reachable', 'Unreachable']))
        elif len_dif > 0:
            while len_dif !=0:
                list2_new.append(' ')
                len_dif = abs(len_dif-1)
            result = zip(list1_new, list2_new)
            #print(tabulate(result, headers=['Reachable', 'Unreachable']))
    else:
        result = zip(list1, list2)
       #print(tabulate(result, headers=['Reachable', 'Unreachable']))

    return print(tabulate(result, headers=['Reachable', 'Unreachable']))
    
