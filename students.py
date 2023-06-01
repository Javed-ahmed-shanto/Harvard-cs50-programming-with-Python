# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().title().split(",") # as split sperates two things in here, we are sepearating in first[0] as name and second[1] as houses
#         print(f"{name} is in{house}")

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.title().rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# def get_name(student):
#     return student["name"]

for student in sorted(students, key = lambda student: student["name"]): # Sorted using studnets names
    print(f"{student['name']} is in{student['house']}")