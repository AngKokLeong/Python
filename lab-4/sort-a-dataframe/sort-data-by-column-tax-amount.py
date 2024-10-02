import pandas

mydf: pandas.DataFrame = pandas.read_csv("../dataset/irascollectionbytaxtype.csv", header=0)

print("***** The first 10 rows of the IRAS collection from 2002 to 2016 ******")

print("")

print(mydf[:10])

print("")

print("***** Top 10 IRAS Collection ******")

print("")

print(mydf.sort_values(by="tax_collected", ascending=False)[:10])

print("***** Bottom 10 IRAS Collection ******")

print("")

print(mydf.sort_values(by="tax_collected", ascending=False)[-10:])