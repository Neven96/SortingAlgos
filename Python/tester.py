import sys
import os
import time

import bubble
import insertion
import merge
import quick

def main():
    '''
    Runs the test file, and prints out the finished products
    '''

    file_path, algo, print_sorted_list = input_checker()
    
    unsorted_list = read_file(file_path)
    
    sorted_list, compares, swaps, time_used = sorter(list(unsorted_list), algo)
    
    # If for some reason something happens to the algorithms
    if sorted_list != sorted(unsorted_list):
        print("LISTS NOT SORTED")
        
    print(f'Sorted list using: {algo.__name__} sort')
    print(f'Using {str(compares)} compares and {str(swaps)} swaps')
    
    # Time handling
    time_used, time_symbol = time_handling(time_used)
        
    print(f'Time used: {time_used:.4f} {time_symbol}')

    # Prints out the sorted list if you asked for it
    if print_sorted_list:
        print('\nSorted list:')
        print('----------------------------------------------------------------------')
        print(sorted_list)

def sorter(unsorted_list, algo):
    '''
    Handles the sorting of the list with the correct algorithm
    Also handles the time keeping for each algorithm

    Parameters
    -----------
    list : list
        The list that shall be sorted
    algo : module
        The sorting algorithm to be used

    Returns
    -----------
    sorted_list : list
        The sorted list
    compares : int
        The amount of compares the algorithm used
        Every time a while loop or if statement is called
    swaps : int
        Every time one item in the list is swaped to another place
    time_used : int
        The time used to run the algorithm
        It is in nano seconds
    '''
    start_time = time.perf_counter_ns()
    sorted_list, compares, swaps = algo.sort(unsorted_list)
    time_used = time.perf_counter_ns() - start_time

    return sorted_list, compares, swaps, time_used

def read_file(file_path):
    '''
    Reads the file that contains an unsorted list

    Parameters
    -----------
    file_path : str
        The path to the file

    Returns
    -----------
    unsorted_list : list
        The unsorted list
    '''

    unsorted_list = []
    
    try:
        with open(file_path, 'r') as file:
            unsorted_list = [int(x) for x in file.readlines()]
    except FileNotFoundError:
        print('File not found!')
        sys.exit(1)
        
    return unsorted_list
    
def input_checker():
    '''
    A function to handle all the inputs needed to sort with correct algorithm

    Returns
    -----------
    file_path : string
        The full path for the file that contains the unsorted list
    algo : module
        The module which contains the sorting algorithm
    print_sorted_list : bool
        If you want to print the sorted list or not
    '''

    # Gets the file path for all the inputs
    test_files_path = os.path.join('..', 'inputs')
    filenames = os.listdir(test_files_path)
    
    # A list of all the modules for the sorting algorithms and a list of their names
    sorting_algos = [bubble, insertion, merge, quick]
    sorting_algo_names = [names.__name__ for names in sorting_algos]
    
    # Gets the file path for the chosen file
    filename = input_handler('Test File', filenames)
    file_path = os.path.join(test_files_path, filename)
    
    # Takes the name for the algo and gets the correct module
    algo_name = input_handler('Sorting Algorithm', sorting_algo_names)
    algo = sorting_algos[sorting_algo_names.index(algo_name)]

    print_sorted_list = input_handler('If You Want To Print The Sorted list', ['yes', 'no'])
    print_sorted_list = True if print_sorted_list == 'yes' else False
    
    return file_path, algo, print_sorted_list
    
def input_handler(description, input_list):
    '''
    Creates the prints and takes in user input for the choices of files,
    algorithms and if you want the sorted list printed

    Parameters
    -----------
    description : str
        The string that describes for the user what they are choosing
    input_list : list
        The list of choices to be made by the user

    Returns
    -----------
    chosen_name : str
        The chosen list item from the input_list
    '''

    while True:
        print(f'Please Choose {description}:')
        print('----------------------------------------------------------------------')
        
        for i in range(len(input_list)):
            print(str(i+1) + ': ' + input_list[i])
        print('x: exit')
        
        choice = input('Choice: ')
        
        try:
            choice = int(choice.strip())
        except:
            if choice.strip().lower() == 'x':
                
                print('----------------------------------------------------------------------')
                print('EXITING')
                print('----------------------------------------------------------------------')
                
                sys.exit(0)
            
            print('----------------------------------------------------------------------')
            print(f'"{choice}" Is Not A Choice')
            print('----------------------------------------------------------------------\n')

            continue
        if choice < 1 or choice > len(input_list):
            
            print('----------------------------------------------------------------------')
            print(
                f'Please Choose A number Between 1 And {str(len(input_list))}')
            print('----------------------------------------------------------------------\n')
            
            continue
        break
        
    chosen_name = input_list[choice-1]
    
    print(f'{description} Chosen: {chosen_name}\n')
    
    return chosen_name
    
def time_handling(time_used):
    '''
    Handles converting of time to appropriate formats

    Parameters
    -----------
    time_used : int
        The time the program used in nanoseconds

    Returns
    -----------
    time_used : int/float
        The time used in either int nanoseconds
        or converted to float milliseconds or seconds
    time_symbol : str
        The format/symbol, either ns for nanoseconds,
        ms for milliseconds or s for seconds
    '''

    time_symbol = 'ns'

    if time_used > 1000000000:
        time_used = time_used/1000000000.0
        time_symbol = 's'
    elif time_used > 1000000:
        time_used = time_used/1000000.0
        time_symbol = 'ms'
    
    return time_used, time_symbol

if __name__ == '__main__':
    main()