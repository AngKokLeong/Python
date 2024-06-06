
number_list: list[int] = []

for index in range(1, 11):
    number: int = input("Enter number {0:d}: ".format(index))
    
    if number.isnumeric() == True:
        number_list.append(int(number))


sorted_number_list: list[int] = number_list.copy()
sorted_number_list.sort(reverse=True)

print("Maximum of the numbers is {0:d}".format(sorted_number_list[0]))
print("Minimum of the number is {0:d}".format(sorted_number_list[-1]))

print("The original list is {0}".format(number_list))
print("The sorted list in reverse order is {0}".format(sorted_number_list))