import numpy
import pandas

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
random_number_generator = numpy.random.default_rng()
myseries: pandas.Series = pandas.Series(random_number_generator.random(size=1000))


random_numeric_values_between_10_to_100: pandas.Series = pandas.Series(random_number_generator.integers(10, 100, size=1000, endpoint=True))

print(myseries.head(10))

print(myseries.tail(20))

