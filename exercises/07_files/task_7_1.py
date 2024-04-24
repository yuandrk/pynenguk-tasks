# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обробити рядки з файлу ospf.txt і вивести інформацію щодо кожного рядка в
такому вигляді на стандартний потік виводу:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""

template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
""" 

with open("/home/yuandrk/github/pynenguk-tasks/exercises/07_files/ospf.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('[', '').replace(']', '').replace('O', ''.replace(',',''))  # Remove square brackets
        parts = line.split()  # Split the line into parts
        prefix = parts[0]
        ad_metric = parts[1]
        next_hop = parts[3].replace(',','')
        last_update = parts[4].replace(',','')
        outbound_interface = parts[5]

        print(template.format(prefix, ad_metric, next_hop, last_update, outbound_interface))
        
