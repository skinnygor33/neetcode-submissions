class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        number_of_islands = 0

        visited = [[False] * cols for _ in range(rows)] 


        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:   
                return
            if visited[i][j] == True or grid[i][j] == "0":
                return False
            visited[i][j] = True 
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return True 
        
        for r in range(rows):
            for c in range(cols): 
                if dfs(r,c) == True: 
                    number_of_islands += 1
        return number_of_islands
        



        