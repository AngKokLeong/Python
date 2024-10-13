import pandas

mydf: pandas.DataFrame = pandas.read_csv("../dataset/hdbresaleindex_missing.csv", header=0)

mydf.set_index("quarter", inplace=True)

df_missing: pandas.DataFrame = mydf.isnull()

filtered_df_missing: pandas.DataFrame = df_missing[df_missing["index"] == True]


print("**** Rows with missing values -- df_missing ****")
print("")
print(mydf.loc[filtered_df_missing.index])

print("")
print("***** Dataset after backward fill operation *****")
print("")
mydf.fillna(method='bfill', inplace=True)

print(mydf)