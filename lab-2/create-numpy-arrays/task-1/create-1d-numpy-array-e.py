import numpy, random

random.seed()
#https://docs.python.org/3/library/random.html

random_decimal_array = numpy.array([])
for index in map(lambda x: random.randrange(0, 10)/10, range(0, 10)):
    random_decimal_array = numpy.append(random_decimal_array, values=index)

print(random_decimal_array)


