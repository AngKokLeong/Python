import numpy
import pandas

df_xls: pandas.DataFrame = pandas.read_excel("../dataset/singstats_household.xlsx")

print(df_xls.shape)

print(df_xls.dtypes)