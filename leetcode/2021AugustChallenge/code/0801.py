class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        
        n = len(grid)
        m = len(grid[0])
        islands = {}
        neighbor = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        cnt = 2
        def dfs(cnt, i, j):
            if i < 0 or i >=n or j < 0 or j >= m or grid[i][j] != 1:
                return
            grid[i][j] = cnt
            islands[cnt] += 1
            for neig in neighbor:
                dfs(cnt, i+neig[0], j+neig[1])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islands[cnt] = 0
                    dfs(cnt, i, j)
                    cnt += 1
        if len(islands) == 0 and n > 0 and m > 0:
            return 1
        ans = max(islands.values())
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    continue
                neig_set = set()
                for neig in neighbor:
                    if 0 <= i+neig[0] < n and 0 <= j+neig[1] < m and grid[i+neig[0]][j+neig[1]] != 0:
                        neig_set.add(grid[i+neig[0]][j+neig[1]])
                ans = max(ans, 1 + sum([islands[t] for t in neig_set]))
                
        return ans