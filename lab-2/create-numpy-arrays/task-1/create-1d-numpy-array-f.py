import numpy, random 

twenty_random_number_numpy_array = numpy.array([])

for index in map(lambda x: random.randrange(100, 200), range(0, 20)):
    twenty_random_number_numpy_array = numpy.append(twenty_random_number_numpy_array, index)

print(twenty_random_number_numpy_array)