def count_sort(input_array):
    # Finding the maximum element of input_array.
    M = max(input_array)
 
    # Initializing count_array with 0
    count_array = [0] * (M + 1)
 
    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1
 
    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    # Creating output_array from count_array
    output_array = [0] * len(input_array)
 
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
 
    return output_array

import numpy as np
import time

SPN = 0 # Abreviation for "Smallest Possible Number"
BPN = 10000 # Abreviation for "Biggest Possible Number"
AOGN = 10000000  # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays


numbersArray = np.random.randint(SPN, BPN, AOGN)

startTime = time.time()

count_sort(numbersArray)

endTime = time.time()

timeElapsed = endTime - startTime

print("The time it took to sort {0} numbers was {1:.8f} seconds".format(AOGN, timeElapsed))