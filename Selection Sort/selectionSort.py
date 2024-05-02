import numpy as np
import time

SPN = 0 # Abreviation for "Smallest Possible Number"
BPN = 10000 # Abreviation for "Biggest Possible Number"
AOGN = 5 # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

numbersArray = np.random.randint(SPN, BPN, AOGN)
#numbersArray = np.random.rand(AOGN)

def selectionSort(numbersArray):
    print(len(numbersArray))
    for i in range(len(numbersArray) - 1):
        min_index = i
        for j in range(i + 1, len(numbersArray)):
            if numbersArray[j] < numbersArray[min_index]:
                min_index = j  
        numbersArray[i], numbersArray[min_index] = numbersArray[min_index], numbersArray[i]

startTime = time.time()

selectionSort(numbersArray)
print(numbersArray)
endTime = time.time()
timeElapsed = endTime - startTime
print("The time it took to sort {0} numbers was {1:.4f} seconds".format(AOGN, timeElapsed))