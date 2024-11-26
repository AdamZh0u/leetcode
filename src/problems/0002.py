# Add Two Numbers

## hints:
## - use dummy node to handle the carry
## - 链表的构建方式完全是bottom up的，先创建头节点，然后逐个添加节点，最后返回头节点。

from typing import Optional
from src.data_obj.LinkedList import ListNode, list_to_linkedlist,print_linkedlist

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from the lists or 0 if list ended
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            
            # Create new node with ones digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
    

def genertate(list1 = [1,2,3], list2 = [2,3,4]):
    l1 = list_to_linkedlist(list1)
    l2 = list_to_linkedlist(list2)
    return l1, l2 

if __name__ == '__main__':
    l1,l2 =  genertate(list1 = [9,9,9,9,], list2 = [9])

    l3 = Solution().addTwoNumbers(l1,l2) 
    print_linkedlist(l3)



