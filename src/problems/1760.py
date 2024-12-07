from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        if maxOperations>0:
            x = max(nums)
            nums.remove(x)
            a, b = (x//2,x//2) if x%2==0 else (x//2 + 1, x//2)
            nums = nums + [a, b]
            return self.minimumSize(nums, maxOperations-1 )
        else:
            return max(nums)

if __name__ == "__main__":
    nums = [2,4,8,2] 
    maxOperations = 4
    print(Solution().minimumSize(nums, maxOperations))
    # 9 要拆成 6和3 然后再拆成 3 和 3 最小是3 如果是4和5 再拆就是432