
row = int(input("Enter a number for rows : "))

if row > 1:
    for i in range(row):
        print(" " * (row - i - 1) + "#" * (2 * i + 1))
    
    for i in range(row - 2, -1, -1):
        print(" " * (row - i - 1) + "#" * (2 * i + 1))
else:
    print("The number must more than 1")