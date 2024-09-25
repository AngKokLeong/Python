import numpy
import pandas

mydf: pandas.DataFrame = pandas.read_excel("../dataset/singstats_maritalstatus.xlsx").set_index("Variables")

print("*** Data in 1980 column ***")
print(mydf.iloc[:, 0])

number_of_rows_with_values_more_than_500k: int = 0
number_of_rows_with_values_less_than_500k: int = 0

for element in mydf.iloc[:, 0]:
    if element > 500000:
        number_of_rows_with_values_more_than_500k += 1
    elif element <= 500000:
        number_of_rows_with_values_less_than_500k += 1

print("")
print("Number of rows more than 500k is " + str(number_of_rows_with_values_more_than_500k))
print("Number of rows less than 500k is " + str(number_of_rows_with_values_less_than_500k))