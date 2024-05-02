import numpy as np
import time

SPN = 0 # Abreviation for "Smallest Possible Number"
BPN = 10000 # Abreviation for "Biggest Possible Number"
AOGN = 10000 # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

#numbersArray = np.random.randint(SPN, BPN, AOGN)
numbersArray = np.random.rand(AOGN)

def insertionSort(numbersArray):
    for i in range(1, len(numbersArray)):  # Iterate over the array starting from the second element
        key = numbersArray[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < numbersArray[j]:  # Move elements greater than key one position ahead
            numbersArray[j + 1] = numbersArray[j]  # Shift elements to the right
            j -= 1
        numbersArray[j + 1] = key  # Insert the key in the correct position
            
startTime = time.time()

insertionSort(numbersArray)

endTime = time.time()

timeElapsed = endTime - startTime
print("The time it took to sort {0} numbers was {1:.4f} seconds".format(AOGN, timeElapsed))