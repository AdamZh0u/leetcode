class Solution:
    def canMakeSubsequence(self, source: str, target: str) -> bool:
        targetIdx, targetLen = 0, len(target)  
        for currChar in source:
            # ord Return the integer that represents the character :
            if targetIdx < targetLen and (ord(target[targetIdx]) - ord(currChar)) % 26 < 2: 
                targetIdx += 1  
        return targetIdx == targetLen
    

if __name__ == '__main__':
    source = "abc"
    target = "ad"
    print(Solution().canMakeSubsequence(source, target)) # Output: true
