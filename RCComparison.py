# The comparisons of Radix and Counting sorts are in this file
import numpy as np
import time

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


def countingSort(arr, exp1):
    n = len(arr)
 
    # The output array elements that will have sorted arr
    outputArray = [0] * (n)
 
    # initialize count array as 0
    countArray = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        countArray[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        countArray[i] += countArray[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        outputArray[countArray[index % 10] - 1] = arr[i]
        countArray[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = outputArray[i]
 
def radixSort(arr):
    # Find the maximum number to know the max number of digits
    max1 = max(arr)
 
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10


SPN = 0 # Areviation for "Smallest Possible Number"
BPN = 10000000 # Abreviation for "Biggest Possible Number"
AOGN = 10000 # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

numbersArray = np.random.randint(SPN, BPN, AOGN)
#numbersArray = np.random.rand(AOGN)

array1 = numbersArray.copy()
array2 = numbersArray.copy()


startTime = time.time()
radixSort(array1)
endTime = time.time()
resultTime = endTime - startTime
print("The time that was needed for Radix Sort to finish sorting is {:.8f}"
.format(resultTime))



startTime = time.time()
count_sort(numbersArray)
endTime = time.time()
resultTime = endTime - startTime
print("The time that was needed for Counting Sort to finish sorting is {:.8f}"
      .format(resultTime))