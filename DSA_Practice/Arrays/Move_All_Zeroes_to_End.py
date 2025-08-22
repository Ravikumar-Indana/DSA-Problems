arr = [0, 0, 0, 1, 2, 0, 3, 4, 0]
def move_zeroes_to_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] ,arr[count] = arr[count],arr[i]
            count += 1
    return arr
print("Array after moving zeroes to the end:", move_zeroes_to_end(arr))