# -*- coding: utf-8 -*-
"""
Завдання 5.4a

Запросити користувача введення IP-мережі у форматі: 10.1.1.0 255.255.255.0

Потім вивести інформацію про мережу та маску в такому форматі:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Перевірити роботу скрипта на різних комбінаціях мережа/маска.

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Приклад роботи завдання:

$ python task_5_4a.py
Enter network address: 10.1.1.0 255.255.255.0

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


$ python task_5_4a.py
Enter network address: 10.1.1.192 255.255.255.240

Network:
10        1         1         192
00001010  00000001  00000001  11000000

Mask:
/28
255       255       255       240
11111111  11111111  11111111  11110000
"""

ip_address_mac = input("Enter network address and mask: ")  # Get the IP address and mask from the user
ip_address, mask = ip_address_mac.split()  # Split the input into IP address and mask

ip_octets = ip_address.split('.')
mask_octets = mask.split('.')

print("\nNetwork:")
print("{:<10}{:<10}{:<10}{:<10}".format(ip_octets[0], ip_octets[1], ip_octets[2], ip_octets[3]))

binary_ip_octets = [format(int(octet), '08b') for octet in ip_octets]
print("{:<10}{:<10}{:<10}{:<10}".format(*binary_ip_octets))

# Count the number of '1's in the binary mask to determine CIDR notation
binary_mask = ''.join([format(int(octet), '08b') for octet in mask_octets])
count = binary_mask.count('1')
cidr = count

print("\nMask:")
print("/{}".format(cidr))
print("{:<10}{:<10}{:<10}{:<10}".format(*mask_octets))
print("{:<10}{:<10}{:<10}{:<10}".format(*[format(int(octet), '08b') for octet in mask_octets]))



