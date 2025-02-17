def sort(unsorted_list):
    '''
    Sorts a list, Stalin method
    This is a lossy sorting algorithm, just as a warning
    Args:
        unsorted_list : 
            The unsorted list
    Returns:
        sorted_list : list
            The properly sorted list
    '''

    sorted_list = []
    i = 1
    sorted_list.append(unsorted_list[0]) #First element is alway correct

    for i in range(1, len(unsorted_list)):
        if sorted_list[len(sorted_list)-1] <= unsorted_list[i]:
            sorted_list.append(unsorted_list[i])
        
        i += 1

    return sorted_list
