# -*- coding: utf-8 -*-
"""
Завдання 7.2a

Створити скрипт, який оброблятиме конфігураційний файл комутатора і виводити на
екран рядки з конфіга, крім деяких.

Ім'я конфігураційного файлу передається як аргумент скрипту
$ python task_7_2a.py config_sw1.txt

Вивести на стандартний потік виведення команди з переданого конфігураційного
файлу, крім рядків, які починаються з '!' і рядки, в яких містяться слова зі
списку ignore. Вивід не повинен містити порожні рядки.

Приклад роботи завдання:
$ python task_7_2a.py config_sw1.txt
version 15.0
hostname sw1
interface Ethernet0/0
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet0/2
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet1/0
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all

Перевірити роботу скрипта на конфігураційному файлі config_sw1.txt. Ім'я файлу
передається як аргумент скрипту.
"""
import sys

# List of keywords to ignore if they exist anywhere in a line
ignore_keywords = ["duplex", "alias", "configuration", "end", "service"]

# Function to check if a line contains any of the ignore keywords
def contains_any(line, keywords):
    # Check if any keyword from the list exists in the line
    return any(keyword in line for keyword in keywords)

# Better variable naming for clarity
input_filename = sys.argv[1]

# Use a context manager for file handling
with open(input_filename) as file:
    # Loop through each line in the file
    for line in file:
        line = line.rstrip()  # Remove trailing whitespace
        # Ignore empty lines
        if not line:
            continue
        
        # Skip lines that start with '!'
        if line.startswith("!"):
            continue
        
        # Skip lines containing ignore keywords
        if contains_any(line, ignore_keywords):
            continue
        
        # If none of the above conditions are met, print the line
        print(line)
