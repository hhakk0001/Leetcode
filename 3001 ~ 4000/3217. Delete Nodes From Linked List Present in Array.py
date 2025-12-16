"""251101"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# FT: Set
def modifiedList(self, nums: list[int], head: [ListNode]) -> [ListNode]:
    delete_set = set(nums)
    dummy = ListNode(0, head)
    cur = dummy

    while cur.next:
        if cur.next.val in delete_set:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next
