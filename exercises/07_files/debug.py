from pprint import pprint
import sys 


input_filename = sys.argv[1]


with open(input_filename) as f:
    output = f.read()

result = {}
sections = output.split("!")
for section in sections:
    section = section.strip()
    if section.startswith("interface"):
        for line in section.split("\n"):
            if line.startswith("interface"):
                intf = line.split()[-1]
                result[intf] = []
            else:
                result[intf].append(line.strip())
pprint(result)
