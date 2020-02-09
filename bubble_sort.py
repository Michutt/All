#bubble Sort


def bubble_sort(item_list):
    ready = False
    while not ready:
        ready = True
        for i in range(len(item_list)-1):
            if item_list[i] > item_list[i+1]:
                ready = False
                buff = item_list[i+1]
                item_list[i+1] = item_list[i]
                item_list[i] = buff


list_to_sort = [4,3,54,3,1,23,43,75,23,8,1,1,1,1]
bubble_sort(list_to_sort)
print(list_to_sort)