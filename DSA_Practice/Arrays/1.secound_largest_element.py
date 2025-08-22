#arr = [12, 35, 1, 10, 34, 1]
def getSecondLargest(self, arr):
    
    highest = second_highest = float('-inf')

    for num in arr:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num
    if second_highest == float('-inf'):
        return -1
    else:
        return second_highest
arr = [12, 35, 1, 10, 34, 1]
print("The second largest element is:", second_largest(arr))