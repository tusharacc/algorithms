import random

def partition(arr,lo,hi):
    pivot = random.randint(lo,hi)
    arr[0],arr[j] = arr[j], arr[0]

    i = 1
    j = 1
    index = 1
    while index < hi:
        if arr[0] < arr[index]:
            arr[i], arr[index] = arr[index],arr[i]
            i += 1
        elif arr[0] > arr[i]:
            arr[j], arr[index] = arr[index],arr[j]
            j += 1
        index += 1
    

def quicksort(arr,lo,hi):
    j = partition(arr,lo,hi)
    quicksort(arr,lo,j-1)
    quicksort(arr,j+1,hi)

if __name__ == "__main__":
    array = [8,2,5,10,45,23,1,48]
