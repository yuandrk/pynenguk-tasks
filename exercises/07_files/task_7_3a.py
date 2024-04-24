# -*- coding: utf-8 -*-
"""
Завдання 7.3a

Зробити копію скрипта завдання 7.3.

Переробити скрипт: Відсортувати вивід за номером VLAN

В результаті має вийти такий вивід:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Зверніть увагу на vlan 1000 – він повинен виводитися останнім. Правильне
сортування можна досягти, якщо vlan буде числом, а не рядком.

Підказка: Для сортування зручно спочатку створити список списків такого типу, а
потім сортувати (зверніть увагу на те, що VLAN число).

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

Сортування має бути за першим елементом (vlan), і якщо перший елемент
однаковий, то з другого. Так працює за замовчуванням функція sorted та метод
sort, якщо сортувати перелік списків вище.
"""

from pprint import pprint

vlan_list = []

with open('CAM_table.txt') as f:
    is_header = True
    for line in f:
        if is_header:
            if 'Mac Address Table' in line:
                is_header = False
            continue
        if line.startswith(' '):
            line = line.split()
            vlan = int(line[0])
            mac = line[1]
            interface = line[-1]
            vlan_list.append([vlan, mac, interface])

vlan_list.sort()


for entry in vlan_list:
    print(f"{entry[0]:<20} {entry[1]:<20} {entry[2]:<20}")