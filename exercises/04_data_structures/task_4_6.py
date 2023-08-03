# -*- coding: utf-8 -*-
"""
Завдання 4.6

Обробити рядок ospf_route та вивести інформацію на стандартний потік виведення у вигляді:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для цього використовувати шаблон template і підставити значення з рядка
ospf_route. Значення рядка ospf_route треба отримати за допомогою Python.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

sop = ospf_route.split()
filtered_sop = []

for x in sop:
    if x != "via":
        filtered_sop.append(x)

# Split filtered_ospf_route string into individual elements
prefix, ad_metric, next_hop, last_update, outbound_interface = filtered_sop

# Remove the square brackets and commas from ad_metric
ad_metric = ad_metric.strip('[]')

template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

print(template.format(prefix, ad_metric, next_hop.strip(','), last_update.strip(','), outbound_interface))