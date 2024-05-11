# The comparisons of Bubble Insertion and Selection sorts are in this file
import numpy as np
import time

def bubbleSort(numbersArray):
    for i in range(0, len(numbersArray) - 1):
        for j in range(i, len(numbersArray)):
            if numbersArray[j] < numbersArray[i]:
                numbersArray[j], numbersArray[i] = numbersArray[i], numbersArray[j]

def selectionSort(numbersArray):
    for i in range(len(numbersArray) - 1):
        min_index = i
        for j in range(i + 1, len(numbersArray)):
            if numbersArray[j] < numbersArray[min_index]:
                min_index = j  
        numbersArray[i], numbersArray[min_index] = numbersArray[min_index], numbersArray[i]

def insertionSort(numbersArray):
    for i in range(1, len(numbersArray)):  # Iterate over the array starting from the second element
        key = numbersArray[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < numbersArray[j]:  # Move elements greater than key one position ahead
            numbersArray[j + 1] = numbersArray[j]  # Shift elements to the right
            j -= 1
        numbersArray[j + 1] = key  # Insert the key in the correct position


SPN = 0 # Areviation for "Smallest Possible Number"
BPN = 10000 # Abreviation for "Biggest Possible Number"
AOGN = 100 # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

numbersArray = np.random.randint(SPN, BPN, AOGN)
#numbersArray = np.random.rand(AOGN)

array1 = numbersArray.copy()
array2 = numbersArray.copy()
array3 = numbersArray.copy()

startTime = time.time()
bubbleSort(array1)
endTime = time.time()
resultTime = endTime - startTime
print("The time that was needed for Bubble Sort to finish sorting is {:.8f}"
.format(resultTime))



startTime = time.time()
selectionSort(array2)
endTime = time.time()
resultTime = endTime - startTime
print("The time that was needed for Selection Sort to finish sorting is {:.8f}"
      .format(resultTime))



startTime = time.time()
insertionSort(array3)
endTime = time.time()
resultTime = endTime - startTime
print("The time that was needed for Insertion Sort to finish sorting is {:.8f}"
      .format(resultTime))