# -*- coding: utf-8 -*-
"""
Завдання 7.4

Створити скрипт, який оброблятиме конфігураційний файл комутатора і
отримуватиме з нього інформацію про порти в режимі trunk і вланах, які
налаштовані на цих портах.

Ім'я конфігураційного файлу передається як аргумент скрипту.
$ python task_7_4.py config_trunk_sw2.txt
$ python task_7_4.py config_trunk_sw3.txt

Передавати ім'я файлу як аргумент скрипту. Вказаний конфіг потрібно обробити і
отримати словник портів у режимі trunk, де ключі номери портів, а значення
список дозволених VLAN (список рядків).

Записати підсумковий словник у змінну trunk_dict (саме ця змінна
перевірятиметься у тесті). За бажанням можна виводити словник на екран, тест
перевіряє лише вміст змінної. Тут зручно виводити словник за допомогою pprint.

Наприклад, для файлу config_trunk_sw2.txt повинен вийти такий словник:
$ python task_7_4.py config_trunk_sw2.txt
{'FastEthernet0/1': ['100', '200'],
 'FastEthernet0/3': ['100', '300', '400', '500', '600'],
 'FastEthernet0/4': ['400', '500', '600']}

Для файлу config_trunk_sw3.txt повинен вийти такий словник:
$ python task_7_4.py config_trunk_sw3.txt
{'FastEthernet0/1': ['10', '20', '21', '22'],
 'FastEthernet0/2': ['10', '13', '1450', '1451', '1452'],
 'FastEthernet0/6': ['40', '50', '60']}

Перевірити роботу функції на прикладі файлів config_trunk_sw2.txt та
config_trunk_sw3.txt. Переконайтеся, що в результаі для цих файлів виходять
вірні словники.

Підказка щодо синтаксису cisco: у цьому завданні вважаємо, що інтерфейс
знаходиться в режимі trunk, якщо в нього налаштована команда:
switchport trunk allowed vlan.
"""

import sys
import pprint

# Get the input filename from command-line arguments
input_filename = sys.argv[1]

# Dictionary to hold trunk port information
trunk_dict = {}

# Use a context manager to read the configuration file
with open(input_filename) as file:
    # Temporary variable to hold the current interface
    current_interface = None
    
    # Loop through each line in the configuration file
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        
        # If the line starts with 'interface', set the current interface
        if line.startswith("interface"):
            current_interface = line.split()[1]  # Extract interface name
        
        # If the current interface is in trunk mode, extract allowed VLANs
        if "switchport trunk allowed vlan" in line:
            # Extract VLANs from the line and store in the dictionary
            vlan_list = line.split("vlan")[-1].strip().split(",")
            trunk_dict[current_interface] = vlan_list

# Output the resulting dictionary using pprint for better readability
pprint.pprint(trunk_dict)
