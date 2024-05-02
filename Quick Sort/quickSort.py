import numpy as np
import time

SPN = 0 # Abreviation for "Smallest Possible Number"
BPN = 1000000 # Abreviation for "Biggest Possible Number"
AOGN = 100  # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

#numbersArray = np.random.randint(SPN, BPN, AOGN)
numbersArray = np.random.uniform(SPN, BPN, AOGN)

def partition(array, low, high):
    pivot = array[high]
    pIndex = low - 1

    for i in range(low, high):
        if array[i] <= pivot:
            pIndex += 1
            array[pIndex], array[i] = array[i], array[pIndex]

    array[pIndex + 1], array[high] = array[high], array[pIndex + 1]
    return pIndex + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

startTime = time.time()

quicksort(numbersArray, 0, len(numbersArray) - 1)

endTime = time.time()

timeElapsed = endTime - startTime
print("The time it took to sort {0} numbers was {1:.4f} seconds".format(AOGN, timeElapsed))