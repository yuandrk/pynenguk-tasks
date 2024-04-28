# -*- coding: utf-8 -*-
"""
Завдання 9.6a

Зробити копію функції get_int_vlan_map із завдання 9.6.

Доповнити функцію: додати підтримку конфігурації, коли налаштування порту
access виглядає так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

Тобто, порт знаходиться у VLAN 1

У такому випадку до словника портів повинна додаватися інформація, що порт у
VLAN 1. Приклад словника:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

Функція повинна мати один параметр config_filename, який очікує як аргумент
ім'я конфігураційного файлу.

Перевірити роботу функції на прикладі файлу config_sw2.txt
Приклад роботи функції
In [2]: get_int_vlan_map("config_sw2.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30,
  'FastEthernet1/3': 1,
  'FastEthernet2/0': 1,
  'FastEthernet2/1': 1},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [4]: access, trunk = get_int_vlan_map("config_sw2.txt")

In [5]: access
Out[5]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30,
 'FastEthernet1/3': 1,
 'FastEthernet2/0': 1,
 'FastEthernet2/1': 1}

In [6]: trunk
Out[6]:
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

    This updated version includes support for ports in access mode without specified VLANs,
    assigning them to VLAN 1 by default.

    :param config_filename: The name of the configuration file to process.
    :return: A tuple of two dictionaries (access_ports, trunk_ports).
    """
    # Dictionaries to store access and trunk ports
    access_ports = {}
    trunk_ports = {}

    with open(config_filename) as file:
        current_port = None  # Keep track of the current interface
        access_mode = False  # Flag to indicate if a port is in access mode

        for line in file:
            line = line.strip()  # Remove leading/trailing spaces

            # If the line starts with 'interface', set the current port and reset flags
            if line.startswith("interface"):
                current_port = line.split()[1]
                access_mode = False  # Reset access mode flag

            # Check if the port is in access mode
            elif "switchport mode access" in line:
                access_mode = True  # Mark the port as in access mode

            # Assign default VLAN 1 if the port is in access mode and not specified
            elif access_mode and "switchport access vlan" not in line and current_port not in access_ports:
                access_ports[current_port] = 1  # Default to VLAN 1 if not specified

            # Assign specified VLAN if explicitly set
            elif "switchport access vlan" in line:
                vlan = int(line.split()[-1])
                access_ports[current_port] = vlan  # Add to the access ports dictionary

            # Assign VLANs for trunk ports
            elif "switchport trunk allowed vlan" in line:
                vlan_list = list(map(int, line.split()[-1].split(",")))  # Get VLAN numbers
                trunk_ports[current_port] = vlan_list  # Add to the trunk ports dictionary

    return access_ports, trunk_ports
