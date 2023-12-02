# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        result = []

        l1 = 0
        l2 = 0

        len_l1 = len(list1)
        len_l2 = len(list2)

        while True:

            value_l1 = list1[l1] if l1<len_l1 else 100
            value_l2 = list2[l2] if l2<len_l2 else 100

            if value_l1<value_l2:
                result += [value_l1]
                l1 += 1
            elif value_l1>value_l2:
                result += [value_l2]
                l2 += 1
            else:
                result += [value_l1, value_l2]
                l1 += 1
                l2 += 1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        current = head

        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next  
            current = current.next          


        current.next = list1 or list2

        return current.next
            
            
