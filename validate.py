# Regex | Regular Expression
import re

email = input("What's your email?").strip()

if re.search(r"^(\w|\s|.)+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE): # \w = word means alpha neumeric 
    print("valid")
else:
    print("Invalid")

