def LinearSearch(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i 
    return -1

arr = [3,23,23,23,21,314,4,14,5,6,7,8,9]

LinearSearch(arr,8)


def binarySearch (arr, l, r, x): 
        if r >= l: 
            mid = l + (r - l) // 2

            if arr[mid] == x: 
                return mid 

            elif arr[mid] > x: 
                return binarySearch(arr, l, mid-1, x) 
  
            else: 
                return binarySearch(arr, mid + 1, r, x)
        else:
            return -1
    
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")




