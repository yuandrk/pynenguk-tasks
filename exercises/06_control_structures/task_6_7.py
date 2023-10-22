# -*- coding: utf-8 -*-
"""
Завдання 6.7

У скрипті створено генератор конфігурації для access-портів. Зробити
аналогічний конфігураційний генератор для портів trunk.

У транка ситуація ускладнюється тим, що VLANів може бути багато, і треба
розуміти, що з ними робити (додавати, видаляти, перезаписувати).

Тому відповідно до кожного порту стоїть список і перший (нульовий) елемент
списку вказує, як сприймати номери VLAN, які йдуть далі.

Приклад значення та відповідної команди:

* ['add', '10', '20'] - switchport trunk allowed vlan add 10,20
* ['del', '17'] - switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - switchport trunk allowed vlan 11,30

Завдання для портів 0/1, 0/2, 0/4, 0/5, 0/7: згенерувати конфігурацію на основі
шаблону trunk_template з урахуванням ключових слів add, del, only
Код не повинен прив'язуватись до конкретних номерів портів. Тобто якщо в
словнику trunk будуть інші номери інтерфейсів, код повинен працювати.

Для даних у словнику trunk_template вивід на стандартний потік виводу має бути таким:

interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20,30,40
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17
interface FastEthernet0/5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,21
interface FastEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30

На стандартний потік виводу треба виводити лише команди trunk налаштування, а
access закоментувати.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {
    "0/1": ["add", "10", "20", "30", "40"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}


def generate_trunk_config(interface, config):
    result = []
    for command in trunk_template:
        if command == "switchport trunk allowed vlan":
            # Обробка команд 'add', 'del', 'only' для VLAN
            if config[0] == "add":
                vlan_command = f"{command} add {','.join(config[1:])}"
            elif config[0] == "del":
                vlan_command = f"{command} remove {','.join(config[1:])}"
            elif config[0] == "only":
                vlan_command = f"{command} {','.join(config[1:])}"
            result.append(vlan_command)
        else:
            result.append(command)
    return result


# Генеруємо конфігурацію для кожного порту trunk
for intf, config in trunk.items():
    print(f"interface FastEthernet{intf}")
    for line in generate_trunk_config(intf, config):
        print(f" {line}")