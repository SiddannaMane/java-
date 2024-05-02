import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1]= key
        
arr = [random.randint(1,100) for _ in range(10)]
print("original array:",arr)
insertion_sort(arr)
print("Sorted array:",arr)
            