import re

string = input()

regex = r"(\@+|\#+)([a-z]{3,})(\@+|\#+)(\W*)(/+)([0-9]+)(/+)"

result = re.findall(regex, string)


for i in result:
    print(f"You found {i[5]} {i[1]} eggs!")










