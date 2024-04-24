# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Створити копію скрипта завдання 7.3a.

Переробити скрипт:
* запросити користувача ввести номер VLAN
* виводити інформацію лише за вказаним VLAN

Приклад роботи скрипта:
$ python task_7_3b.py
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

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

input_vlan = input('Enter VLAN number: ')
for vlan in vlan_list:
    if vlan[0] == int(input_vlan):
        print(f'{vlan[0]:<8}{vlan[1]:<20}{vlan[2]:<20}')
    else:
        continue