import math


class Solution1:
    #
    def arrangeCoins(self, n: int) -> int:
        x = 1
        while (
            sum(range(x + 1)) < n
        ):  # range(x) is the sequence of integers from 0 to x-1
            print(x, sum(range(x + 1)))
            if sum(range(x + 2)) > n:
                return x - 1
            x += 1
        return 1 

class Solution2:
    # 40
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n >= 0:
            i += 1
            n = n - i
        return i - 1


class Solution3:
    # 100
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8 * n + 1) - 1) / 2)


if __name__ == "__main__":
    n = 8
    print(Solution1().arrangeCoins(n))
    print(Solution2().arrangeCoins(n))
    print(Solution3().arrangeCoins(n))
