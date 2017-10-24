def bin_srch(ls,l,r,x):
    print l,r,x
    if r >= l:
        mid = l + (r-l)/2
        print ls[mid], mid
        if ls[mid] == x:
            return mid
        elif ls[mid] > x:
            return bin_srch(ls,l,mid-1,x) 
        else:
            return bin_srch(ls,mid+1,r,x) 
    else:
        return -1
ls = [ 2, 3, 4, 10, 40,50 ]
x = 10
result = bin_srch(ls,0,len(ls)-1,x)
print result
