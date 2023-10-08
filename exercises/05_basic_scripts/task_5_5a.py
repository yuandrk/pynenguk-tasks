# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
"""
# Define configuration templates for access and trunk modes
templates = {
    'access': {
        'template': """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
""",
        'prompt': 'Enter VLAN number:'
    },
    'trunk': {
        'template': """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
""",
        'prompt': 'Enter the allowed VLANs:'
    }
}

# Get user input
interface_mode = input("Enter interface mode (access/trunk): ")
interface_type = input("Enter interface type and number: ")
vlan_number = input(templates[interface_mode]['prompt'])

# Check if the selected interface mode exists in the templates dictionary
if interface_mode in templates:
    print("interface", interface_type)
    print(templates[interface_mode]['template'].format(vlan_number))
else:
    print("Wrong interface mode")
