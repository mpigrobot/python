def binarySearch(lst, value, low, high):
    if high < low:
        return -1
    mid = (low + high) / 2
    if lst[mid] > value:
        return binarySearch(lst, value, low, mid - 1)
    elif lst[mid] < value:
        return binarySearch(lst, value, mid + 1, high)
    else:
        return mid
def bsearch(l, value):
    lo, hi = 0, len(l) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    l = range(50)
    print binarySearch(l, 10, 0, 49)
    print bsearch(l, 10)