# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(A,first,middle,last):
    L = A[first:middle] # left half of the array
    R = A[middle:last+1]
    L.append(999999)
    R.append(999999)
    i = j = 0
    for k in range(first,last+1):
        
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    
    
    return A


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr, first, last ):
    if first < last:
        middle = (first + last) // 2
        merge_sort(arr,first,middle)
        merge_sort(arr,middle+1,last)
        merge(arr,first,middle,last)
    

    return arr



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


arr = [6,2,43,5,9,19,22]
x = 0
y = len(arr) - 1

print(merge_sort(arr,x,y))