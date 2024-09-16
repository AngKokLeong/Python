import pandas
import numpy

df_csv: pandas.DataFrame = pandas.read_csv("../dataset/income.csv",header=0, delimiter=";")


print(df_csv.shape)

# There are 5 rows and 11 columns

print(df_csv.dtypes)

# The GEOID and State column are object datatype
# all other columns are int64

