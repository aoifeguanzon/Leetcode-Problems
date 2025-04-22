 '''
Count how many separate groups of connected '1's (land) exist in a 2D grid, 
where connections can be horizontal or vertical.
'''

# Brute force - checking every possible pair of 1's in the grid
class Solution:
  def numIslands(grid):
      if not grid:
          return 0
  
      m, n = len(grid), len(grid[0])
      visited = [[False] * n for _ in range(m)]
      islands = 0
  
      def dfs(i, j):
          if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or visited[i][j]:
              return
          visited[i][j] = True
        
          dfs(i + 1, j) 
          dfs(i - 1, j)
          dfs(i, j + 1)
          dfs(i, j - 1)
  
      for i in range(m):
          for j in range(n):
              if grid[i][j] == '1' and not visited[i][j]:
                  dfs(i, j)
                  islands += 1
  
      return islands

'''
Time Complexity: O(m x n) 
Checking every '1' against every other '1' in the grid.

Space Complexity: O(m x n)
Storing the visited matrix to track processed cells.
'''

# Optimal solution - DFS
class Solution:
  def numIslands(grid):
      if not grid: # if grid is empty
          return 0
      
      m, n = len(grid), len(grid[0]) # rows = m, columns = n
      islands = 0
      
      def dfs(i, j): # recursive function that explores all connected land ('1') from a starting point
          if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0': # base case; recursion stops when out of bounds or on water
            # last valid row is m - 1 due to indexing
              return
          grid[i][j] = '0'  # mark as visited by changing '1' to '0'
          # visit all 4 directions
          dfs(i + 1, j) # up
          dfs(i - 1, j) # down
          dfs(i, j + 1) # left
          dfs(i, j - 1) # right
      # this is where the code starts
      for i in range(m): # for each row
          for j in range(n): # for all columns in the row
              if grid[i][j] == '1':  # if we find unvisted land
                  dfs(i, j)  # perform DFS at coordinate
                  islands += 1
  
      return islands

'''
Time Complexity: O(m × n)
Every cell in the grid is visited once at most, either by the main loop or by DFS.

Space Complexity: O(m × n)
This comes from the call stack used by recursion — in the worst case, the island could cover the whole grid and the DFS goes that deep.

'''
