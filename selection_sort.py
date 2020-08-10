# Selection Sort 
def selection_sort(lst) -> list:
    length = len(lst)
    for i in range(length):
        minimum = i
        for j in range(i+1, length):
            if lst[j] > lst[minimum]:
                minimum = j
        tmp = lst[i]
        lst[i] = lst[minimum]
        lst[minimum] = tmp
