'''
Given a string s, find the length of the longest substring without duplicate characters.
'''
# Brute force - linear search
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        
        for i in range(len(s)):
            seen = set() # for each letter in string, we start with empty set
            for j in range(i, len(s)):
                if s[j] in seen:
                    break  # found a repeat, stop and go back to outer loop
                seen.add(s[j]) # if loop doesn't break (ie. character is unique), add it to set
                max_length = max(max_length, j - i + 1) # +1 to account for last number too
        
        return max_length

'''
Time Complexity: O(n²) due to nested for-loop
Space Complexity: O(n) as in the worst case, it can store all characters (n) in the substring
'''

# Optimal solution - hash map
class Solution: # Moving window function, we expand with right and shrink with left when duplicates are found
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)): 
            while s[right] in char_set: # as long as letter at right pointer is in char_set
                char_set.remove(s[left]) # remove all characters in char_set up to and including the duplicate character
                left += 1 
            # char_set = abcde
            # s[right] = d
            # remove letters in char_set until char_set = de

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            # left = 2, right = 6
            # 2 3 4 5 6 = 5 numbers
            # 6 - 2 = 4 -> not enough numbers
            # + 1 so we also account for last number

        return max_length
'''
Time Complexity: O(n) as there is ONE loop over the string
Each character in string is added and removed from the set at most once

Space Complexity: O(k)
At most, char_set stores the unique characters in the current window. In the worst case, it can hold k unique characters (where k is the size of the longest substring without repeating characters). So, space complexity is O(k), where k ≤ n.

'''
