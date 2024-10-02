import pandas

mydf: pandas.DataFrame = pandas.read_csv("../dataset/irascollectionbytaxtype.csv", header=0)

mydf.set_index(["financial_year", "tax_collected"], inplace=True)


print("***** The first 10 rows of the IRAS collection from 2002 to 2016 ******")
print("")

print(mydf[:10])

print("")
print("***** Top collections by year ******")

print("")

mydf.sort_index(level=["tax_collected"], ascending=[False], inplace=True)

print(mydf[:10])


print("")

print("***** Bottom collections by year ******")

print("")


print(mydf[-10:])

print("")

mydf.sort_index(level=["financial_year","tax_collected"], ascending=[True,False], inplace=True)

print("*****  by year ******")

print("")

print(mydf)