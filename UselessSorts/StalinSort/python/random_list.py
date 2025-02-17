import random


def create_list(list_length, list_range):
    '''
    Creates an unsorted list of random length and number range

    Parameters
    -----------
        list_length : int
            How long the unsorted list will be
        list_range : int
            How wide the range of the numbers in the list will be
    
    Returns
    -----------
        unsorted_list : list
            An unsorted list of integers
    '''

    unsorted_list = []

    for i in range(1, list_length+1):
        unsorted_list.append(random.randint(1, list_range))

    return unsorted_list
