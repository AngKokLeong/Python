import numpy, random

random.seed()

two_d_array = []


for row in range(0, 4):
    new_row: list = []
    for index in map(lambda x: random.randrange(1,6), range(0, 8)):
        new_row.append(index)

    two_d_array.append(new_row)


two_d_numpy_array: numpy.ndarray = numpy.array(two_d_array)

print(two_d_numpy_array)
