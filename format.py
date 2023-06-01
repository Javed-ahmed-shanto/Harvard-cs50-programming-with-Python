import re

name = input("What's your name?").strip().title()

if match := re.search(r"^(.+), *(.+)$", name): # := walruss operator where if and assigning at the same time
    name = match.group(2) + " " + match.group(1)

print(f"hello, {name}")