# -*- coding: utf-8 -*-
"""
Завдання 4.5

З рядків command1 та command2 одержати список VLANів, які є і в команді
command1 і в команді command2 (перетин). Елементи списку мають бути
відсортовані за зростанням.

В даному випадку, результатом має бути такий список: ['1', '3', '8']

Записати підсумковий список у змінну result (саме ця змінна перевірятиметься у
тесті). У списку result влада повинна бути відсортована за зростанням номерів.
Для отримання підсумкового списку не можна видаляти конкретні vlanи вручну.

Отриманий список результату вивести на стандартний потік виведення (stdout) за
допомогою print.

Це завдання можна виконати без використання циклів і умов.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans_command1 = set(command1.split()[-1].split(','))
vlans_command2 = set(command2.split()[-1].split(','))

result = sorted(list(vlans_command1 & vlans_command2))

print(result)

# import re

# command1 = "switchport trunk allowed vlan 1,2,3,5,8"
# command2 = "switchport trunk allowed vlan 1,3,8,9"

# com = command1 + " " + command2 

# result = []

# numbers = re.findall(r'\d+', com)

# numbers = set(numbers)
# numbers = [int(num) for num in numbers]
# result = list(numbers)
# numbers.sort()

# print(numbers)