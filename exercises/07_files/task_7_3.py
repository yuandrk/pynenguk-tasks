# -*- coding: utf-8 -*-
"""
Завдання 7.3

Скрипт повинен обробляти записи у файлі CAM_table.txt. Кожен рядок, де є
MAC-адреса, має бути оброблена таким чином, щоб на стандартний потік виведення
була виведена таблиця виду:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9

"""

with open ('CAM_table.txt') as f:
    is_header = True
    for line in f:
        if is_header:
            if 'Mac Address Table' in line:
                is_header = False
            continue
        if line.startswith(' '):
            line = line.split()
            enf = line[-1]
            vlan = line[0]
            mac = line[1]
            print(f'{vlan:20}{mac:20}{enf}')
