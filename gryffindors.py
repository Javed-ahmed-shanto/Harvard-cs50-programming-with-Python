# students = ["Hermione", "Harry", "Ron"]

# for i, student in enumerate(students):
#     print(i+1, student)

# students = ["Hermione", "Harry", "Ron"]

# gryffindors = { student: "Gryffindor" for student in students} # Dict comprehentation

# print(gryffindors)

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students] # List comprehentation

print(gryffindors)