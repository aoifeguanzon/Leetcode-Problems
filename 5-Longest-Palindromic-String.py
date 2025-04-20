'''
Given a string s, return the longest palindromic substring in s.
'''

# Brute force search
'''
Finding all possible substrings for each character in s
'''
def longest_palindrome(s):
    max_len = 0
    longest = ""
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > max_len:
                max_len = len(substring)
                longest = substring
                
    return longest

# Optimal solution - expand around centre search
'''
Comparing each half of word to each other
'''
def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right] # because we make moves before

def longestPalindrome(self, s: str) -> str:
    if len(s) == 0:
        return ""
    
    longest = ""
    
    for i in range(len(s)):
        palindrome1 = self.expand_around_center(s, i, i)       # odd-length palindrome
        palindrome2 = self.expand_around_center(s, i, i + 1)   # even-length palindrome
        # makes sense because middle of even amount of numbers = middle two numbers
        # 1 2 3 4 5 6
        #     | |     3rd and 4th -> n / 2 and (n / 2 + 1)
        
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
    
    return longest

  '''
   0   1   2   3   4
   a   b   c   d   e
           ↑
        center (i=2)
  left = 2
  right = 2
  
  c = c
  left -= 1 is 1
  right += 1 = 3
  b != d
  
  s[1:3] = bc which is wrong so we do
  s[left + 1:right]
  s[2:3] 
  c
  '''
