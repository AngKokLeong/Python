import pandas

mydf: pandas.DataFrame = pandas.read_csv("../dataset/irascollectionbytaxtype.csv", header=0)

print("***** Before PIVOT ******")

print(mydf[:5])

print("")

print("***** After PIVOT ******")

pivot_dataframe: pandas.DataFrame = mydf.pivot(index="tax_type", columns="financial_year", values="tax_collected")

print(pivot_dataframe.iloc[:5,:5])
