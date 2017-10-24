# Like Binary Search, Jump Search is a searching algorithm for sorted arrays. 
# The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or
# skipping some elements in place of searching all elements.

# For example, suppose we have an array arr[] of size n and block (to be jumped) size m. 
# Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on. 
# Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search operation from the index km to find the element x.


import math

def jump_search(ls, x):
    
    n = len(ls)
#   Finding block size to be jumped
    step = int(math.floor(math.sqrt(n)))
    print "Step Size: %d" %(step)
    prev=0
#   Finding the block where element is present (if it is present)
    while (ls[min(step,n-1)]<x):
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n-1:
            return -1
#   Doing a linear search for x in block beginning with prev
    while (ls[prev]<x):
#           If we reached next block or end of array, element is not present.
        if (prev == min(step, n-1)):
            return -1 
        prev += 1
    print "prev:", prev
#  If element is found
    if (ls[prev] == x):
        return prev
    return -1

ls=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x=377

result = jump_search(ls, x)
print result
