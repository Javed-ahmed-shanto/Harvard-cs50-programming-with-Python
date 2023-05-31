# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}")

# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

names = []

with open("names.txt") as file: # Default is read "r"
    for line in file:
        names.append(line.rstrip().title())

for name in sorted(names):
    print(f"hello, {name}")

# with open ("names.txt") as file:
#     for line in sorted(file):
#         print("hello, ", line.rstrip())