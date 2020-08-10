# Bubble Sort

def bubble_sort(lst) -> list:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] > lst[i]:
                # print("smaller")
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    # print(lst)
    return lst
