import pandas

mydf: pandas.DataFrame = pandas.read_csv("../dataset/irascollectionbytaxtypemelt.csv", header=0)


print("***** Before MELT ******")
print("")
print(mydf.iloc[:5, :6])


print("")

print("***** After MELT ******")
print("")

melt_dataframe: pandas.DataFrame = mydf.melt(id_vars=["tax_type"], var_name="financial_year", value_name="tax_collected")
print(melt_dataframe[["financial_year", "tax_type", "tax_collected"]].iloc[:5])