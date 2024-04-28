# -*- coding: utf-8 -*-
"""
Завдання 9.7

Створити функцію convert_config_to_dict, яка обробляє конфігураційний файл
комутатора та повертає словник:

* Усі команди верхнього рівня (команди, які не починаються з пробілу), будуть
  ключами.
* Якщо у команди верхнього рівня є підкоманди (команди, які починаються з
  пробілу), вони повинні бути у значенні у відповідного ключа у вигляді списку
  (пробіли на початку рядка треба видалити).
* Якщо команда верхнього рівня не має підкоманд, то значення буде порожнім
  списком

У функції мають бути такі параметри:
* config_filename - очікує як аргумент ім'я конфігураційного файлу
* ignore_lines - чекає як аргумент список рядків. Якщо в рядку файлу
  знаходиться одне зі слів у списку ignore_lines, потрібно ігнорувати рядок,
  тобто не додавати в словник.

Перевірити роботу функції на прикладі файлу config_sw1.txt

При обробці конфігураційного файлу, треба ігнорувати рядки, які починаються з
'!', порожні рядки, а також рядки, в яких містяться слова зі списку ignore.


Приклад роботи функції:
In [3]: cfg_dict1 = convert_config_to_dict("config_r2_short.txt", ignore)

In [4]: pprint(cfg_dict1, sort_dicts=False)
{'version 15.2': [],
 'no service timestamps debug uptime': [],
 'no service timestamps log uptime': [],
 'hostname PE_r2': [],
 'no ip http server': [],
 'no ip http secure-server': [],
 'ip route 10.2.2.2 255.255.255.255 Tunnel0': [],
 'ip access-list standard LDP': ['deny   10.0.0.0 0.0.255.255',
                                 'permit 10.0.0.0 0.255.255.255'],
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32': [],
 'mpls ldp router-id Loopback0 force': [],
 'control-plane': [],
 'line con 0': ['exec-timeout 0 0',
                'privilege level 15',
                'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all']}

In [5]: cfg_dict2 = convert_config_to_dict("config_sw1.txt", ignore)

In [6]: pprint(cfg_dict2, sort_dicts=False)
{'version 15.0': [],
 'service timestamps debug datetime msec': [],
 'service timestamps log datetime msec': [],
 'no service password-encryption': [],
 'hostname sw1': [],
 'interface FastEthernet0/0': ['switchport mode access',
                               'switchport access vlan 10'],
 'interface FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 100,200',
                               'switchport mode trunk'],
 'interface FastEthernet0/2': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 100,300,400,500,600',
                               'switchport mode trunk'],
 'interface FastEthernet1/0': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet1/1': ['switchport mode access',
                               'switchport access vlan 30'],
 'interface FastEthernet1/2': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 400,500,600',
                               'switchport mode trunk'],
 'interface Vlan100': ['ip address 10.0.100.1 255.255.255.0'],
 'line con 0': ['exec-timeout 0 0',
                'privilege level 15',
                'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all'],
 'end': []}


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""
ignore = ["duplex", "alias", "configuration"]


def convert_config_to_dict(config_filename, ignore_lines=None):
    """
    Processes a switch configuration file and returns a dictionary with top-level commands as keys
    and subcommands as values (if any), ignoring specific lines.

    :param config_filename: The name of the configuration file to process.
    :param ignore_lines: A list of words to ignore if found in a line.
    :return: A dictionary with top-level commands and their corresponding subcommands (as a list).
    """
    config_dict = {}
    current_command = None  # Track the current top-level command

    if ignore_lines is None:
        ignore_lines = []

    with open(config_filename) as file:
        for line in file:
            line = line.rstrip()  # Remove trailing whitespace

            # Skip empty lines, lines starting with '!', and lines containing ignored words
            if not line or line.startswith("!") or any(word in line for word in ignore_lines):
                continue

            # If line doesn't start with a space, it's a top-level command
            if not line.startswith(" "):
                current_command = line
                config_dict[current_command] = []  # Start a new list for subcommands
            else:
                # If it starts with a space, it's a subcommand
                config_dict[current_command].append(line.strip())  # Add subcommand

    return config_dict
