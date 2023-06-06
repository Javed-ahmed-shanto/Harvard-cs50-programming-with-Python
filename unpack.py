# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "Knuts") """ * usage for unpacking"""

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(**coins), "Knuts")  # ** used for dictionary unpacking

def f(*args, **kwargs):
    print("Positional: ", args)

f(100, 50, 25)