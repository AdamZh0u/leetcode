import heapq
from typing import List
from bisect import bisect_right

class Solution1:
    # 70
    def maxTwoEvents(self, events):
        events.sort()  # Sort by start time
        pq = []  # Priority queue to store (end_time, value)
        max_value = 0
        ans = 0
        
        for start, end, value in events:
            # Remove all events that end before the current event's start time
            while pq and pq[0][0] < start:
                max_value = max(max_value, heapq.heappop(pq)[1])
            
            # Update the maximum sum of values
            ans = max(ans, max_value + value)
            
            # Push the current event into the priority queue
            heapq.heappush(pq, (end, value))
        
        return ans

class Solution2:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        max_weights = [0]
        max_weight_ends = [-1]

        events.sort(key = lambda x: x[1])

        max_two = 0
        for start, end, weight in events:
            index = bisect_right(max_weight_ends, start - 1) - 1
            
            if weight + max_weights[index] > max_two:
                max_two = weight + max_weights[index]
            if weight > max_weights[-1]:
                max_weights.append(weight)
                max_weight_ends.append(end)
        
        return max_two


if __name__ == '__main__':
    events = [[1,3,2],[4,5,2],[1,5,5]]
    events = [[1,3,2],[4,5,2],[2,4,3]]
    print(Solution2().maxTwoEvents(events))

# 找到事件与事件之间重叠的events 然后做最小生成树？
# 2 约束一个事件为必须，遍历整个
# 大顶堆和小顶堆
# debug运行会改变结果！！