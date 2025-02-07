# Insertion sort implementation for O(n^2)
def sort(array):
    compares = 0
    swaps = 0
    for i in range(1, len(array)):

        j = i
        while j > 0 and array[j-1] > array[j]:
            compares += 1
            array[j-1],array[j] = array[j],array[j-1]
            swaps += 1
            j -= 1
    return array, compares, swaps
