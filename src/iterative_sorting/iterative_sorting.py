# TO-DO: Complete the selection_sort() function below 
# How it works [4,7,2,9,3,8]
        # start with the current index
        # so "for i in range(len(arr)):
        #       CI = i
        #       arr[i] == 4"
        #
        # then for j in range(len(arr)):
        #           if arr[CI] > arr[j]:
        #               arr[CI] = arr[j]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0,len(arr)-1):
        smallest = i 
        
             

        # finds the smallest element in the list
        for j in range(smallest+1,len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
        
        # swap 
        arr[i],arr[smallest] = arr[smallest],arr[i]
        
         

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
            
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



print(selection_sort([8,2,4,6,9,0]))
