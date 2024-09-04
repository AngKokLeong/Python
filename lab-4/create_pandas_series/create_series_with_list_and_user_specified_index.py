import pandas
import numpy

user_defined_index = pandas.Index(["a", "b", "c", "d", "e", "f"])

data = pandas.Series([1.0, 3.0, 5.0, numpy.nan, 6.0, 8.0], index=user_defined_index)

print(data)
print(data.dtype)