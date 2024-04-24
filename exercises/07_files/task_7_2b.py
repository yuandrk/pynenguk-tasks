# -*- coding: utf-8 -*-
"""
Завдання 7.2b

Скопіювати код із завдання 7.2a та переробити його: замість виведення на стандартний потік виведення, скрипт повинен записати отримані рядки у файл.

Імена файлів потрібно передавати як аргументи скрипту:
1 аргумент ім'я конфігураційного файлу з якого читаються рядки
2 аргумент ім'я файлу, в який будуть записані рядки

Приклад роботи завдання:
$ python task_7_2b.py config_sw1.txt new_config.txt

При цьому повинні бути відфільтровані рядки зі словами, які містяться в списку
ignore та рядки, що починаються на '!'.
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

output_filename = sys.argv[2]



# Use a context manager for file handling
with open(input_filename) as file, open(output_filename, 'w') as w:
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
        w.write(line + '\n')
