import math

# Using compares and swaps as global variables, 
# should probably be using a class for the entire program
compares = 0
swaps = 0

def sort(array):
    '''
    Main function for quick sort
    
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
    
    quicksort(array, 0, len(array)-1)
    
    return array, compares, swaps

# Quick sort implementation for O(n*log(n))
def quicksort(array, low, high):
    '''
    Recursive function for partitioning the list into smaller lists,
    runs until each partition has either 1 or 0 items
    
    Parameters
    -----------
    array : list
        A list of items, 
    low : int
        The lower poisition of the pivot point
    high : int
        The higher position of the pivot point
        Both low and high referes to the boundaries of the list to be partitioned
        
    Returns
    -----------
    array : list
        The gradually more sorted list
    '''
    
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
    '''
    Function to set the pivot point and to sort the list
    
    Parameters
    -----------
    array : list
        The list of items to be partitioned/sorted
    low : int
        The lower poisition of the pivot point
    high : int
        The higher position of the pivot point
        Both low and high referes to the boundaries of the list to be partitioned
    
    Returns
    -----------
    left : int
        The new pivot point
    '''
    
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
