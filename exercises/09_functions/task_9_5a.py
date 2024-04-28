# -*- coding: utf-8 -*-
"""
Завдання 9.5a

Зробити копію функції generate_trunk_config із завдання 9.5

Змінити функцію таким чином, щоб вона повертала не список команд, а словник:
* ключі: імена інтерфейсів, виду 'FastEthernet0/1'
* значення: список команд, який потрібно виконати на цьому інтерфейсі

Перевірити роботу функції на прикладі словника trunk_dict та шаблону
trunk_cmd_list.


Приклад роботи функції
In [2]: pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
{'FastEthernet0/1': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 10,20,30'],
 'FastEthernet0/2': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 11,30'],
 'FastEthernet0/4': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 17']}

У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""


trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_dict, trunk_template):
    """
    Generate trunk port configurations and return a dictionary with interfaces as keys.

    :param intf_vlan_dict: Dictionary mapping interfaces to lists of VLANs
    :param trunk_template: List of commands for trunk port configuration
    :return: A dictionary where keys are interfaces and values are lists of commands
    """
    # Dictionary to store the configuration for each interface
    config_dict = {}

    # Loop through each interface in the dictionary
    for interface, vlans in intf_vlan_dict.items():
        # Create a list to store commands for the current interface
        interface_commands = []

        # Loop through each command in the template
        for command in trunk_template:
            if command == "switchport trunk allowed vlan":
                # Convert VLAN list to comma-separated string
                vlan_list = ",".join(map(str, vlans))
                interface_commands.append(f"{command} {vlan_list}")
            else:
                interface_commands.append(command)

        # Add the interface-specific commands to the config dictionary
        config_dict[interface] = interface_commands

    return config_dict
