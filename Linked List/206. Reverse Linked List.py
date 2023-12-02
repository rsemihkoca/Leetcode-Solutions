# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val}, {self.next}"
class Solution:
    """
    Time O(n)
    Space O(n)
    """

    def getItems(self, head: Optional[ListNode]):

        current_node = head
        while current_node:
            yield current_node
            current_node = current_node.next


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        reversed_nodes = None

        for node in self.getItems(head):
            reversed_nodes = ListNode(node.val, reversed_nodes)
        
        return reversed_nodes
        


class Solution(object):

    """
    Time O(n)
    Space O(1)
    """
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev