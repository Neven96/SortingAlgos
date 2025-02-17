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

def sort(lists):
    '''
    Main function for merge sort
    
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
    mergesort(lists)
    
    return lists, compares, swaps

# Merge sort implementation for O(n*log(n))
def mergesort(lists):
    '''
    The function for splitting the list into multiple smaller lists by using
    recursion, then when the lists contains 1 or 0 items, which is sorted,
    it starts the sorting/merging
    
    Parameters
    -----------
    lists : list
        At the starts it is the full list, but as the recursion continues it is
        lists of various sizes
    
    Returns
    -----------
    lists : list
        Returns the merge() function, which in turn returns a list
    '''
    
    global compares
    global swaps
    
    n = len(lists)
    if n <= 1:
        compares = compares + 1
        return lists
        
    i = math.floor(n/2)
    list1 = mergesort(lists[0:i])
    list2 = mergesort(lists[i:n])

    return merge(list1, list2, lists)

def merge(list1, list2, lists):
    '''
    Takes in the smaller list and adds them to the third list,
    gradually merging them together to form a fully sorted list
    
    Parameters
    -----------
    list1 : list
        One of the smaller lists
    list2 : list
        Another of the smaller lists
    lists : list
        The after a while fully sorted list
        
    Returns
    -----------
    lists : list
        The gradually more sorted list,
        eventually fully sorted list
    '''
    global compares
    global swaps
    
    i = 0
    j = 0
    a1 = len(list1)
    a2 = len(list2)

    while i < a1 and j < a2:
        compares = compares + 1
        if list1[i] < list2[j]:
            compares = compares + 1
            lists[i+j] = list1[i]
            swaps = swaps + 1
            i += 1
        else:
            compares = compares + 1
            lists[i+j] = list2[j]
            swaps = swaps + 1
            j += 1

    while i < a1:
        compares = compares + 1
        lists[i+j] = list1[i]
        swaps = swaps + 1
        i += 1

    while j < a2:
        compares = compares + 1
        lists[i+j] = list2[j]
        swaps = swaps + 1
        j += 1

    return lists
