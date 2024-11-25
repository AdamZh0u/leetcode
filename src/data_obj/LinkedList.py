# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(arr):
    """
    将Python列表转换为链表
    
    参数:
        arr: List - 输入列表
        
    返回:
        ListNode - 链表的头节点
    """
    if not arr:
        return None
        
    # 创建头节点
    head = ListNode(arr[0])
    current = head
    
    # 遍历列表创建其余节点
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

# 用于打印链表的辅助函数
def print_linkedlist(head):
    """
    打印链表中的所有值
    
    参数:
        head: ListNode - 链表的头节点
    """
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))