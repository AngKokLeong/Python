import pandas


mydf: pandas.DataFrame = pandas.read_csv("../dataset/hdbresaleindex_missing.csv", header=0)

mydf.set_index("quarter", inplace=True)

mydf.rename(columns={"index": "resale_index"}, inplace=True)

print("**** First 5 rows of mydf ****")
print("")

print(mydf[:5])

print("")
print("**** Last 5 rows of mydf ****")
print("")

print(mydf[-5:])

print("")
print("**** Rows with missing values -- df_missing ****")
print("")

df_missing: pandas.DataFrame = mydf.isnull()

print(df_missing[df_missing["resale_index"] == True])

print("")

mean_of_resales_index_before_filling: float = mydf["resale_index"].mean()

print("Mean of resale index is " + str(mean_of_resales_index_before_filling))

print("")
print("***** Dataset after filling with mean of the rest of the values *****")
print("")

mydf.fillna(value=mean_of_resales_index_before_filling, inplace=True)

print(mydf[:13])