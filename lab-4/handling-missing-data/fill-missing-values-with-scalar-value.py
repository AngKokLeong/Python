import pandas
import numpy

mydf: pandas.DataFrame = pandas.read_csv("../dataset/hdbresaleindex_missing.csv", header=0)

missing_data_dataframe: pandas.DataFrame = mydf.isnull()

filtered_missing_data_dataframe: pandas.DataFrame = missing_data_dataframe[missing_data_dataframe["index"] == True]

print("**** Rows with missing values -- df_missing ****")
print("")

df_missing: pandas.DataFrame = mydf.iloc[filtered_missing_data_dataframe.index]

print(df_missing)

print("")

print("***** Dataset after scalar fill operation *****")
print("")

mydf.fillna(value=50.0, inplace=True)

print(mydf[:12])