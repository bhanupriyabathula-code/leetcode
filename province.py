class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        vis=set()
        def dfs(city):
            for nei in range(n):

                if isConnected[city][nei]==1 and nei not in vis:
                    vis.add(nei)
                    dfs(nei)
        p=0
        for city in range(n):
            if city not in vis:
                vis.add(city)
                dfs(city)
                p+=1
        return p
