import math

compares = 0
swaps = 0

def sort(array):
    global compares
    global swaps
    quicksort(array, 0, len(array)-1)
    return array, compares, swaps

# Quick sort implementation for O(n*log(n))
def quicksort(array, low, high):
    global compares
    global swaps
    if low >= high:
        compares = compares + 1
        return array
    p = partition(array, low, high)
    quicksort(array, low, p-1)
    quicksort(array, p+1, high)
    return array

def partition(array, low, high):
    global compares
    global swaps
    p = math.floor((low+high)/2) # Pivot point chosen after long and thoughtful decision process
    array[p],array[high] = array[high],array[p]
    swaps = swaps + 1
    pivot = array[high]
    left = low
    right = high-1

    while left <= right:
        compares = compares + 1
        while left <= right and array[left] <= pivot:
            compares = compares + 1
            left += 1
        while right >= left and array[right] >= pivot:
            compares = compares + 1
            right -= 1
        if left < right:
            compares = compares + 1
            array[left],array[right] = array[right],array[left]
            swaps = swaps + 1

    array[left],array[high] = array[high],array[left]
    swaps = swaps + 1
    return left
