import pandas
import numpy

df_1: pandas.DataFrame = pandas.read_csv("../dataset/schoolinfo_1a.csv", header=0)
df_2: pandas.DataFrame = pandas.read_csv("../dataset/schoolinfo_2a.csv", header=0)

print("***** df1 ******")

df_1.set_index("school_name", inplace=True)

print("")
print("")
print("Columns in df1 --> " + str(df_1.columns))
print(df_1[:2])




print("***** df2 ******")
df_2.set_index("school_name", inplace=True)

print("")
print("")
print("Columns in df2 --> " + str(df_2.columns))

print(df_2[:2])


print("***** After concatenating the two DataFrame objects ******")
print("")

df_all: pandas.DataFrame = pandas.concat([df_1, df_2]).apply(lambda x: )

print("Columns in df_all --> " + str(df_all.columns))

print(df_all)