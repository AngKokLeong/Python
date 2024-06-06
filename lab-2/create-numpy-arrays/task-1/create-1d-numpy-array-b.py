import numpy

b: numpy.array = []

# refer to this documentation https://stackoverflow.com/questions/7267226/range-for-floats
for index in map(lambda x: x/10.0, range(12, 21, 2)):
    b.append(index)

print(b)