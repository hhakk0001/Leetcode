'''250908'''

# 第一次，嘗試快慢指標，通過
def hasCycle(self, head: Optional[ListNode]) -> bool:
    ptr_f = head 
    ptr_s = head

    while ptr_f:
        ptr_f = ptr_f.next
        ptr_s = ptr_s.next

        if ptr_f:
            ptr_f = ptr_f.next
        else:
            return False

        if ptr_f == ptr_s:
            return True
        
    return False

# 快慢指標: 修改過後的版本
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # 兩指標從同個起點開始
    ptr_f = head 
    ptr_s = head

    # 每次移動指標時檢查快指標是否走到底了(None)
    while ptr_f and ptr_f.next:
        ptr_s = ptr_s.next
        ptr_f = ptr_f.next.next

        # 如果兩指標相遇，說明快指標繞了一圈追上慢指標，有環
        if ptr_f is ptr_s:
            return True
    
    # 快指標走到鏈結尾端，無環
    return False

# 雜湊表法
def hasCycle(head: Optional[ListNode]) -> bool:
    # 建立一個雜湊表，紀錄經過的節點
    visited = set()

    # 將遇到的節點存入雜湊表並檢查是否重複遇見
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    
    return False
