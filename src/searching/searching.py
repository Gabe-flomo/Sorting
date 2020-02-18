# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code

   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)
  middle = (low + high) // 2
  found = False
  arr.sort()
  i = 0
  while i < 10:
    i += 1
    val = arr[middle]
    print(f"Middle: {middle} value: {val} target: {target}")
     
    if val == target:
      found = True
      return val
    elif val > target:
      print("Top half")
      low = middle + 1
      high = len(arr[low:])
      middle = (low + high) // 2
    elif val < target:
      
    




  

   # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

x = [2,13,6,8,10,24,20]
t = 13

print(binary_search(x,t))