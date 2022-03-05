response = 1

while response != 0:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print("a = ", a)
    #
    #
    #
    response = int(input("Enter an integer (\"0 to stop\"): "))
