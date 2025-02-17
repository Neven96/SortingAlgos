import random

def sort(lists):
    '''
    Sorts a list using bogosort
    Which randomizes the list every time and checks if it sorted

    Parameters
    -----------
    lists : list
        An unsorted list in need of sorting

    Returns
    -----------
    lists : list
        A properly sorted list
    attempts : int
        How many attempts it took to sort the list
    '''
    
    attempts = 0
    while lists != sorted(lists):
        lists = randomize_list(lists)
        attempts += 1

    return lists, attempts

def randomize_list(lists):
    for i in range(len(lists)):
        j = random.randint(0, len(lists)-1)

        if i == j:
            continue

        lists[i], lists[j] = lists[j], lists[i]

    return (lists)
