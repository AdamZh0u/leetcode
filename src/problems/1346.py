from typing import List
class Solution1:
    # 7 
    def checkIfExist(self, arr: List[int]) -> bool:
        v = False
        for i,x in enumerate(arr):
            for j,y in enumerate(arr):
                if x==2*y and (i!=j):
                    v = True
        return v

class Solution2:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            # Check if 2 * num or num / 2 exists in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        # No valid pair found
        return False
    
if __name__ == '__main__':
    arr = [10,2,5,3]
    print(Solution1().checkIfExist(arr))