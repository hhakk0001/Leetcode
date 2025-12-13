"""250918"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 指標解
def reverseList(self, head: ListNode) -> ListNode:
    prev = None  # 紀錄新方向的上一個節點，即下一個節點

    while head:
        next_node = head.next  # 暫存原方向的下一個節點
        head.next = prev  # 反轉當前節點的指標方向
        prev = head  # prev, head 指標向前
        head = next_node

    # 此時 head 指向 None，prev 指向反轉後的串列頭部
    return prev


# 遞迴解
def reverseList(self, head: ListNode) -> ListNode:
    # base case: 空串列或單一節點
    if not head or not head.next:
        return head

    reversed_head = self.reverseList(head.next)  # 反轉剩餘的部分

    # 反轉操作
    head.next.next = head  # 把下一個節點的指向反轉
    head.next = None  # 斷開自己的指向

    return reversed_head
