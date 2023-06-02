import re

url = input("URL: ").strip()



if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-z0-9_]+)", url, re.IGNORECASE): # ? makes optional the digit before ?

    print(f"Username:", matches.group(1))