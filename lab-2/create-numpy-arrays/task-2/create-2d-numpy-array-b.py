import numpy

three_d_array = [[], [], []]

number_of_element: int = 0
current_row: int = 0

for index in map(lambda x: x/10 ,range(15, 100, 10)):
    
    if number_of_element % 3 == 0 and number_of_element > 0:
        current_row = current_row + 1

    three_d_array[current_row].append(index)

    number_of_element = number_of_element + 1

numpy_3d_array = numpy.array(three_d_array)


print(numpy_3d_array)