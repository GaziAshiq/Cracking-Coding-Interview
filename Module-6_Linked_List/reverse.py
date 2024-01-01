"""
Task: One
Time complexity: O(n)
Space complexity: O(1)
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


# Test the solution
linked_list = LinkedList()
for i in [1, 2, 3, 4, 5]:
    linked_list.add_node(i)

linked_list.reverse()

# Print the reversed list
current = linked_list.head
while current:
    print(current.val, end=' ')
    current = current.next
