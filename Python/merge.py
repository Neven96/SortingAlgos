import math

compares = 0
swaps = 0

def sort(array):
    global compares
    global swaps
    mergesort(array)
    return array, compares, swaps

# Merge sort implementation for O(n*log(n))
def mergesort(array):
    global compares
    global swaps
    n = len(array)
    if n <= 1:
        compares = compares + 1
        return array
    i = math.floor(n/2)
    array1 = mergesort(array[0:i]) # Has to be i not i-1, or else it doubles elements in the list
    array2 = mergesort(array[i:n-1])

    return merge(array1, array2, array)

def merge(array1, array2, array):
    global compares
    global swaps
    i = 0
    j = 0
    a1 = len(array1)
    a2 = len(array2)

    while i < a1 and j < a2:
        compares = compares + 1
        if array1[i] < array2[j]:
            compares = compares + 1
            array[i+j] = array1[i]
            swaps = swaps + 1
            i += 1
        else:
            compares = compares + 1
            array[i+j] = array2[j]
            swaps = swaps + 1
            j += 1

    while i < a1:
        compares = compares + 1
        array[i+j] = array1[i]
        swaps = swaps + 1
        i += 1

    while j < a2:
        compares = compares + 1
        array[i+j] = array2[j]
        swaps = swaps + 1
        j += 1

    return array
