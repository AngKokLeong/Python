a: list[int] = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("The list elements are: {0}".format(a))

print("Items less than 5 are: ")
for number in a:
    if number < 5:
        print(number)