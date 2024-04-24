# -*- coding: utf-8 -*-
"""
Завдання 7.2

Створити скрипт, який оброблятиме конфігураційний файл комутатора і виводити на
екран рядки з конфіга, крім деяких.

Ім'я конфігураційного файлу передається як аргумент скрипту:
$ python task_7_2.py config_sw1.txt

Вивести на стандартний потік виведення команди з переданого конфігураційного
файлу, крім рядків, які починаються з '!'.

Вивід має бути без порожніх рядків.

Приклад роботи завдання:
$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...

"""

import sys

# Better variable naming for clarity
input_filename = sys.argv[1]

# Use a context manager for file handling
with open(input_filename) as file:
    # Initialize a flag for writing lines
    write_line = False
    
    # Loop through each line in the file
    for line in file:
        # If line starts with 'interface', print and set the flag to True
        if line.startswith('interface'):
            print(line.rstrip())  # Remove trailing spaces
            write_line = True
        
        # For specific keywords, print the line without a new line (end='')
        elif line.startswith(('version', 'service', 'Current', 'no service')):
            print(line, end='')
            
        elif line.startswith('hostname'):
            print(line.rstrip())  # Remove trailing spaces
            write_line = True
            
        # If line starts with a space, only print if 'write_line' is True
        elif line.startswith(" "):
            if write_line:
                print(line.rstrip())
        
        # Reset the flag if none of the above conditions are met
        else:
            write_line = False