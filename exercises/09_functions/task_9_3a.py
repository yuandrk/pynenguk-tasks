# -*- coding: utf-8 -*-
"""
Завдання 9.3a

Створити функцію clean_config. Функція clean_config обробляє конфігураційний
файл та повертає список команд із зазначеного конфігураційного файлу.

Функція clean_config повинна мати такі параметри:
* config_filename - чекає як аргумент на ім'я конфігураційного файлу
* ignore_lines - чекає як аргумент список рядків з підстроками, які треба
  ігнорувати.  Значення за замовчуванням None. Тобто за замовчуванням жодні рядки
  не ігноруються
* ignore_exclamation - контролює чи ігноруються рядки, які починаються зі знака
  оклику. Можливі значення True/False. Значення за промовчанням True
* strip_lines - контролює видалення пробілу на початку рядка та перекладу рядка
  в кінці. True - видалити пробілу на початку рядка та переклад наприкінці,
  False - не видаляти. Можливі значення True/False. Значення за замовчуванням False
* delete_empty_lines – контролює видалення порожніх рядків. True – видаляти,
  False – ні. Можливі значення True/False. Значення за замовчуванням True

Для зручності всі значення за замовчуванням для необов'язкових параметрів:
* ignore_lines - None
* ignore_exclamation - True
* delete_empty_lines - True
* strip_lines - False

Функція clean_config обробляє конфігураційний файл та повертає список команд із
зазначеного конфігураційного файлу:
* якщо параметр ignore_lines передає список рядків - виключаючи рядки
  конфігурації, в яких містяться рядки зі списку ignore_lines.
* якщо ignore_exclamation дорівнює True - виключаючи рядки, які починаються з '!'
* якщо delete_empty_lines дорівнює True - виключаючи порожні рядки
* якщо strip_lines дорівнює True - рядки у списку повинні бути без пробілів на
  початку та переведення рядка в кінці рядка


Приклад роботи функції:
In [3]: clean_config("config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list, ignore_exclamation=False)
Out[3]:
['hostname PE_r3',
 '!',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 '!',
 '!',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 '!',
 '!',
 '!',
 'alias configure sh do sh',
 '!',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']

In [4]: clean_config("config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list)
Out[4]:
['hostname PE_r3',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 'alias configure sh do sh',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']

In [5]: clean_config("config_r3_short.txt", strip_lines=True, delete_empty_lines=False)
Out[5]:
['hostname PE_r3',
 '',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 '',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 '',
 'alias configure sh do sh',
 'alias exec ospf sh run | s ^router ospf',
 'alias exec bri show ip int bri | exc unass',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""
import sys

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

config_filename = sys.argv[1]


def clean_config(
    config_filename,
    ignore_lines=None,
    ignore_exclamation=True,
    strip_lines=False,
    delete_empty_lines=True,
):
    """
    Processes a configuration file and returns a list of commands based on given conditions.

    :param config_filename: The name of the configuration file to process.
    :param ignore_lines: A list of keywords to ignore in the configuration file. Default is None.
    :param ignore_exclamation: If True, ignore lines that start with '!'. Default is True.
    :param strip_lines: If True, strip spaces at the beginning and end of lines. Default is False.
    :param delete_empty_lines: If True, delete empty lines from the result. Default is True.
    :return: A list of commands from the processed configuration file.
    """
    results = []  # List to store the filtered lines

    # Open the configuration file with a context manager
    with open(config_filename) as file:
        # Loop through each line in the file
        for line in file:
            # Strip lines if the flag is set
            if strip_lines:
                line = line.strip()  # Remove leading/trailing spaces
            else:
                line = line.rstrip()  # Only remove trailing spaces

            # Ignore empty lines if the flag is set
            if delete_empty_lines and not line:
                continue

            # Ignore lines starting with '!' if the flag is set
            if ignore_exclamation and line.startswith("!"):
                continue

            # Ignore lines containing any keywords from ignore_lines
            if ignore_lines and any(keyword in line for keyword in ignore_lines):
                continue

            # If none of the above conditions are met, add the line to the results
            results.append(line)

    return results

