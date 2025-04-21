'''
Given an integer array 'height' of length n,
There being n vertical lines representing sides of a container,
Find the 2 lines that together with the x-axis form the container holding the largest amount of water.
'''

# Brute force
class Solution:
    def maxArea(height):
        max_area = 0
        n = len(height)

        for i in range(n): # left columns
            for j in range(i + 1, n): # right columns
              # because right columns start at i + 1 we don't overlap
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                max_area = max(max_area, area)

        return max_area

'''
Time Complexity: O(n²)
Two nested loops check every pair of lines.

Space Complexity: O(1)
Only a few variables are used so no extra space is needed for data structures.
'''

# Optimal solution - 2 pointer technique
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = min(height[right], height[left]) * width
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
'''
Time Complexity: O(n)
Only loop through the array once, moving the pointers toward each other.

Space Complexity: O(1)
You use only a constant amount of extra space.
'''
