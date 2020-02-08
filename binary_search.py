#binary search

def binary_search(itemList, item):
    first = 0
    last = len(itemList) - 1
    result = False
    while (first <= last and not result):
        mid = (first + last)//2
        if itemList[mid] == item:
            result = True
        else:
            if item < itemList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return result

print(binary_search([1,2,3,4,5,6,7,8,9,10], 7))