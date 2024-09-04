import pandas
import numpy


pandas_series_with_default_inde: pandas.Series = pandas.Series([1.0, 3.0, 5.0, numpy.nan, 6.0, 8.0])

print(pandas_series_with_default_inde)
print(pandas_series_with_default_inde.dtype)