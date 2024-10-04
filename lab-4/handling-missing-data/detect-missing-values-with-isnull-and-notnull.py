import pandas
import numpy


mydf: pandas.DataFrame = pandas.read_excel("../dataset/singstats_maritalstatus.xlsx")

mydf.set_index("Variables", inplace=True)

for column_name, series in mydf.items():
    
    #object
    #int64

    if series.dtype == object:
        mydf[column_name].replace('-', numpy.NaN, inplace=True)

print("***** Use isnull to see if a column or row contains data *****")        
print(mydf.isnull().iloc[:, :8])