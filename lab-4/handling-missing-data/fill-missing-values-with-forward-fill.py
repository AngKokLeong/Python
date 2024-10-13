import pandas
import numpy

mydf: pandas.DataFrame = pandas.read_csv("../dataset/hdbresaleindex_missing.csv", header=0)

df_missing: pandas.DataFrame = mydf.isnull()

missing_data_index_list: list = df_missing[df_missing["index"] == True].index.to_list()

print("**** Rows with missing values -- df_missing ****")
print("")
print(mydf.iloc[missing_data_index_list])

print("")

print("***** Dataset after forward fill operation *****")
print("")

mydf.fillna(method='ffill', inplace=True)

print(mydf[:12])