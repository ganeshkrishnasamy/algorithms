# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# Runs O(n^2) time even if the array is sorted. It can be optimized by stopping the algorithm if inner loop didn’t cause any swap

def bubble_sort(arr):
    for i in range(len(arr)):
        swap=False
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap=True
        if swap == False:
            return arr
    return arr
arr = [0,1,3,2,5,4]
print bubble_sort(arr)
