# -*- coding: utf-8 -*-
"""
Завдання 6.6b

Зробити копію скрипта завдання 6.6a.
Доповнити скрипт: якщо адреса була введена неправильно, запитати адресу знову.

Якщо адреса неправильна, виводьте повідомлення: 'Wrong IP address'.
Повідомлення "Wrong IP address" має виводитися лише один раз після кожного
введення адреси, навіть якщо кілька пунктів перевірки адреси не виконано
(приклад виведення нижче).

Приклад виконання скрипту:
$ python task_6_6b.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: a.a.a
Wrong IP address
Enter IP address: 10.1.1.1.1
Wrong IP address
Enter IP address: 500.1.1.1
Wrong IP address
Enter IP address: a.1.1.1
Wrong IP address
Enter IP address: 50.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: 10.a.1.1.1
Wrong IP address
Enter IP address: 255.255.255.255
local broadcast

"""
while True:
    ip = input("Enter IP address: ")

    octets = ip.split(".")

    is_valid = True

    if len(octets) != 4:
        is_valid = False
    else:
        for octet in octets:
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                is_valid = False
                break

    if not is_valid:
        print("Wrong IP address")
    else:
        first_octet = int(octets[0])

        if first_octet == 0:
            print("unassigned")
        elif first_octet == 255 and all(int(octet) == 255 for octets in octets):
            print("local broadcast")
        elif 1 <= first_octet <= 223:
            print("unicast")
        elif 224 <= first_octet <= 239:
            print("multicast")
        else:
            print("unused")
        break
