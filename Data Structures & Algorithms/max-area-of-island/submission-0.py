class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i,j):
            if i >= len(grid) or j>= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0 or (i,j) in visited :
                return 0 

            visited.add((i,j))
            
            a1 = dfs(i, j+1)
            a2 = dfs(i, j-1)
            a3 = dfs(i+1, j)
            a4 = dfs(i-1, j)
            return 1 + a1 + a2 + a3 + a4
            

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = dfs(i,j)
                max_area = max(max_area, area)
                    

        return max_area