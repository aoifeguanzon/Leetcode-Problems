'''
Given 2 nodes, find the closest ancestor (node connected to both nodes)
'''

# Brute force: two dfs
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # find path to q then find another path to p
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_path(root, target, path):
            if not root:
                return False
            path.append(root)
            if root == target:
                return True
            if find_path(root.left, target, path) or find_path(root.right, target, path):
                return True
            path.pop()
            return False

        path_p = []
        path_q = []

        find_path(root, p, path_p)
        find_path(root, q, path_q)

        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1

        return path_p[i - 1]
'''
Time complexity: O(N) 
Execution time increases in proportion to the number of nodes in the tree

Space complexity: O(N) 
Due to storing the paths for both p and q, which can be as long as the height of the tree.
'''


# Optimal solution: one dfs
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left  # left child of this node
        self.right = right  # right child of this node

class Solution: # notice outer function takes root, inner functions take next nodes
    def lowestCommonAncestor(self, root, p, q):  # finds the lowest common ancestor of p and q
        # root is the current node we're checking
        if not root or root == p or root == q:  # if node is null or matches p or q, return it
            return root # if we were searching left, now search right, then after that begin backtracking
        
        # search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)   # go left
        right = self.lowestCommonAncestor(root.right, p, q)  # go right

        # THIS IS WHERE BACKTRACKING HAPPENS - both left and right have found end, p or q
        # remember this is still the same function call, we recursed left and right from root (eg. 2) and now will either return 2 or whatever side found p or q
        if left and right: 
            return root # if both sides found something, this node is the LCA

        return left if left else right  # otherwise return the side that found p or q (or None if neither)
'''
Time complexity: O(N) because we perform a single DFS traversal of the tree, visiting each node once.

Space complexity: O(N) because of the recursion stack, which can reach a depth of N in the worst case (for a skewed tree).
'''

'''
It took me so long to wrap my head around the logic of this, i think it was because i somehow thought root.left/right updates the root variable in the outer function, which just doesn't happen
Have to remember that recursion keeps happening until we find p or q or end of tree, so if left and/or right have a value, it has to be p or q!
'''

'''
Until we find both p and q or reach end of tree, we only reach base case and inner functions.
We begin the backtracking process with the second half of the code.
'''

'''
    3
   / \
  5   1
 / \
6   2
   / \
  7   4
Finding LCA of 7 and 4:

Start at root 3, call lowestCommonAncestor(5, 7, 4) and lowestCommonAncestor(1, 7, 4).

At root 5:
Call lowestCommonAncestor(6, 7, 4) and lowestCommonAncestor(2, 7, 4).

At root 6:
Neither 7 nor 4 is here, so left = None.

At root 2:
Call lowestCommonAncestor(7, 7, 4) and lowestCommonAncestor(4, 7, 4).

At root 7:
This is p, so left = 7.

At root 4:
This is q, so right = 4.

Back at root 2:
left = 7 and right = 4, so both are not None. We return root = 2 (the LCA of 7 and 4). Reminder, outer function 'root' variable = 2.

Back at node 5:
left = None and right = 2, so we return right = 2.

Back at root 3:
left = 2 and right = None, so we return left = 2.
'''
