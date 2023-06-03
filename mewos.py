# class Cat:
#     MEOWS = 3

#     def mewo(self):
#         for _ in range(Cat.MEOWS):
#             print("mewo")

# cat = Cat()
# cat.mewo()


# def meow(n: int) -> None:  # Typehints
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meow(number)

# def meow(n: int) -> str:  # Typehints
#     """Meow n times. formal pythonic way"""
#     """ 
#     or like this.
#     :type n: int
#     :rtype: str
#     """
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help ="number of times to meow", type=int)
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")