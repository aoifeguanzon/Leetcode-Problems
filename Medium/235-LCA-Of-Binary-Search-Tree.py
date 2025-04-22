'''
Given 2 nodes in a binary search tree, find the closest ancestor (node connected to both nodes)
'''

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val: # if p and q are bigger than cur
                cur = cur.right # search right
            elif p.val < cur.val and q.val < cur.val: # or if they're both smaller
                cur = cur.left # search left
            else: # when one is bigger and one is smaller
                return cur # we've found the answer

'''
Time: O(log n)
In a balanced BST, each step skips half the nodes by going left or right.

Space: O(1) 
Uses only one pointer (cur) and no extra memory.
'''

'''
      LCA
     /   \
    p     q
 Since BST is sorted, this is the only valid arrangement
'''
