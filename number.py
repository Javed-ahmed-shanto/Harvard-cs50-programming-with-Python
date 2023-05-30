def main():
    x = get_int("what's x?")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # return x
            # break
        except ValueError:
            pass

main()