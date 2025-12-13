# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""250909"""


# 雙指標解
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa: F821
    ptr_s = ptr_f = head

    # 檢查是否有環
    while ptr_f and ptr_f.next:
        ptr_s = ptr_s.next
        ptr_f = ptr_f.next.next
        if ptr_f is ptr_s:
            break

    else:
        return None

    # 兩指標分別從 head 與相遇點出發，相遇處即為環起點
    ptr_f = head
    while ptr_f is not ptr_s:
        ptr_s = ptr_s.next
        ptr_f = ptr_f.next

    return ptr_f


# 雜湊表法
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa: F821
    # 建立一個雜湊表，紀錄經過的節點
    visited = set()

    # 將遇到的節點存入雜湊表並檢查是否重複遇見
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next

    return None
