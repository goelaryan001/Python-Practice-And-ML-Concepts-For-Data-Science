class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols= len(grid),len(grid[0]) #Number of rows and columns

        visited =set()
        islands=0

        def bfs(r,c):
            q=collections.deque() #using this data structure
            visited.add((r,c))
            q.append((r,c))
            jen
            # Now lloking to expand the island
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c=row+dr, col+dc
                    if(r in range(rows) and c in range(cols) #first check if position is in bounds
                    and grid[r][c] =="1" and
                    (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                      
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in vsisted:
                    bfs(r,c)
                    islands+=1
        return islands