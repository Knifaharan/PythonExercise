def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        print("True")
    else:
        print("False")
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]
import math
def make_pi():
    return [3,1,4]
def common_end(arr1, arr2):
    if arr1[0] == arr2[0] or arr1[len(arr1)-1] == arr2[len(arr2)-1]:
        print("true")
    else:
        print("false")
def sum3(arr):
    sum=0
    for num in arr:
        sum+=num
        print(sum)
def rotate_left3(nums):
    return [nums[1], nums[2], num[0]]
def reverse3(nums):
    return [nums[2],nums[1],nums[0]]
def max_end3(nums):
    return [nums[0]]*3 if nums[0] >= nums[-1] else [nums[-1]]*3
def sum2(nums):
    return sum(nums[:2])
def middle_way(a,b):
    return [ a[1], b[1]]
def make_ends(nums):
    return [ nums[0], nums[-1]]
def has23(nums):
    return 2 in nums or 3 in nums
