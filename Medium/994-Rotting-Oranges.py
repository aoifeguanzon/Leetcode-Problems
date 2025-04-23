'''
Given a grid with fresh and rotten oranges,
find the minimum time for all fresh oranges to rot,
or return -1 if it's impossible.
'''

# Brute force - BFS using lists
def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    queue = []
    fresh_count = 0
    minutes = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh_count += 1
            elif grid[i][j] == 2:
                queue.append((i, j))

    if fresh_count == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        for _ in range(len(queue)):
            x, y = queue.pop(0)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    queue.append((nx, ny))

        minutes += 1

    if fresh_count > 0:
        return -1

    return minutes

'''
Time Complexity: O(m * n) 
Iterate through all m * n cells, and each BFS operation involves popping from the front of the list, which takes O(n) time for each element

Space Complexity: O(m * n) 
Storing grid and queue
'''


# Optimal solution - BFS using collections.deque
from collections import deque

def orangesRotting(grid):
    m, n = len(grid), len(grid[0]) # m = rows, n = columns
    queue = deque()
    fresh_count = 0
    minutes = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1: # if fresh orange is found
                fresh_count += 1
            elif grid[i][j] == 2: # if rotten orange is found
                queue.append((i, j)) # add its position to queue

    if fresh_count == 0: # if no fresh oranges exist
        return 0 # return 0 because there's nothing to rot

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
    
    while queue: # as long as there are rotten oranges in the queue
      # start spreading rot from the originally rotten oranges
        for _ in range(len(queue)): # for all rotten oranges at current minute (ie. rotten oranges in the queue)
          # no i because we don't need to use it 
            x, y = queue.popleft() # remove first rotten orange from the queue and stores its coordinates

            for dx, dy in directions: # for each (of 4 changes in) direction (up, down, left, right) from current orange
                nx, ny = x + dx, y + dy # get one of its neighbours' coordinates
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1: # if neighbour position is within grid and contains a fresh orange
                    grid[nx][ny] = 2 # rot it
                    fresh_count -= 1 # 1 less fresh orange
                    queue.append((nx, ny)) # add the newly rotten orange to the queue for future rounds (it will spread rot to its neighbors next)
                  # newly rotten oranges probably have new neighbours to rot

        minutes += 1

    if fresh_count > 0:
        return -1

    return minutes

'''
Time Complexity: O(m * n)
Iterate through all m * n cells, and each BFS operation involves efficient O(1) popleft() and append() operations using the deque.

Space Complexity: O(m * n) 
Storing grid and deque
'''

'''
[ [2, 1, 0],
  [1, 1, 1],
  [0, 1, 2] ]
Queue: [(0, 0), (2, 2)] (initial rotten oranges).

Fresh Count: 
5 (5 fresh oranges).

First Round:
Process (0, 0): Check neighbors.
(1, 0) → Fresh, rot it, add (1, 0) to queue, fresh_count = 4.
(0, 1) → Fresh, rot it, add (0, 1) to queue, fresh_count = 3.
Queue = [(2, 2), (1, 0), (0, 1)].

Process (2, 2): Check neighbors.
(1, 2) → Fresh, rot it, add (1, 2) to queue, fresh_count = 2.
(2, 1) → Fresh, rot it, add (2, 1) to queue, fresh_count = 1.
Queue = [(1, 0), (0, 1), (1, 2), (2, 1)].

Second Round:

Process (1, 0): Check neighbors.
(1, 1) → Fresh, rot it, add (1, 1) to queue, fresh_count = 0.
Queue = [(0, 1), (1, 2), (2, 1), (1, 1)].

Process (0, 1): Check neighbors.
(1, 1) → Already rotten, skip.
No other fresh neighbors.
Queue = [(1, 2), (2, 1), (1, 1)].

Process (1, 2): Check neighbors.
No fresh neighbors.
Queue = [(2, 1), (1, 1)].

Process (2, 1): Check neighbors.
No fresh neighbors.
Queue = [(1, 1)].

Grid after second round:
[ [2, 2, 0],
  [2, 2, 2],
  [0, 2, 2] ]
Fresh Count: 0 (all fresh oranges have rotted).
(Zeros are empty cells)

Queue: Empty, so the process ends.
'''
