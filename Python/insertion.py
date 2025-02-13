# Insertion sort implementation for O(n^2)
def sort(array):
    '''
    Takes a list of items and sorts them using insertion sort
    Insertion sort by moving the smaller item towards the front of the list
    
    Parameters
    -----------
    array : list
        A list of items that needs sorting
        
    Returns
    -----------
    array : list
        A sorted list of items
    compares : int
        The number of compares done,
        in this it will be as long as the while loop runs
    swaps : int
        The number of swaps done
    '''
    
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
