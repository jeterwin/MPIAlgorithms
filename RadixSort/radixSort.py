import numpy as np
import time
 
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
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

SPN = 0 # Abreviation for "Smallest Possible Number"
BPN = 1000000 # Abreviation for "Biggest Possible Number"
AOGN = 10000  # Abreviation for "Amount Of Generated Numbers"
 
numbersArray = np.random.randint(SPN, BPN, AOGN)

startTime = time.time()

radixSort(numbersArray)
            
endTime = time.time()

timeElapsed = endTime - startTime

print("The time it took to sort {0} numbers was {1:.8f} seconds".format(AOGN, timeElapsed))