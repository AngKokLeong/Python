import numpy
import pandas



mydf: pandas.DataFrame = pandas.read_excel("../dataset/singstats_maritalstatus.xlsx")



df_1986: pandas.DataFrame = mydf[["Variables", "1986"]].set_index("Variables")
df_1986 = df_1986["1986"]

print("*** Only 1986 ***")
print(df_1986)



column_list: list = []
for element in mydf.columns:
    if element.startswith("198"):
        column_list.append(element)

column_list.insert(0, "Variables")


df_1980s: pandas.DataFrame = pandas.DataFrame(mydf[column_list]).set_index("Variables") 


print("")
print("*** All of 1980s ***")
print(df_1980s)