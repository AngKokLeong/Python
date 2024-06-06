list_students1: list[str] = ['Ann', 'Brandon', 'Christine', 'Daniel', 'Eileen', 'Francis', 'Gloria', 'Henry', 'Irene', 'John']
list_weights1: list[int] = [45, 90, 52, 75, 48, 65, 60, 85, 49, 100]
list_heights1: list[float] = [1.54, 1.85, 1.66, 1.75, 1.58, 1.71, 1.68, 1.78, 1.62, 1.88]

list_students2: list[str] = []
list_weights2: list[int] = []
list_heights2: list[float] = []

for index in range(1, 6):

    input_name: str = input("Enter student {0:d}'s name: ".format(index))
    
    input_weight: str = input("Enter student {0:d}'s weight: ".format(index))

    input_height: str = input("Enter student {0:d}'s height: ".format(index))

    
    list_students2.append(input_name)
    list_weights2.append(int(input_weight))
    list_heights2.append(float(input_height))


list_students_all: list[str] = []
list_weights_all: list[int] = []
list_heights_all: list[float] = []

#Combine data into one list for each category
list_students_all.extend(list_students1)
list_students_all.extend(list_students2)

list_weights_all.extend(list_weights1)
list_weights_all.extend(list_weights2)

list_heights_all.extend(list_heights1)
list_heights_all.extend(list_heights2)


list_bmis_all: list[float] = []

for index in range(0, len(list_students_all)):

    weight: int = list_weights_all[index]
    height: float = list_heights_all[index]

    bmi: float = (weight / (height * height))

    list_bmis_all.append(bmi)


print("Here's the BMI's of all {0:d} students {1}".format(len(list_students_all), list_bmis_all))



#Find out the highest and lowest bmi


sorted_list_bmis_all = []
sorted_list_bmis_all.extend(list_bmis_all)
sorted_list_bmis_all.sort()

highest_bmi: float = sorted_list_bmis_all[-1]
lowest_bmi: float = sorted_list_bmis_all[0]

highest_bmi_index: int = list_bmis_all.index(highest_bmi)
lowest_bmi_index: int = list_bmis_all.index(lowest_bmi)

highest_bmi_student: str = list_students_all[highest_bmi_index]
lowest_bmi_student: str = list_students_all[lowest_bmi_index]

print("")

print("{0:s} has the highest bmi of {1:f}".format(highest_bmi_student, highest_bmi))
print("{0:s} has the lowest bmi of {1:f}".format(lowest_bmi_student, lowest_bmi))
