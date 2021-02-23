
def bubbleSort(array):
    for j in range(len(array) - 1, 0, -1):
        for i in range(j):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp


array = [54,26,93,17,77,31,44,55,20] 

print('> Array not sorted:', array)
bubbleSort(array)
print('> Array sorted:', array)
