#
'''
Модуль проверки IP-адреса
'''

import ipaddress

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

ip1 = '10.1.1.1'
ip2 = '1.1.1'

print(__name__)

# не запускать при импорте
if __name__== "__main__":
    print('Проверяем IP-адреса')
    print(ip1, check_ip(ip1))
    print(ip2, check_ip(ip2))

