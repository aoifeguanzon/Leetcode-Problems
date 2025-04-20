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

        Need to make iterator as list
            With reversed() you create new list
        Uses more memory because it keeps original order
        O(n) time, O(n) space

    Method 3
        reversed_list = result[::-1] 
        print(reversed_list)
        O(n) time, O(n) space

        Best method is .reverse(), takes up less space because it modifies the list in place

'''
# Brute force using normal lists
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
Space complexity: O(n + m) as extra list stores digits

Process both lists simultaneously
'''

# Optimal solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # value of current node
        self.next = next # pointer to the next node

class Solution:
    def addTwoNumbers(self, l1, l2): 
            # l1 and l2 are pointers to the first/head nodes of 2 linked lists
            # each time we point to a node in l1 or l2 we automatically traverse through the whole list
            ''' 
            when we talk about passing a "linked list" to a function, what we’re actually passing is just the head node of that list
            '''
        dummy_head = ListNode(0)  # dummy nodes ensure we don’t have to check if the list is empty and handle the special case of assigning the first node in the result list
        current = dummy_head  # pointer to build the result list
        carry = 0
        
        while l1 or l2 or carry:
            # continue loop until l1 and l2 are both None (ie. we've reached the last node in both lists) and there's no carry
            # get the value of the current node from l1 and l2, or use 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry  # add the values and any carry from the previous step
            
            carry = total // 10  # calculate the new carry (if total >= 10)
            current.next = ListNode(total % 10)  # create new node with ones digit of total and add it as next node in results list
            # current is used to CREATE pointers to nodes in RESULT list
            current = current.next  # move pointer to newly created node in result list
            
            if l1: l1 = l1.next  # if l1 isn't None, move to the next node in l1 (last/tail node always points to None)
            if l2: l2 = l2.next  # if l2 isn't None, move to the next node in l2
        
        return dummy_head.next  # return node dummy node ie. head of result list (which returns next, next next, next next next etc)

# current.next doesn't return all nodes because we're 'building' the linked list with it
# since dummy_head stays as the start node, when we return dummy_head.next, we go through the finished linked list

'''
Same time and space complexities O(n + m)

Time complexity: O(n + m) 
Space complexity: O(n + m) as space is used for resulting linked list
---
l1 = 2 -> 4 -> 3
l1 is a node with val = 2 and next pointing to the node with val = 4

So l1.val is 2

Then you move to l1 = l1.next (current = current.next), and now l1.val is 4, and so on
This example is for a normal list, 
'''

'''
To output a linked list:

    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

'''
