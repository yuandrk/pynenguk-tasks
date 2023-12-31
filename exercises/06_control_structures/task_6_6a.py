# -*- coding: utf-8 -*-
"""
Завдання 6.6a

Зробити копію скрипта завдання 6.6.

Додати перевірку введеної IP-адреси.
Адреса вважається коректно заданою, якщо вона:
- складається з 4 чисел (а не літер чи інших символів)
- числа розділені точкою
- кожне число в діапазоні від 0 до 255

Якщо адреса неправильна, виводьте повідомлення: "Wrong IP address".  Якщо
адреса правильна, перевіряти та виводити тип адреси як у завданні 6.6.

Повідомлення "Wrong IP address" має виводитися лише один раз, навіть якщо
кілька пунктів вище не виконано.


Приклад виконання скрипту:
$ python task_6_6a.py
Enter IP address: 10.10.1.1
unicast

$ python task_6_6a.py
Enter IP address: 10.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: a.a.10.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.a.a
Wrong IP address

$ python task_6_6a.py
Enter IP address: 10,1,1,1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 500.1.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.1.1.1
Wrong IP address
"""
ip = input("Enter IP address: ")

# Розділяємо IP-адресу на октети
octets = ip.split(".")

# Перевіряємо, чи кожен октет є числом (в межах 0-255)
is_valid = True

if len(octets) != 4:
    is_valid = False
else:
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            is_valid = False
            break

# Виводимо повідомлення про помилку, якщо адреса неправильна
if not is_valid:
    print("Wrong IP address")
else:
    first_octet = int(octets[0])

    if first_octet == 0:
        print("unassigned")
    elif first_octet == 255 and all(int(octet) == 255 for octet in octets):
        print("local broadcast")
    elif 1 <= first_octet <= 223:
        print("unicast")
    elif 224 <= first_octet <= 239:
        print("multicast")
    else:
        print("unused")
