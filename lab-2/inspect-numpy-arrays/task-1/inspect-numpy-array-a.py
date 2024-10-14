import numpy


float_ndarray: numpy.ndarray = numpy.array([1.55, 1.73, 1.9, 1.72, 1.66, 1.8])
tuple_ndarray: numpy.ndarray = numpy.array([
    ('red', 'green', 'yellow', 'blue'),
    (True, False, False, True),
    ('2017-10-01', '2017-11-11', '2917-12-23', '2018-03-31')
])

integer_tuple_ndarray: numpy.ndarray = numpy.array([
    [
        (10, 9, 8, 7),
        (6, 5, 4, 3)
    ],
    [
        (1,2,3,4),
        (5,6,7,8)
    ]
])

data_1_ndarray: numpy.ndarray = numpy.loadtxt("../../Lab2_Dataset/data1.txt", delimiter=",", dtype=[("asd",'<U12'), ("ds",'<U12'), ("qwe",'<U12'),("zxc",'<U12')])



print("Size")
print(float_ndarray.size)
print(tuple_ndarray.size)
print(integer_tuple_ndarray.size)
print(data_1_ndarray.size)

print("")

print("shape")
print(float_ndarray.shape)
print(tuple_ndarray.shape)
print(integer_tuple_ndarray.shape)
print(data_1_ndarray.shape)

print("")

print("len")
print(len(float_ndarray))
print(len(tuple_ndarray))
print(len(integer_tuple_ndarray))
print(len(data_1_ndarray))

print("")

print("ndim")
print(float_ndarray.ndim)
print(tuple_ndarray.ndim)
print(integer_tuple_ndarray.ndim)
print(data_1_ndarray.ndim)

