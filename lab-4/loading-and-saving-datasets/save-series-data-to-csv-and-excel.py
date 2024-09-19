import numpy
import pandas

myseries: pandas.Series = pandas.Series([1.0, 3.0, 5.0, numpy.NaN, 6.0, 8.0])

print(myseries)

myseries.to_csv("../dataset/myseries.csv")

myseries.to_excel("../dataset/myseries.xlsx")
