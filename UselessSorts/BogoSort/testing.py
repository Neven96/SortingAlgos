import bogosort
import random_list

def main():
    unsorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorted_list, attempts = bogosort.sort(list(unsorted_list))

    print('Ordered list of numbers:')
    print('----------------------------------------------------------------------')

    print(f'Unsorted: {unsorted_list}')
    print(f'Sorted: {sorted_list}')
    print(f'Attempts: {attempts}')

    unsorted_list = random_list.create_list(7, 100)
    sorted_list, attempts = bogosort.sort(list(unsorted_list))

    print('\nRandom list of numbers:')
    print('----------------------------------------------------------------------')
    print(f'Unsorted: {unsorted_list}')
    print(f'Sorted: {sorted_list}')
    print(f'Attempts: {attempts}')

if __name__ == '__main__':
    main()
