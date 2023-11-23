def find_smallest(array: list):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if smallest > array[i]:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def sort_list(array: list):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


if __name__ == '__main__':
    print(sort_list([5, 3, 6, 2, 10]))