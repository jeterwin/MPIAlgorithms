# The comparisons of Merge and Quick sort are in this file
import numpy as np
import time

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0 
    j = 0
    k = l
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


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


SPN = 0 # Areviation for "Smallest Possible Number"
BPN = 10000 # Abreviation for "Biggest Possible Number"
AOGN = 100000 # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

numbersArray = np.random.randint(SPN, BPN, AOGN)
#numbersArray = np.random.rand(AOGN)

array1 = numbersArray.copy()
array2 = numbersArray.copy()

startTime = time.time()
mergeSort(array1, 0, len(array1) - 1)
endTime = time.time()
resultTime = endTime - startTime
print("The time that was needed for Merge Sort to finish sorting is {:.8f}"
.format(resultTime))



startTime = time.time()
quicksort(array2, 0, len(array2) - 1)
endTime = time.time()
resultTime = endTime - startTime
print("The time that was needed for Quick Sort to finish sorting is {:.8f}"
      .format(resultTime))