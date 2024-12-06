from typing import List
from bisect import bisect_left

class Solution:
    # time limit exceeded
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ls = []
        for i in range(1,n+1):
            if i not in banned: 
                if sum(ls)+i <= maxSum:
                    ls.append(i)
                else:
                    return len(ls)
        return len(ls)

class Solution2:
    # 5.2%
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        ls = [i for i in range(1,n+1) if i not in banned_set]
        cumsum = [sum(ls[:i]) for i in range(1,len(ls)+1) if sum(ls[:i]) <= maxSum]
        return len(cumsum)
    
class Solution3:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        temp = 0
        banned = set(banned)
        for i in range(1, n + 1):
            if temp >= maxSum or temp + i > maxSum: break
            elif i not in banned:
                temp += i
                ans += 1
        return ans
    
if __name__ == '__main__':
    banned = [11]
    n = 7
    maxSum = 50
    print(Solution3().maxCount(banned, n, maxSum))