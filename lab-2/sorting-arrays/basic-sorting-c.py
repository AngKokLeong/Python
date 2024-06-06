import numpy as np

arr_3 = np.random.randint(100,200, (2,5))

print("**Before sorting - original array **")
print(arr_3)

print()
print()

print("**After calling sort method - original array **")
sorted_original_array = np.sort(arr_3, axis=0)
print(sorted_original_array)

print()
print()

print("**After calling sort method - copy of sorted array **")
copy_of_sorted_original_array = np.sort(sorted_original_array, axis=1)
print(copy_of_sorted_original_array)