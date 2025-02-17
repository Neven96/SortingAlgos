import math

# Using compares and swaps as global variables, 
# should probably be using a class for the entire program
compares = 0
swaps = 0

def sort(lists):
    '''
    Main function for quick sort
    
    Parameters
    -----------
    lists : list
        A list of items that needs to be sorted
    
    Returns
    -----------
    lists : list
        A sorted list of items
    compares : int
        The number of compares done,
        every time an if-statement or while loop runs
    swaps : int
        The number of swaps done
    '''
    
    global compares
    global swaps
    
    lists = quicksort(lists, 0, len(lists)-1)
    
    return lists, compares, swaps

# Quick sort implementation for O(n*log(n))

def quicksort(lists, low, high):
    '''
    Recursive function for partitioning the list into smaller lists,
    runs until each partition has either 1 or 0 items
    
    Parameters
    -----------
    lists : list
        A list of items, 
    low : int
        The lower poisition of the pivot point
    high : int
        The higher position of the pivot point
        Both low and high referes to the boundaries of the list to be partitioned
        
    Returns
    -----------
    list : list
        The gradually more sorted list
    '''
    
    global compares
    global swaps
    
    if low >= high:
        compares = compares + 1
        return lists
        
    p = partition(lists, low, high)
    
    quicksort(lists, low, p-1)
    quicksort(lists, p+1, high)
    
    return lists

def partition(lists, low, high):
    '''
    Function to set the pivot point and to sort the list
    
    Parameters
    -----------
    lists : list
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
    lists[p], lists[high] = lists[high], lists[p]
    swaps = swaps + 1
    
    pivot = lists[high]
    
    left = low
    right = high-1

    while left <= right:
        compares = compares + 1
        
        while left <= right and lists[left] <= pivot:
            compares = compares + 1
            left += 1
            
        while right >= left and lists[right] >= pivot:
            compares = compares + 1
            right -= 1
            
        if left < right:
            compares = compares + 1
            lists[left], lists[right] = lists[right], lists[left]
            swaps = swaps + 1

    lists[left], lists[high] = lists[high], lists[left]
    swaps = swaps + 1
    
    return left
