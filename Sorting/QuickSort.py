
def quickSort(array, start, end):
    if end > start:
        pivot = partition(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

def partition(array, start, end):
    i, j, pivotVal, left = start, end, array[start], 1
    while i != j:
        if left:
            if array[j] > pivotVal:
                j -= 1
            else:
                left = 0
                array[i] = array[j]
                i += 1
        else:
            if array[i] <= pivotVal:
                i += 1
            else:
                left = 1
                array[j] = array[i]
                j -= 1
        array[j] = pivotVal
    return j




list = [100, 2, 9, 1, 10, 22, 999, 120, 300, 5, 105]
print(list)
quickSort(list, 0, len(list) - 1)
print(list)