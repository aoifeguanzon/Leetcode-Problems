'''
Given a rotated sorted array, find the index of a target number using an algorithm with O(log n) time complexity.
'''

# Brute force - linear search
class Solution:
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
'''
- Linear Search:  
  Time Complexity: O(n) 
  Check each element one by one.
  
  Space Complexity: O(1) 
  Only a constant amount of space is used, we aren't creating any new data
'''
    
# Optimal solution - binary search
# We can't use binary search on unsorted arrays but this is exception as in rotated sorted array, at least one side will always be sorted
def search(nums, target): # halves the array everytime so we don't go through unnecessary numbers
    left, right = 0, len(nums) - 1 # 2 pointers

    while left <= right: # if target isn't found, eventually left > right and loop ends
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]: # if left side is sorted eg [1, 2, 3, 4, 5, 0, 1, 2] 
        # but you can check if right half is sorted first too it doesn't matter
            if nums[left] <= target < nums[mid]: # if target in left side (not including middle as we've already checked that)
                right = mid - 1 # move left
            else: # if target is on RIGHT side
                left = mid + 1 # move right

        else: # if right side is sorted eg [5, 6, 0, 1, 2, 3]
            if nums[mid] < target <= nums[right]: # and if target in right side
                left = mid + 1 # move right
            else: # if target is in LEFT side
                right = mid - 1 # move left

    return -1

'''
-  Binary Search :  
   Time Complexity : O(log n) — It divides the search space in half each time.  
   Space Complexity : O(1) — Only a constant amount of space is used.
'''

'''
In a normal sorted array, we don't need to check which half is sorted each time

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1
'''

'''
This is why we need to check which side of the array is sorted each time:

[5, 1, 3], target = 5
Didn't check for sorted side, next line in code says check left side

if nums[left] <= target < nums[mid]:
if 5 <= 5 < 1 (if target (5) is greater than 5 and less than one)
Can't be true

else: left = mid + 1
We skip the target and go to 3

left = 3, right = 2
while left <= right:
3 is not less than 2 and also 3 is out of bounds and the loop stops

Return -1 even though the target was in the array
'''
