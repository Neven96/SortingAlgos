import stalinsort
import random_list

def main():
    unsorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorted_list = stalinsort.sort(list(unsorted_list))

    print('Ordered list of numbers')
    print('----------------------------------------------------------------------')
    print(f'Unsorted: {unsorted_list}')
    print(f'Length unsorted: {len(unsorted_list)}')
    print(f'Sorted: {sorted_list}')
    print(f'Length sorted: {len(sorted_list)}')

    unsorted_list = random_list.create_list(100, 100)
    sorted_list = stalinsort.sort(list(unsorted_list))

    print('\nRandom list of numbers:')
    print('----------------------------------------------------------------------')
    print(f'Unsorted: {unsorted_list}')
    print(f'Length unsorted: {len(unsorted_list)}')
    print(f'Sorted: {sorted_list}')
    print(f'Length sorted: {len(sorted_list)}')

if __name__ == '__main__':
    main()
