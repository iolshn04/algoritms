def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        count += 1
        print(count)
    return None


if __name__ == '__main__':
    list = [x for x in range(101)]
    print(binary_search(list, 55))
    # print(binary_search(list, -1))
