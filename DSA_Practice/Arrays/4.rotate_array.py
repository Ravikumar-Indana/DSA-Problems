def reverse(arr,s,l):
    while s<l:
        arr[s], arr[l] = arr[l], arr[s]
        s += 1
        l -= 1  

def rotate_array(arr, d):
    n = len(arr)
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    return arr

arr = [1, 2, 3, 4, 5]
d = 2
print("Original array:", arr)
print("Rotated array:", rotate_array(arr, d))   