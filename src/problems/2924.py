from typing import List

import numpy as np

class Solution1:
    #Rank 10%
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        nodes =  set(range(n)) - set(np.array(edges)[:,1]) 
        return nodes.pop() if len(nodes)==1 else -1
    
class Solution2:
    #Rank 80%
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if len(edges)==0:
            win_nodes = set(range(n))
        else:
            win_nodes =  set(range(n)) - {v for _, v in edges} 
        return win_nodes.pop() if len(win_nodes)==1 else -1
    
class Solution3:
    #Rank 90%
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # 计算每个节点的入度
        indegree = [0] * n
        for _, v in edges:
            indegree[v] += 1
        
        # 找到入度为0的节点
        champion = -1
        for i in range(n):
            if indegree[i] == 0:
                if champion != -1:  # 已经找到一个入度为0的节点
                    return -1
                champion = i
                
        return champion

if __name__ == '__main__':
    n = 5
    edges = [[0,1],[1,2],[2,3],[3,4]]
    # edges = []
    solution = Solution2()
    print(solution.findChampion(n, edges))