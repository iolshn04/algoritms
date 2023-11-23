def sum(array):
    if array == []:
        return 0
    return array[0] + sum(array[1:])


if __name__ == '__main__':
    print(sum([1, 2, 3, 4]))
