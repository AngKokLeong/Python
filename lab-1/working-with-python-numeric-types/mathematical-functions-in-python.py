import math
from fractions import Fraction

n1: float = float(input("Enter number 1: "))
n2: float = float(input("Enter number 2: "))
n3: float = float(input("Enter number 3: "))
n4: float = float(input("Enter number 4: "))

n1_squareroot: float = math.sqrt(n1)

print("The square root of {0} is {1}".format(n1, n1_squareroot))

print("The ceiling value of n1_squareroot is {0}".format(math.ceil(n1_squareroot)))

print("")

n2_times_pi: float = n2 * math.pi

print("The truncated value of n2_times_pi {0}".format(n2_times_pi))

print("")

n3_powerof_n1: float = n3 ** n1

print("{0} to the power of {1} is {2}".format(n3, n1, n3_powerof_n1))
print("The floor value of n3_powerof_n1 is {0}".format(math.floor(n3_powerof_n1)))

print("")

n4_factorial: int = math.factorial(int(n4))
n4n3 = n4_factorial / n3

print("{0:f} factorial is {1:d}".format(n4, n4_factorial))
print("{0:d} divided by {1:f} is {2:.11f}".format(n4_factorial, n3, n4n3))


print("The fractional value of the result is {0}".format(math.modf(n4n3)[0]))
print("The integer value of the result is {0}".format(math.modf(n4n3)[1]))