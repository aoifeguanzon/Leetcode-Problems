'''
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
'''
# Brute force solution
def longestPalindrome(s):
    count = 0
    ans = 0
    a = set(s)

    for i in a:
        if i % 2 == 0:
            c = s.count(i)
            if c % 2 == 0:
                ans += c
            else:
                ans += c - 1
                count = 1
    
    print(ans + count)

'''
Time Complexity: O(n²)  
Creating `set(s)` takes O(n) time
In the worst case, the set's size is `n`, and calling `s.count(i)` for each unique character takes O(n)
.count basically a loop so we have a nested loop, therefore n * n = n^2

Space Complexity: O(n)  
The set or dictionary requires O(k) space, where `k` is the number of unique characters
In the worst case, `k = n`, so the space complexity is O(n).
'''

# Solution 1 - hash map
def longestPalindrome(s: str) -> int:
    freq = {} # hash map
    
    for char in s: # adding chars to hash map / increasing their count
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    length = 0
    odd_found = False
    
    for count in freq.values(): # freq.values() are the counts, if we wanted letters we'd get keys
        if count % 2 == 0: # if even
            length += count
        else:
            length += count - 1 # get closest even number and add it to length of palindrome as we need pairs of letters for symmetry
            odd_found = True
    
    if odd_found:
        length += 1 # centre character added if there's at least 1 odd-occuring letter
    
    return length

'''
Time Complexity:
O(n), where n is the length of the string
We iterate through the string once to count the frequencies 
and then through the frequency dictionary (which will have at most 52 entries (k = 52) in the case of case-sensitive letters).
Therefore technically O(n + k) but n could be a million and k will always be capped at 52, so its size is negligible

Space Complexity:
O(k), where k is the number of unique characters in the string. 
Worst case is at most 52 for case-sensitive letters
'''

# Solution 2 - set
def longestPalindrome(s: str) -> int:
    odd_set = set()
    
    for char in s:
        if char in odd_set:
            odd_set.remove(char)
        else:
            odd_set.add(char)
    # every second time we see a letter it gets removed, therefore all letters NOT in the set once we've reached the end of the string are even

    return len(s) - len(odd_set) + (1 if odd_set else 0) # all characters in string - amount of unique odd-occuring characters + centre character
    # len(s) - len(odd_set) returns all characters that can be used in pairs
'''
Time complexity: O(n) as we loop through the string once, and we do constant-time work (like adding/removing from a set) for each character

Space complexity: O(k) where k is the number of unique characters (max 52 for a–z + A–Z) → basically constant
'''

'''
s = "abccccdd"

a | 1
b | 1
c | 4
d | 2

odd_set = set()

# a → add 'a' → {'a'}
# b → add 'b' → {'a', 'b'}
# c → add 'c' → {'a', 'b', 'c'}
# c → remove 'c' → {'a', 'b'}
# c → add 'c' → {'a', 'b', 'c'}
# c → remove 'c' → {'a', 'b'}
# d → add 'd' → {'a', 'b', 'd'}
# d → remove 'd' → {'a', 'b'}

len(s) = 8              # Total characters
len(odd_set) = 2        # a and b have odd counts

len(s) - len(odd_set) = 8 - 2 = 6

Total palindrome length = 6 + 1 = 7
'''
