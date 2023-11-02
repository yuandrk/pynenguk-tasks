# -*- coding: utf-8 -*-
import sys
"""
Завдання 7.2b

Скопіювати код із завдання 7.2a та переробити його: замість виведення на стандартний потік виведення, скрипт повинен записати отримані рядки у файл.

Імена файлів потрібно передавати як аргументи скрипту:
1 аргумент ім'я вихідного конфігураційного файлу
2 аргумент ім'я підсумкового файлу конфігурації, в який будуть записані рядки

Приклад роботи завдання:
$ python task_7_2b.py config_sw1.txt new_config.txt

При цьому повинні бути відфільтровані рядки зі словами, які містяться в списку
ignore та рядки, що починаються на '!'.
"""

ignore = ["duplex", "alias", "configuration", "end", "service"]

with open(sys.argv[1]) as f, open(sys.argv[2], 'w') as b:
    for line in f:
        if line.startswith('!'):
            continue
        elif line.startswith(('version', 'service', 'Current', 'no service')):
            print(line, end='')
            b.write(line)
        elif line.startswith(" "):
            if line.split()[0] not in ignore:
                print(line.rstrip())
                b.write(line.rstrip())
        else:
            continue