from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printLinkedList(self):
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

class Solution:
    def reorderLinkedList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head.printLinkedList()

        curr = slow.next
        prev = None
        slow.next = None # bu sekilde slow head'i kesiyor 12345N'den 123N oluyor.
        print("slow, new head")
        head.printLinkedList()

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev.printLinkedList()
        first, second = head, prev

        
        while second:  
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        
        head.printLinkedList()

        

# Test cases
# Test case 1: Odd length linked list
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
sol.reorderLinkedList(head1)
# head1.printLinkedList()  # Expected output: 1 -> 5 -> 2 -> 4 -> 3 -> None

# Test case 2: Even length linked list
# head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# sol = Solution()
# sol.reorderLinkedList(head2)
# head2.printLinkedList()  # Expected output: 1 -> 4 -> 2 -> 3 -> None
