import math

# Using compares and swaps as global variables, 
# should probably be using a class for the entire program
compares = 0
swaps = 0

def compare(compares):
    compares += 1
    return compares
    
def swap(swaps):
    swaps += 1
    return swaps

def sort(array):
    '''
    Main function for merge sort
    
    Parameters
    -----------
    array : list
        A list of items that needs to be sorted
    
    Returns
    -----------
    array : list
        A sorted list of items
    compares : int
        The number of compares done,
        every time an if-statement or while loop runs
    swaps : int
        The number of swaps done
    '''
    
    global compares
    global swaps
    mergesort(array)
    
    return array, compares, swaps

# Merge sort implementation for O(n*log(n))
def mergesort(array):
    '''
    The function for splitting the list into multiple smaller lists by using
    recursion, then when the lists contains 1 or 0 items, which is sorted,
    it starts the sorting/merging
    
    Parameters
    -----------
    array : list
        At the starts it is the full list, but as the recursion continues it is
        lists of various sizes
    
    Returns
    -----------
    array : list
        Returns the merge() function, which in turn returns a list
    '''
    
    global compares
    global swaps
    
    n = len(array)
    if n <= 1:
        compares = compares + 1
        return array
        
    i = math.floor(n/2)
    array1 = mergesort(array[0:i])
    array2 = mergesort(array[i:n])

    return merge(array1, array2, array)

def merge(array1, array2, array):
    '''
    Takes in the smaller list and adds them to the third list,
    gradually merging them together to form a fully sorted list
    
    Parameters
    -----------
    array1 : list
        One of the smaller lists
    array2 : list
        Another of the smaller lists
    array : list
        The after a while fully sorted list
        
    Returns
    -----------
    array : list
        The gradually more sorted list,
        eventually fully sorted list
    '''
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
