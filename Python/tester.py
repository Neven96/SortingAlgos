import sys
import os
import time

import bubble
import insertion
import merge
import quick

def sorter(filename, algo):
    with open(filename, 'r') as file:
        array = [int(x) for x in file.readlines()]
    
    start_time = time.process_time_ns()
    sorted_array, compares, swaps = algo.sort(array)
    time_used = time.process_time_ns() - start_time
    return sorted_array, compares, swaps, time_used
    
def input_checker():
    test_files_path = os.path.join('..', 'inputs')
    filenames = os.listdir(test_files_path)
    
    sorting_algos = [bubble, insertion, merge, quick]
    sorting_algo_names = [n.__name__ for n in sorting_algos]
    
    filename = input_validator('Test File', filenames)
    filename = os.path.join(test_files_path, filename)
    
    algo_name = input_validator('Sorting Algorithm', sorting_algo_names)
    algo = sorting_algos[sorting_algo_names.index(algo_name)]
    
    print_sorted_array = input_validator('If You Want To Print The Sorted Array', ['yes', 'no'])
    print_sorted_array = True if print_sorted_array == 'yes' else False
    
    return filename, algo, print_sorted_array
    
def input_validator(description, array):
    while True:
        print('Please Choose ' + description + ':')
        print('----------------------------------------------------------------------')
        
        for i in range(len(array)):
            print(str(i+1) + ': ' + array[i])
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
            print('"' + choice + '" Is Not A Choice')
            print('----------------------------------------------------------------------\n')

            continue
        if choice < 1 or choice > len(array):
            
            print('----------------------------------------------------------------------')
            print('Please Choose A choice Between 1 And ' + str(len(array)))
            print('----------------------------------------------------------------------\n')
            
            continue
        break
        
    name = array[choice-1]
    
    print(description + ' Chosen: ' + name + '\n')
    
    return name
    
if __name__ == '__main__':
    filename, algo, print_sorted_array = input_checker()
    
    sorted_array, compares, swaps, time_used = sorter(filename, algo)
    
    print('Sorted array using: ' + algo.__name__ + ' sort')
    print('Using ' + str(compares) + ' compares and ' + str(swaps) + ' swaps')
    if time_used > 1000000000:
        print('Over ' + '{:.4f}'.format(time_used/1000000000.0) + 's')
    elif time_used > 1000000:
        print('Over ' + '{:.4f}'.format(time_used/1000000.0) + 'ms')
    else:
        print('Over ' + '{:.4f}'.format(time_used) + 'ns')

    
    if print_sorted_array:
        print('\nSorted Array:')
        print('----------------------------------------------------------------------')
        print(sorted_array)