'''250907'''

# 迭代法
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 建立一個虛擬的開頭節點，用一個指標進行串接
    head = ListNode(-1)
    ptr = head

    # 從兩條串列的開頭進行比較，選擇較少的串列接上
    while list1 and list2:
        if list1.val > list2.val:
            ptr.next = list2
            ptr = ptr.next
            list2 = list2.next
        else:
            ptr.next = list1
            ptr = ptr.next
            list1 = list1.next

    # 將非空的串列接上
    if list1:
        ptr.next = list2
    else:
        ptr.next = list1
        
    # 因為 head 是虛擬節點，後面接的一位才是串列開頭
    return head.next

# 遞迴法
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 終止條件：若其中一個為空，回傳另一個
    if not list1:
        return list2
    if not list2:
        return list1

    # 遞迴比較與接續
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
