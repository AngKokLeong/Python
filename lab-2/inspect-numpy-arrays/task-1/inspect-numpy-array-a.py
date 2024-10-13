import numpy


float_ndarray: numpy.ndarray = [1.55, 1.73, 1.9, 1.72, 1.66, 1.8]
tuple_ndarray: numpy.ndarray = [
    ('red', 'green', 'yellow', 'blue'),
    (True, False, False, True),
    ('2017-10-01', '2017-11-11', '2917-12-23', '2018-03-31')
]

integer_tuple_ndarray: numpy.ndarray = [
    [
        (10, 9, 8, 7),
        (6, 5, 4, 3)
    ],
    [
        (1,2,3,4),
        (5,6,7,8)
    ]
]


data_1_ndarray: numpy.ndarray = numpy.loadtxt("../../Lab2_Dataset/data1.txt")



print(float_ndarray)

print(tuple_ndarray)

print(integer_tuple_ndarray)

print(data_1_ndarray)