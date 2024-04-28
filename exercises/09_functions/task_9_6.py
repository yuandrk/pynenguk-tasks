# -*- coding: utf-8 -*-
"""
Завдання 9.6

Створити функцію get_int_vlan_map, яка обробляє конфігураційний файл комутатора
та повертає кортеж із двох словників:
* словник портів у режимі access, де ключі номери портів, а значення access
  VLAN (числа)
* словник портів у режимі trunk, де ключі номери портів, а значення список
  дозволених VLAN (список чисел)

Функція повинна мати один параметр config_filename, який очікує як аргумент
ім'я конфігураційного файлу.

Перевірити роботу функції на прикладі файлу config_sw1.txt

Приклад роботи функції
In [2]: get_int_vlan_map("config_sw1.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [3]: access, trunk = get_int_vlan_map("config_sw1.txt")

In [4]: access
Out[4]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30}

In [5]: trunk
Out[5]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""


def get_int_vlan_map(config_filename):
    """
    Processes a switch configuration file and returns a tuple with two dictionaries:
    - Dictionary of access ports with port names as keys and VLAN numbers as values.
    - Dictionary of trunk ports with port names as keys and lists of allowed VLANs as values.

    :param config_filename: The name of the configuration file to process.
    :return: A tuple of two dictionaries (access_ports, trunk_ports).
    """
    # Dictionaries to store access and trunk ports
    access_ports = {}
    trunk_ports = {}

    with open(config_filename) as file:
        current_port = None  # Keep track of the current interface

        for line in file:
            line = line.strip()  # Remove leading/trailing spaces

            # If the line starts with 'interface', set the current port
            if line.startswith("interface"):
                current_port = line.split()[1]

            # Check if the current port is in access mode and find its VLAN
            elif "switchport mode access" in line:
                continue  # Move to the next line

            elif "switchport access vlan" in line:
                vlan = int(line.split()[-1])  # Get the VLAN number
                access_ports[current_port] = vlan  # Add to the access ports dictionary

            # Check if the current port is in trunk mode and find allowed VLANs
            elif "switchport trunk allowed vlan" in line:
                vlan_list = list(map(int, line.split()[-1].split(",")))  # Get VLAN numbers as a list
                trunk_ports[current_port] = vlan_list  # Add to the trunk ports dictionary

    return access_ports, trunk_ports
