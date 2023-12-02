



# Linked List Data Structure

"""
Insert at the beginning of the linked list

"""


class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self) -> str:
        return f"Node({self.data}), {self.next}"
    
class LinkedList:
    
    def __init__(self, head=None):
        self.head = head
        self.length = 0
        self.findLength(head)

    def findLength(self, head:Node) -> int:

        while head:
            self.length += 1
            head = head.next


    def __repr__(self) -> str:
        return f"{self.head}"
    
    def __len__(self) -> int:
        return self.length
    
    # def insert(self, value: Node, index: int):

    #     if -self.length <= index:
    #         index = index + self.length
        
    #     elif index < self.length:
    #         index = index

    #     else:
    #         raise "Invalid Index"
        
    #     if index == 0:
    #         self.head = Node
    #         return
        
    #     curr = self.head 

    #     while index<=0:
    #         if index == 0:
    #             curr = 

    #         prev = curr 
    #         next = curr.next
    #         curr = curr.next
    #         index -= 1

        

    #     while index:
    #         if index == 0:

    #         ll = ll.next
            
            



    #         index -= 1


    
second = Node(15, None)
first = Node(8, second)
head = Node(5, first)

LinkedList = LinkedList(head)

print(len(LinkedList))
