import pandas
import numpy

mydf: pandas.DataFrame = pandas.read_excel("../dataset/singstats_maritalstatus_2006_to_2016.xlsx").set_index("Variables")

df_index123: pandas.DataFrame = mydf.iloc[:, 0:3]

print("***Index 1,2,3***")
print("")
print(df_index123)

df_last5cols: pandas.DataFrame = mydf.iloc[:, -5:]


print("")
print("***Last 5 cols ***")
print("")
print(df_last5cols)