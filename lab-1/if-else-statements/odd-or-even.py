print("*" * 50)
print("Section 6 - if-else statement")
print("*" * 50)

print("")

data:str = input("Enter a number: ")

print("")

if data.isnumeric() == False:
    print("You did not enter a number")
else:
    numeric_data: int = int(data)

    if numeric_data % 2 == 0:
        print("{0:d} is even".format(numeric_data))
    else:
        print("{0:d} is odd".format(numeric_data))

