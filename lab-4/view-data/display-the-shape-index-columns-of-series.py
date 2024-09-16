import numpy
import pandas

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
random_number_generator = numpy.random.default_rng()
myseries: pandas.Series = pandas.Series(random_number_generator.random(size=1000))



print(myseries.shape)

print(myseries.index)

print(myseries.values)

print(myseries.count())

print(myseries.describe())