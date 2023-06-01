# Houses:
# Shanto, All
# harry, Gryffindor
# ron, Gryffindor
# Draco Malfoy, Slytherin

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().title().split(",") # as split sperates two things in here, we are sepearating in first[0] as name and second[1] as houses
#         print(f"{name} is in{house}")


# with open("students.csv") as file:
#     for line in file:
#         name, house = line.title().rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": ["home"]})/ or just (row)

# for student in sorted(students, key=lambda student: student["name"]): # Sorted using studnets names
#     print(f"{student['name']} is from {student['home']}")


# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})