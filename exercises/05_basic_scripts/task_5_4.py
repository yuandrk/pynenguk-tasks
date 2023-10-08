# -*- coding: utf-8 -*-
"""
Завдання 5.4

Запросити користувача введення IP-адреси у форматі: 10.1.1.1

Потім вивести інформацію про адресу у такому форматі:
10        1         1         1
00001010  00000001  00000001  00000001

Перевірити роботу скрипта на різних IP-адресах, наприклад: 192.168.100.1, 10.5.5.190.

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

"""
ip_address = input("Enter IP-address: ")
octets = ip_address.split('.')

# Print the IP address in decimal format
print("{:<10}{:<10}{:<10}{:<10}".format(octets[0], octets[1], octets[2], octets[3]))

# Convert each octet to binary and format them correctly
binary_octets = [format(int(octet), '08b') for octet in octets]

# Print the IP address in binary format
print("{:<10}{:<10}{:<10}{:<10}".format(binary_octets[0], binary_octets[1], binary_octets[2], binary_octets[3]))
