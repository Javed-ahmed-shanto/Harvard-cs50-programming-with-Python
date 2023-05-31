def main():
    name = input("whats your name? ").strip().title()
    print(hello(name))


def hello(to = "world"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()

# print("hello, world")