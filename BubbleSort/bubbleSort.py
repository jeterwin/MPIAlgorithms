import numpy as np
import time

SPN = 0 # Areviation for "Smallest Possible Number"
BPN = 10000 # Abreviation for "Biggest Possible Number"
AOGN = 10000 # Abreviation for "Amount Of Generated Numbers"

# There was the need of abbreviating the names of the variables due to lack of space on
# displays

#numbersArray = np.random.randint(SPN, BPN, AOGN)
numbersArray = np.random.rand(AOGN)

startTime = time.time()

for i in range(0, len(numbersArray) - 1):
    for j in range(i, len(numbersArray)):
        if numbersArray[j] < numbersArray[i]:
            numbersArray[j], numbersArray[i] = numbersArray[i], numbersArray[j]
            
endTime = time.time()

timeElapsed = endTime - startTime
print("The time it took to sort {0} numbers was {1:.4f} seconds".format(AOGN, timeElapsed))