class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        Mod=10**9+7
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        q=deque([(1,0,-1)])
        mxlvl=0
        while q:
            node, level, parent = q.popleft()
            mxlvl=max(mxlvl,level)
            for nei in adj[node]:
                if nei != parent: q.append((nei,level+1,node))

        all=pow(2,mxlvl,Mod)
        odd=(all*pow(2,-1,Mod))%Mod
        return odd

        