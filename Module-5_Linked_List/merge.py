"""
Task: Two
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

    def merge(self, list1, list2):
        dummy = Node()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next


# Test the solution
linked_list1 = LinkedList()
for i in [1, 2, 4]:
    linked_list1.add_node(i)

linked_list2 = LinkedList()
for i in [1, 3, 4]:
    linked_list2.add_node(i)

merged_list = linked_list1.merge(linked_list1.head, linked_list2.head)

# Print the merged list
current = merged_list
while current:
    print(current.val, end=' ')
    current = current.next
