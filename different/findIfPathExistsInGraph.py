# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        def findPaths(start):
            result = []

            for path in (x for x in edges if start in x):
                for p in path:
                    if p != start and p not in result:
                        result.append(p)
                    
            return result

        ways = {}
        for mainRoad in set(sum(edges, [])):
            ways[mainRoad] = findPaths(mainRoad)

        for mainRoad in ways:
            print(f'Пути {mainRoad}', ways[mainRoad])
        
        return False
        
n = Solution()
print(n.validPath(1,[[0,1],[1,2],[1,2],[2,3],[3,4],[4,5],[5,6]], 0, 2))