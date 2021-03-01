import random

def randomList(list, size):
    for _ in range(size):
        list.append(random.randrange(0, 100))

def heapify(arr, size, index):
    i = index
    if (index + 1) * 2 < size and arr[i] < arr[(index + 1) * 2]:
        i = (index + 1) * 2
    if (index + 1) * 2 - 1 < size and arr[i] < arr[(index + 1) * 2 - 1]:
        i = (index + 1) * 2 - 1
    if index != i:
        arr[index], arr[i] = arr[i], arr[index]
        heapify(arr, size, i)

def heapSort(arr):
    heapSize = len(arr) - 1
    # BuildHeap:
    for i in range(heapSize, 0, -1):
        heapify(arr, len(arr), i//2)
    # Sort
    for i in range(heapSize + 1):
        arr[0], arr[heapSize] = arr[heapSize], arr[0]
        heapify(arr, heapSize, 0)
        heapSize = heapSize - 1




list = []
randomList(list, 10)
print('> Array not sorted:', list)
heapSort(list)
print('> Array sorted:', list)