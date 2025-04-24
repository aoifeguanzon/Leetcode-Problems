'''
Return nodes on each row,level by level
'''
# Bfs with lists
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         # Value of the node
        self.left = left       # Left child
        self.right = right     # Right child

def levelOrder(root):
    if not root:
        return []  # If the tree is empty, return an empty list
    
    result = []  # This will store the final level order traversal
    queue = [root]  # Initialize the queue with the root node (using a list)
    
    while queue:  # While there are nodes to process
        level_values = []  # This will store values of nodes at the current level
        level_size = len(queue)  # Number of nodes at the current level
        
        for _ in range(level_size):
            node = queue.pop(0)  # Remove the first node from the list (inefficient)
            level_values.append(node.val)  # Add the current node's value to the list
            
            # Add left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)  # Add left child to the end of the list
            if node.right:
                queue.append(node.right)  # Add right child to the end of the list
        
        result.append(level_values)  # Add current level's values to the result
    
    return result  # Return the full list of levels
'''
Time complexity: O(n²)
All other elements must shift. Since we perform this operation for each node, the total time complexity becomes O(n²).

Space complexity: O(n)
We store each node in the queue, and the queue size is at most the number of nodes in the tree.
'''
# Optimal solution - dfs with collections
from collections import deque  # deque is better than list for queue operations

def levelOrder(root):
    if not root:
        return []  # If the tree is empty, return an empty list
    
    result = []  # This will store the final level order traversal
    queue = deque([root])  # Use deque for efficient pops from the front (BFS)
    
    while queue:
        level_values = []  # This will store values of nodes at the current level
        level_size = len(queue)  # Number of nodes at the current level
        
        for _ in range(level_size):
            node = queue.popleft()  # Pop from the front of the queue (fast with deque)
            level_values.append(node.val)  # Add the current node's value
            
            # Add left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_values)  # Add current level's values to the result
    
    return result  # Return the full list of levels
'''
Time complexity: O(n)
Removing the first element (popleft()) and adding elements to the end of the queue both take constant time since each node is processed once.

Space complexity: O(n)
Similar to the list solution, we store each node in the queue, and the maximum size of the queue is equal to the number of nodes in the tree.


'''
