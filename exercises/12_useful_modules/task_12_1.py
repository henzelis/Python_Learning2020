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
def ping_ip_addresses(ip_list):
    import subprocess
    list_ok = []
    list_fail = []
    for ip in ip_list:
        print("Пингую адресс ",ip)
        result = subprocess.run('ping {} -c 2 -n'.format(ip),
        shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, encoding='utf-8')
        if result.returncode == 0:
            list_ok.append(ip)
        else:
            list_fail.append(ip)
    all_ip = (list_ok,list_fail)
    return(all_ip)

if __name__=="__main__":
    ip_list=['1.1.1.1', '4.4.4.4', '8.8.8.8']
    print(ping_ip_addresses(ip_list))

