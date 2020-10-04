# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def ping_ip(ip): 
    print('Пингую', ip) 
    result = subprocess.run('ping {} -c 5 -n'.format(ip),
          shell=True, stdout=subprocess.PIPE,  
          stderr=subprocess.PIPE, encoding='utf-8') 
    if result.returncode == 0: 
        return True 
    else: 
        return False 
                                                         

