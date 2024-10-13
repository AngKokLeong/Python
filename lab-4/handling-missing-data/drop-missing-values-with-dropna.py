import pandas
import numpy

mydf: pandas.DataFrame = pandas.read_excel("../dataset/singstats_maritalstatus.xlsx")

mydf.set_index("Variables", inplace=True)


for column_name, series in mydf.items():

    if series.dtype == object:
        mydf[column_name].replace('-', numpy.NaN, inplace=True)


print("")
print("**** First 10 rows of original dataset ****")
print("")
print(mydf.iloc[:10, :7])



print("")
print("**** Remaining dataset after dropping columns with missing data ****")
print("")

print(mydf.dropna(axis='columns').iloc[:10, :6])