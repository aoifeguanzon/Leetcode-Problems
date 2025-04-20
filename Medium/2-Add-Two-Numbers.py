'''
Given two non-empty linked lists representing two non-negative integers, 
with digits stored in reverse order, 
add the two numbers and return the sum as a linked list in reverse order.

Example:
Input: 
l1 = [2,4,3], l2 = [5,6,4]

Output: 
[7, 0, 8]

Explanation: 
1. Add the first digits from each list:
        2 + 5 = 7 (no carry)
        
2. Add the second digits from each list:
        4 + 6 = 10. 
        Write down 0 and carry over 1.
        
3. Add the third digits from each list, including the carry:
        3 + 4 = 7, plus the carry 1, gives 8.

4. Result = 807, represented in reverse order by [7, 0, 8]

If we wanted the digits in normal order we just do result.reverse() or result[::-1] (-1 steps)

---
To write output as a normal number:
    Method 1
        result.reverse() 
        result = ''.join(map(str, result)
        print(int(result))

        We must do .reverse() first otherwise None is returned
        .reverse() modifies original list
        O(n) time, O(1) space

    Method 2
        reverse_iterator = reversed(result)
        print(list(reverse_iterator))

        Need to make iterator as list, so with reversed() you create new list
        Uses more memory because it keeps original order
        O(n) time, O(n) space

    Method 3
        reversed_list = result[::-1] 
        print(reversed_list)
        O(n) time, O(n) space

        Best method is .reverse(), takes up less space because it modifies the list in place

'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = [] # initialise empty list which stores digits of sum, starting from rightmost digit (reversed)
        carry = 0 # stores carry over when digit > 9
        i = 0 # to iterate over l1 and l2

        while i < len(l1) or i < len(l2) or carry:  # loop through both lists until all digits are processed and there's no carry left
            val1 = l1[i] if i < len(l1) else 0 # these lines says if either list is shorter, add 0 to remaining elements of other list
            val2 = l2[i] if i < len(l2) else 0 
            # val1, val2 = l1[i] if i < len(l1) else 0, l2[i] if i < len(l2) else 0
            # could combine these as shown above, creating a tuple, but written the first way improves readability

            total = val1 + val2 + carry
            carry = total // 10 # digit in 'tens' place gets carried
            result.append(total % 10) # append the 'ones' digit as you do in addition

            i += 1

        return result

'''
Time complexity: O(n + m) ie. the length of both lists n and m
Space complexity: O(n + m)

Process both lists simultaneously
'''

# We could also use linked lists and iterate over the nodes but the solution takes longer to write, and time / space complexities are the same
