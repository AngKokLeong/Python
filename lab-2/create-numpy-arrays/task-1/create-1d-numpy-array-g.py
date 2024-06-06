import numpy, random

random.seed()

even_number_numpy_array: numpy.ndarray = numpy.array([])

number_of_even_numbers_created = 0

while number_of_even_numbers_created < 50:
    current_random_number: int = random.randrange(5,10)

    if current_random_number % 2 == 0:
        even_number_numpy_array = numpy.append(even_number_numpy_array, current_random_number)
        number_of_even_numbers_created = number_of_even_numbers_created + 1


print(even_number_numpy_array)