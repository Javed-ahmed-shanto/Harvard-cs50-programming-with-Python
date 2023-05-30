def main():
    number  = get_number()
    mewo(number)

def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n

def mewo(n):
    for _ in range (n):
        print("mewo")

main()