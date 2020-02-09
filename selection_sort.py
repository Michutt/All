# Selection Sort


def selection_sort(item_list):
    for i in range(0, len(item_list)):
        buff = item_list[i]
        for j in range(i+1, len(item_list)):
            if item_list[j] < buff:
                buff = item_list[j]
                min_loc = j

        item_list[min_loc] = item_list[i]
        item_list[i] = buff


list_to_sort = [4,3,54,3,1,23,43,75,23,8,1,1,1,1]
selection_sort(list_to_sort)
print(list_to_sort)