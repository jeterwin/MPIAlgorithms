import numpy as np
import time

SPN = 0 # Abreviation for "Smallest Possible Number"
BPN = 1000000 # Abreviation for "Biggest Possible Number"
AOGN = 10000000  # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

#numbersArray = np.random.randint(SPN, BPN, AOGN)
numbersArray = np.random.uniform(SPN, BPN, AOGN)

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

startTime = time.time()

mergeSort(numbersArray, 0, len(numbersArray) - 1)

endTime = time.time()
timeElapsed = endTime - startTime
print("The time it took to sort {0} numbers was {1:.4f} seconds".format(AOGN, timeElapsed))