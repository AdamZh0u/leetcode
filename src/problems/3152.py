from typing import List
from itertools import pairwise
class Solution:
    # time exceed
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ls = []
        for query in queries:
            left, right = query[0], query[1]
            sub_array = nums[left:right+1]
            res = []
            for i, j in pairwise(sub_array):
                res.append(False if ((i+j) % 2 == 0) else True)# 两个数不同为奇数或者偶数
            ls.append(all(res))
        return ls
    
class Solution2:
    # time exceed
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ls_res = []
        ls = [0]*len(nums)
        for i, (x,y) in enumerate(pairwise(nums)):
            if (x+y) % 2 == 0:
                ls[i] = 1
        for query in queries:
            left, right = query[0], query[1]
            res = sum(ls[left:right]) == 0
            ls_res.append(res)
        return ls_res

class Solution3:
    # 100
    # 构建一个cumsum序列 如果收尾不相等则说明有变化 在第一个循环sum  第二个就不用sum了！
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        runningSum = 0
        partialSum = []
        oddEven = None

        for num in nums:
            if num % 2 == oddEven:
                runningSum += 1
            oddEven = num % 2
            partialSum.append(runningSum)

        out = []

        for start, end in queries:
            if partialSum[start] == partialSum[end]:
                out.append(True)
            else:
                out.append(False)
        return out

if __name__ == "__main__":
    nums = [4,3,1,6]
    queries = [[0,2],[2,3]]
    print(Solution3().isArraySpecial(nums, queries))