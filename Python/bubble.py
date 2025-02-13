# Bubble sort implementation for O(n^2)
def sort(array):
    '''
    Takes a list of items and returns the sorted list using bubble sort
    Bubble sort works by moving the bigger items to the end of the list
    
    Parameters
    -----------
    array : list
        A list of items that needs sorting
        
    Returns
    -----------
    array : list
        A sorted list of items
    compares : int
        The number of times the if sentence was true,
        which is how often a comparison happened
    swaps : int
        The number of swaps done with items in the list
    '''
    
    compares = 0
    swaps = 0

    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                compares += 1
                array[j],array[j+1] = array[j+1],array[j]
                swaps += 1

    return array, compares, swaps
