# Time Complexity: O(n*n)
# Auxiliary Space: O(1)
# Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
# Driver code to test above
arr = [5, 4, 3, 2, 1]
print insertion_sort(arr)
