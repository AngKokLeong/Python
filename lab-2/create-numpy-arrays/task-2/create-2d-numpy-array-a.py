import numpy

two_d_array = [[], []]

number_of_element: int = 0
current_row: int = 0

for index in range(1, 9):

    if number_of_element == 4:
        current_row = 1

    two_d_array[current_row].append(index)

    number_of_element = number_of_element + 1

numpy_2d_array = numpy.array(two_d_array)


print(numpy_2d_array)