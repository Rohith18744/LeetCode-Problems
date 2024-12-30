class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        Provinces=0
        visited=[False]*n

        def dfs(node):
            visited[node]=True
            for neighbor in range(n):
                if isConnected[node][neighbor]==1 and not visited[neighbor]:
                    dfs(neighbor)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                Provinces+=1
        return Provinces

        