class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        reverse_graph=[[] for _ in range(n)]
        outdegree=[0]*n
        for u in range(n):
            outdegree[u]=len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)
        q=deque()
        for i in range(n):
            if outdegree[i]==0:
                q.append(i)
        safe=[False]*n
        while q:
            node=q.popleft()
            safe[node]=True
            for prev in reverse_graph[node]:
                outdegree[prev]-=1
                if outdegree[prev]==0:
                    q.append(prev)
        result=[i for i in range(n) if safe[i]]
        return result
