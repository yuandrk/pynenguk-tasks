# -*- coding: utf-8 -*-
"""
Завдання 6.2

Замінити у рядку line всі голосні у нижньому регістрі на голосні у верхньому
регістрі. Змінений рядок записати в змінну result і вивести стандартний потік
виведення (stdout) за допомогою print.

Приклад роботи завдання:
$ python task_6_2.py
GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s

Рядок line не можна змінювати вручну, всі зміни треба зробити за допомогою
Python.
"""

line = "Guido van Rossum began working on Python in the late 1980s"

vowels = "aeioyu"  # Define lowercase vowels
result = ""  # Initialize an empty string to store the result

# Loop through each character in the 'line' string
for char in line:
    if char in vowels:  # Check if the character is a lowercase vowel
        result += char.upper()  # If yes, convert it to uppercase and add to 'result'
    else:
        result += char  # If not a vowel, add the character as is to 'result'

print(result)  # Print the modified string