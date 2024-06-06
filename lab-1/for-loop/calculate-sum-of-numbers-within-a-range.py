
print("This program prints the sum of a range of number from x to y")

print("For example, if x is 10 and y is 50, the program will print the sum of numbers from 10 to 50")

x: str = input("Please enter the value of x: ")
y: str = input("Please enter the value of y: ")

if (x.isnumeric() == True and y.isnumeric() == True):
    if int(x) > 0 and int(y) > 0:
        if int(y) > int(x):
            sum_of_numbers: int = 0    
            for number in range(int(x), int(y) + 1 ):
                sum_of_numbers += number
            
            print("The sum of numbers between {0:s} and {1:s} is {2:d}".format(x, y, sum_of_numbers))
            exit()

        else:
            print("y is less than x")

    else:
        print("One or more of your inputs are not greater than zero")

else:
    print("One or more of your inputs are not numeric!")

print("Unable to continue. Program terminated.")
