import numpy as np

arr_2 = np.random.randint(1,20, (3,5))

print("**Before Sorting**")
print(arr_2)

print()
print()

print("**After Sorting**")
sorted_arr_2 = np.sort(arr_2, axis=0)
print(sorted_arr_2)
