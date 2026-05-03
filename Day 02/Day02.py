# Given an array of integer, return indices of two number such that they add upto a specific target.
#you may asume that each input would have exactly one solution and you may not use the same element twice
nums1 = [2,6,8,1,9,7]
target = 9
def two_sum(nums1, target):
    for i in range(0, len(nums1) - 1):
        for j in range(1, len(nums1)):
            if nums1[i] + nums1[j] == target:
                return i, j
            


result = two_sum(nums1, target)
print(result)
#classic two sum roblem is better solved with dictionary