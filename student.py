# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house, patronous):
#         if not name:
#             raise ValueError("Missing Value")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name 
#         self.house = house
#         self.patronous = patronous

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronous:
#             case "Stag":
#              return "🦌"
#             case "Otter":
#                return "🦦"
#             case "Jack":
#                 return "🐕"
#             case _:
#                 return "🪄"

# def main():
#     student = get_student()
#     print("Expecto Patronum")
#     print(student.charm())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronous = input("Patronous: ")
#     return Student(name, house, patronous)
    
# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self, name, house):
        self.name = name 
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    # Getter
    @property
    def name(self):
        return self._name
    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Value")
        self._name = name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    
if __name__ == "__main__":
    main()