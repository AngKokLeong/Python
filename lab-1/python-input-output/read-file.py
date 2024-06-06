
filepath: str = input("Enter the input filename: ")

file = open(filepath, "r")
file_content: list[str] = file.readlines()

print("{0:s} contains {1:d} numbers".format(filepath, len(file_content)))

total_sum:float = 0.0

for data in file_content:
    
    total_sum += float(data.strip('\n'))

print("The total sum of all the {0:d} numbers is {1:d}".format(len(file_content), int(total_sum)))
print("The average of all the numbers is {0:f}".format(total_sum / len(file_content)))
