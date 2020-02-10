# Insertion Sort


def insertion_sort(item_list):
    for i in range(1, len(item_list)):
        buff = item_list[i]
        pos = i

        while pos > 0 and item_list[pos-1]>buff:
            item_list[pos] = item_list[pos-1]
            pos -= 1

        item_list[pos] = buff


lista = [3,1,7,2,4,7,2,4,6,0,8,9,1]
insertion_sort(lista)
print(lista)