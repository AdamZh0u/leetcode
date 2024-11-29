from typing import List

class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        # 20% 
        distincts = []
        for i in nums:
            if i not in distincts:
                distincts.append(i)
        distincts.sort(reverse=True)
        return distincts[2] if len(distincts)>=3 else max(distincts)
    
class Solution2:
    # 100%
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        for n in nums[::-1]:
            if n not in res:
                res.append(n)

            if len(res) == 3:
                return res[-1]

        return res[0]
    

if __name__ == '__main__':
    nums = [3, 2, 1]
    print(Solution1().thirdMax(nums))
    print(Solution2().thirdMax(nums))