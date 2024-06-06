
n1: int = int(input("Enter number 1: "))
n2: int = int(input("Enter number 2: "))
n3: int = int(input("Enter number 3: "))
n4: int = int(input("Enter number 4: "))

print("The four numbers are {0:d}, {1:d}, {2:d}, {3:d}".format(n1, n2, n3, n4))

add: int = n1+n2+n3+n4
print("Sum is {0:d}".format(add))


difference: int =  n1 - n4
print("Difference is {0:d}".format(difference))

product: int = n2 * n3
print("Product is {0:d}".format(product))

quotient: float = (n1 + n2) / (n3 + n4)
print("Quotient is {0:f}".format(quotient))

remainder: float = (n1 * n2)  / (n3 * n4)
print("Remainder is {0:f}".format(remainder))

powerl = n1 ** n2
print("Power is {0:d}".format(powerl))