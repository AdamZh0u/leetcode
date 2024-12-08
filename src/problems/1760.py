from typing import List
import math
class Solution:
    # error 9 要拆成 6和3 然后再拆成 3 和 3 最小是3 如果是4和5 再拆就是432
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        if maxOperations>0:
            x = max(nums)
            nums.remove(x)
            a, b = (x//2,x//2) if x%2==0 else (x//2 + 1, x//2)
            nums = nums + [a, b]
            return self.minimumSize(nums, maxOperations-1 )
        else:
            return max(nums)

class Solution2:
    # 76
    def minimumSize(self, nums: List[int], maxOps: int) -> int:
        low, high = 1, max(nums) # min and max posible bags
        while low < high:
            mid = (low + high) // 2
            if sum((n - 1) // mid for n in nums) <= maxOps: high = mid
            else: low = mid + 1
        return high

class Solution3:
    #100
    def minimumSize(self, nums: List[int], O: int) -> int:
        N = len(nums)
        S = sum(nums)
        G = N+O
        if G >= S: return 1

        def verify(v):
            return sum(math.ceil(n/v) for n in nums) <= G
        
        l = math.ceil(S/G)-1
        h = min(max(nums),math.floor(S/O))
        
        while l<h-1:
            m = (h+l)//2
            if verify(m): h=m
            else: l=m
        return h
    
if __name__ == "__main__":
    nums = [2,4,8,2] 
    maxOperations = 4
    print(Solution().minimumSize(nums, maxOperations))
    # 