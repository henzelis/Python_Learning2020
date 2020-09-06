#
'''
'''
from function_check_ip import check_ip

def return_correct_ip(ip_list):
    correct_ip = []
    for ip in ip_list:
        if check_ip(ip):
            correct_ip.append(ip)
        else:
            print(f'IP-адрес {ip} не прошел проверку')
     #correct_ip = [ip for ip int ip_list if check_ip(ip)]
    return correct_ip

ip_addresses = ['101.1.1.1', '8.8.8.8', '4.4.4.4', '2.2.2', '3.3.3', '1.1.1.']
print('#'*30)
print(ip_addresses)
correct = return_correct_ip(ip_addresses)
print(correct)
