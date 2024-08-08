
row = int(input("Enter a number for rows : "))

if row > 1:
    for i in range(row):
        for j in range(row - i - 1):
            print(" ", end="")
        for k in range((2 * i) + 1):
            print("#", end="")
        print()

    for i in range(row):
        for j in range(i):
            print(" ", end="")
        for k in range(2 * (row - i) - 1):
            print("#", end="")
        print()
else:
    print("The number must more than 1")