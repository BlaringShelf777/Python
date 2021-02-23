import random

def bubbleSort(array):
    for j in range(len(array) - 1, 0, -1):
        for i in range(j):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
def randomList(list, size):
    for _ in range(size):
        list.append(random.randrange(0, 100))

list = []
randomList(list, 10)
print('> Array not sorted:', list)
bubbleSort(list)
print('> Array sorted:', list)
