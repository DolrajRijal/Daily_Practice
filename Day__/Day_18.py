#Given an array arr[], 
# find and return the maximum product
#  possible with the subset of elements 
# present in the array.

arr1 = [9,-4,7,0,-1,8]

def max_prod_subset(arr):
    n = len(arr)
    if n == 1:
            return(arr[0])
    product = 1
    neg_count = 0
    zero_count = 0
    max_neg = float('-inf')

    for num in arr:
        if num == 0:
            zero_count += 1
            continue

        if num < 0:
            neg_count += 1
            max_neg =max(max_neg, num)

        product *= num

    if zero_count == n:
        return 0

    if neg_count == 1 and zero_count == n-1:
        return 0
    if neg_count % 2 == 1:
        product //= max_neg

        
    return product
    
    
max_prod_subset(arr1)
