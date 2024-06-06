import random
from typing import Tuple

original_list: list[int] = []

for random_number in range(100):
    original_list.append(random.randint(1, 1000))


def oddandeven(numbers_list: list[int]) -> Tuple[list[int], list[int]]:
    
    odd_number_list: list[int] = []
    even_number_list: list[int] = []

    for number in numbers_list:

        if number % 2 == 0:
            even_number_list.append(number)
        else:
            odd_number_list.append(number)

    return even_number_list, odd_number_list


even_numbers, odd_numbers = oddandeven(original_list)

print("Original List: " + str(original_list))

print("")

print("Odd: " + str(odd_numbers))

print("")

print("Even: " + str(even_numbers))