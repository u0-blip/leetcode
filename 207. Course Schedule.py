from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # building the adjacency list, and in degree
        in_dgree = {i: 0 for i in range(numCourses)}
        adj_list = {i: [] for i in range(numCourses)}
        
        for p in prerequisites:
            parent, child= p[0], p[1]
            in_dgree[child] += 1
            adj_list[parent].append(child)
        # find the source

        # print(adj_list)
        # print(in_dgree)
        sources = deque()
        for k in in_dgree:
            if in_dgree[k] == 0:
                sources.append(k)

        # print(sources)
        # sort by putting the source into a queue and decrease the in degress
        sorted_list = []
        while sources:
            v = sources.popleft()
            sorted_list.append(v)
            for child in adj_list[v]:
                in_dgree[child] -= 1
                if in_dgree[child] == 0:
                    sources.append(child)
        # print(sorted_list)
        
        return len(sorted_list) == numCourses


a = 3
b = [[1,0]]
s = Solution()
print(s.canFinish(a, b))