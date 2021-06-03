# Python version 3.8
import sys
from random import sample, randint
from timeit import default_timer


def quickSort(inputArray, start, end):
    if start < end:
        pivotIndex = partition(inputArray, start, end)
        quickSort(inputArray, start, pivotIndex - 1)
        quickSort(inputArray, pivotIndex + 1, end)


def partition(inputArray, start, end):
    # Choosing pivot from first element of the input range
    pivot = inputArray[end]
    i = start - 1
    for j in range(start, end):
        if inputArray[j] < pivot:
            i += 1
            inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
    inputArray[i + 1], inputArray[end] = inputArray[end], inputArray[i + 1]
    return i + 1


def countingSort(inputArray, maxElement):
    print(f'Array before counting sort: {inputArray}\n')
    countingArr = [0] * (maxElement + 1)
    for element in inputArray:
        countingArr[element] += 1
    print(f'Counting array is: {countingArr}')
    for index in range(len(countingArr)):
        if index != 0:
            countingArr[index] += countingArr[index - 1]
    print(f'Counting array after sum of previous counts: {countingArr}')
    outputArray = [0] * len(inputArray)
    for index, element in enumerate(reversed(inputArray)):
        outputArray[countingArr[element] - 1] = element
        countingArr[element] -= 1
    print(f'Array after counting sort: {outputArray}')


def createArray(count, maximum):
    elementCount = randint(count + 1, count + 1000)
    randomArray = []
    for integer in range(elementCount):
        randomArray.append(randint(0, maximum))
    return randomArray


array = createArray(1000, 9999)
maximumInteger = max(array)
timerStart = default_timer()
countingSort(array, maximumInteger)
timerEnd = default_timer()
print(f'Runtime of counting sort is: {timerEnd - timerStart} seconds')
timerStart = default_timer()
quickSort(array, 0, len(array) - 1)
timerEnd = default_timer()
print(f'Runtime of quick sort is: {timerEnd - timerStart} seconds')
