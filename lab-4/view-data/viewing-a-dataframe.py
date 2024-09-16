import pandas
import numpy

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
random_number_generator = numpy.random.default_rng()

random_numeric_values_between_10_to_100: pandas.Series = pandas.Series(random_number_generator.integers(10, 100, size=1000, endpoint=True))
zero_value_series: pandas.Series = pandas.Series(random_number_generator.integers(0, 1, size=1000))

stepping_value_list :list = []
for i in range(1000):
    stepping_value_list.append(i)

stepping_value_series: pandas.Series = pandas.Series(stepping_value_list)


mydf: pandas.DataFrame = pandas.DataFrame(
        {
            "Column A": random_numeric_values_between_10_to_100,
            "Column B": zero_value_series,
            "Column C": stepping_value_series
        }
        
    )


print(mydf.head(20))

print(mydf.tail(10))